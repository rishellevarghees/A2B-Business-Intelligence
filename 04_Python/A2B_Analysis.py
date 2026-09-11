# ============================================================
# A2B BUSINESS INTELLIGENCE PROJECT
# PHASE 1 — PHASE 5
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# FILE LOCATION
# ============================================================

file_path = r"C:\A2B_Business_Intelligence\04_Python\data\A2B_Clean_Data.xlsx"


# ============================================================
# PHASE 1 — FINANCIAL ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("PHASE 1 — FINANCIAL ANALYSIS")
print("=" * 70)

financials = pd.read_excel(
    file_path,
    sheet_name="A2B_Financials"
)

financials["Revenue_Growth_%"] = (
    financials["Revenue_Operations_Cr"].pct_change() * 100
)

financials["Profit_Growth_%"] = (
    financials["PAT_Cr"].pct_change() * 100
)

financials["Profit_Margin_%"] = (
    financials["PAT_Cr"]
    / financials["Revenue_Operations_Cr"]
) * 100

financials[
    [
        "Revenue_Growth_%",
        "Profit_Growth_%",
        "Profit_Margin_%"
    ]
] = financials[
    [
        "Revenue_Growth_%",
        "Profit_Growth_%",
        "Profit_Margin_%"
    ]
].round(2)

print("\nFinancial Analysis:")
print(
    financials[
        [
            "FY",
            "Revenue_Operations_Cr",
            "PAT_Cr",
            "Revenue_Growth_%",
            "Profit_Growth_%",
            "Profit_Margin_%"
        ]
    ]
)

highest_revenue = financials.loc[
    financials["Revenue_Operations_Cr"].idxmax()
]

highest_profit = financials.loc[
    financials["PAT_Cr"].idxmax()
]

print("\nHighest Revenue Year:")
print(
    f"{int(highest_revenue['FY'])} → "
    f"₹{highest_revenue['Revenue_Operations_Cr']} Cr"
)

print("\nHighest Profit Year:")
print(
    f"{int(highest_profit['FY'])} → "
    f"₹{highest_profit['PAT_Cr']} Cr"
)

latest = financials.iloc[-1]

print("\nBusiness Signal:")

if (
    latest["Revenue_Growth_%"] > 0
    and latest["Profit_Growth_%"] < 0
):
    print("Revenue increased while profit declined.")
else:
    print("Revenue and profit are moving in the same direction.")


# ============================================================
# PHASE 2 — GEOGRAPHIC / OUTLET ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("PHASE 2 — GEOGRAPHIC / OUTLET ANALYSIS")
print("=" * 70)

outlets = pd.read_excel(
    file_path,
    sheet_name="A2B_114_Outlets"
)

print(
    "\nTotal retail outlets:",
    len(outlets)
)

print(
    "Duplicate Outlet IDs:",
    outlets["Outlet_ID"].duplicated().sum()
)

regional_outlets = (
    outlets
    .groupby("Official_Region")
    .size()
    .reset_index(name="Outlet_Count")
    .sort_values(
        "Outlet_Count",
        ascending=False
    )
)

regional_outlets["Outlet_Share_%"] = (
    regional_outlets["Outlet_Count"]
    / regional_outlets["Outlet_Count"].sum()
    * 100
).round(2)

print("\nRegional Outlet Analysis:")
print(regional_outlets)

top_two_share = (
    regional_outlets
    .head(2)["Outlet_Share_%"]
    .sum()
)

print(
    "\nTop two regions account for:",
    round(top_two_share, 2),
    "% of listed outlets."
)


# ============================================================
# PHASE 3 — MENU & PRICING ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("PHASE 3 — MENU & PRICING ANALYSIS")
print("=" * 70)

menu = pd.read_excel(
    file_path,
    sheet_name="A2B_Menu_Pricing"
)

# Clean column names
menu.columns = (
    menu.columns
    .astype(str)
    .str.strip()
)

print("\nMenu Columns:")
print(menu.columns.tolist())

print("\nMenu Data:")
print(menu)

print(
    "\nTotal products in public menu sample:",
    len(menu)
)


# ------------------------------------------------------------
# Products by category
# ------------------------------------------------------------

category_counts = (
    menu
    .groupby("Category")
    .size()
    .reset_index(name="Product_Count")
    .sort_values(
        "Product_Count",
        ascending=False
    )
)

print("\nProducts by Category:")
print(category_counts)


# ------------------------------------------------------------
# Convert public price to numeric value
# ------------------------------------------------------------

menu["Price_Numeric"] = (
    menu["Web_Price"]
    .astype(str)
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.extract(r"(\d+(?:\.\d+)?)")[0]
    .astype(float)
)


# ------------------------------------------------------------
# Average price
# ------------------------------------------------------------

average_price = menu["Price_Numeric"].mean()

print(
    "\nAverage listed web-shop price:",
    round(average_price, 2)
)


# ------------------------------------------------------------
# Price range
# ------------------------------------------------------------

minimum_price = menu["Price_Numeric"].min()

maximum_price = menu["Price_Numeric"].max()

print(
    "\nPublic web-shop price range:",
    round(minimum_price, 2),
    "to",
    round(maximum_price, 2)
)


# ------------------------------------------------------------
# Most expensive products
# ------------------------------------------------------------

expensive_products = (
    menu
    .sort_values(
        "Price_Numeric",
        ascending=False
    )
    .head(5)
)

print("\nTop 5 Most Expensive Products:")

print(
    expensive_products[
        [
            "Product",
            "Category",
            "Pack_Size",
            "Web_Price",
            "Price_Numeric"
        ]
    ]
)


# ------------------------------------------------------------
# Least expensive products
# ------------------------------------------------------------

cheap_products = (
    menu
    .sort_values(
        "Price_Numeric",
        ascending=True
    )
    .head(5)
)

print("\nTop 5 Lowest Priced Products:")

print(
    cheap_products[
        [
            "Product",
            "Category",
            "Pack_Size",
            "Web_Price",
            "Price_Numeric"
        ]
    ]
)


# ------------------------------------------------------------
# Pricing observation
# ------------------------------------------------------------

print("\nPricing Observation:")

print(
    "The current public pricing sample consists "
    "entirely of sweet products."
)

print(
    "Prices shown are public web-shop starting/listed "
    "prices and should not be treated as restaurant "
    "dine-in prices."
)
# ============================================================
# PHASE 4 — COMPETITOR ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("PHASE 4 — COMPETITOR ANALYSIS")
print("=" * 70)

competitors = pd.read_excel(
    file_path,
    sheet_name="Competitors"
)

# Clean column names
competitors.columns = (
    competitors.columns
    .astype(str)
    .str.strip()
)

print("\nCompetitor Data:")
print(competitors)

print(
    "\nNumber of competitor records:",
    len(competitors)
)


# ------------------------------------------------------------
# Public footprint comparison
# ------------------------------------------------------------

print("\nPublic Footprint Comparison:")

print(
    competitors[
        [
            "Company",
            "Footprint",
            "Public_Footprint_Claim"
        ]
    ]
)


# ------------------------------------------------------------
# Identify international competitors
# ------------------------------------------------------------

international_competitors = competitors[
    competitors["Footprint"]
    .astype(str)
    .str.contains(
        "International|Global",
        case=False,
        na=False
    )
]

print(
    "\nInternational / Global Footprint:"
)

print(
    international_competitors[
        [
            "Company",
            "Public_Footprint_Claim"
        ]
    ]
)


# ============================================================
# PHASE 5 — INTEGRATED BUSINESS INSIGHTS
# ============================================================

print("\n" + "=" * 70)
print("PHASE 5 — INTEGRATED BUSINESS INSIGHTS")
print("=" * 70)

# ------------------------------------------------------------
# 1. FINANCIAL POSITION
# ------------------------------------------------------------

print("\n1. FINANCIAL POSITION")

# Get latest financial year
latest_row = financials.iloc[-1]

latest_year = int(latest_row["FY"])
latest_revenue = float(latest_row["Revenue_Operations_Cr"])
latest_profit = float(latest_row["PAT_Cr"])
latest_margin = float(latest_row["Profit_Margin_%"])
latest_revenue_growth = float(latest_row["Revenue_Growth_%"])
latest_profit_growth = float(latest_row["Profit_Growth_%"])

print(
    f"A2B generated ₹{latest_revenue:.2f} Cr "
    f"of operating revenue in FY{latest_year}."
)

print(
    f"PAT was ₹{latest_profit:.2f} Cr "
    f"with a net profit margin of {latest_margin:.2f}%."
)

print(
    f"Revenue growth was {latest_revenue_growth:.2f}%, "
    f"while profit growth was {latest_profit_growth:.2f}%."
)

if latest_revenue_growth > 0 and latest_profit_growth < 0:
    print(
        "Business signal: Revenue increased while profit declined, "
        "indicating pressure on profitability."
    )

# ------------------------------------------------------------
# 2. Profitability
# ------------------------------------------------------------

print("\n2. PROFITABILITY")

if (
    latest["Revenue_Growth_%"] > 0
    and latest["Profit_Growth_%"] < 0
):

    print(
        "Revenue increased while profit declined "
        "in FY2025."
    )

    print(
        "This indicates profitability pressure "
        "despite continued revenue growth."
    )


# ------------------------------------------------------------
# 3. Geographic concentration
# ------------------------------------------------------------

print("\n3. GEOGRAPHIC CONCENTRATION")

print(
    f"The top two regional clusters account for "
    f"{round(top_two_share, 2)}% of listed outlets."
)


# ------------------------------------------------------------
# 4. Menu and pricing
# ------------------------------------------------------------

print("\n4. MENU / PRICING")

print(
    f"The current public web-shop sample contains "
    f"{len(menu)} products."
)

print(
    f"The average listed price is ₹"
    f"{round(average_price, 2)}."
)

print(
    f"The observed price range is ₹"
    f"{round(minimum_price, 2)} to ₹"
    f"{round(maximum_price, 2)}."
)


# ------------------------------------------------------------
# 5. Competitive position
# ------------------------------------------------------------

print("\n5. COMPETITIVE POSITION")

print(
    f"The project currently tracks "
    f"{len(competitors)} competitor records."
)

print(
    f"{len(international_competitors)} tracked competitors "
    "have an international/global footprint."
)


# ------------------------------------------------------------
# 6. Overall conclusion
# ------------------------------------------------------------

print("\n6. OVERALL BUSINESS CONCLUSION")

print(
    "A2B demonstrates strong revenue scale and "
    "a substantial regional retail footprint."
)

print(
    "However, FY2025 shows revenue growth alongside "
    "a decline in PAT."
)

print(
    "The next analytical focus should examine the "
    "relationship between expansion, costs, pricing, "
    "customer experience and competition."
)


# ============================================================
# CHART 1 — REVENUE TREND
# ============================================================

print("\nCreating Revenue Trend Chart...")

plt.figure(figsize=(9, 5))

plt.plot(
    financials["FY"],
    financials["Revenue_Operations_Cr"],
    marker="o"
)

plt.title("A2B Revenue Trend")

plt.xlabel("Financial Year")

plt.ylabel("Revenue (₹ Cr)")

plt.grid(
    True,
    alpha=0.3
)

plt.tight_layout()

plt.show()


# ============================================================
# CHART 2 — PROFIT TREND
# ============================================================

print("\nCreating Profit Trend Chart...")

plt.figure(figsize=(9, 5))

plt.plot(
    financials["FY"],
    financials["PAT_Cr"],
    marker="o"
)

plt.title("A2B Profit Trend")

plt.xlabel("Financial Year")

plt.ylabel("PAT (₹ Cr)")

plt.grid(
    True,
    alpha=0.3
)

plt.tight_layout()

plt.show()


# ============================================================
# CHART 3 — REGIONAL OUTLETS
# ============================================================

print("\nCreating Regional Outlet Chart...")

plt.figure(figsize=(10, 6))

plt.bar(
    regional_outlets["Official_Region"],
    regional_outlets["Outlet_Count"]
)

plt.title(
    "A2B Retail Outlets by Region"
)

plt.xlabel("Region")

plt.ylabel("Number of Outlets")

plt.xticks(
    rotation=45,
    ha="right"
)

plt.tight_layout()

plt.show()


# ============================================================
# CHART 4 — MENU CATEGORIES
# ============================================================

print("\nCreating Menu Category Chart...")

if not category_counts.empty:

    plt.figure(figsize=(9, 5))

    plt.bar(
        category_counts["Category"],
        category_counts["Product_Count"]
    )

    plt.title(
        "A2B Products by Category"
    )

    plt.xlabel("Category")

    plt.ylabel("Number of Products")

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    plt.show()


# ============================================================
# EXPORT PYTHON RESULTS
# ============================================================

output_file = (
    r"C:\A2B_Business_Intelligence"
    r"\04_Python\data\A2B_Python_Analysis_Output.xlsx"
)

with pd.ExcelWriter(
    output_file,
    engine="openpyxl"
) as writer:

    financials.to_excel(
        writer,
        sheet_name="Financial_Analysis",
        index=False
    )

    regional_outlets.to_excel(
        writer,
        sheet_name="Regional_Analysis",
        index=False
    )

    category_counts.to_excel(
        writer,
        sheet_name="Menu_Categories",
        index=False
    )

    expensive_products.to_excel(
        writer,
        sheet_name="Top_Expensive",
        index=False
    )

    cheap_products.to_excel(
        writer,
        sheet_name="Top_Cheap",
        index=False
    )

    competitors.to_excel(
        writer,
        sheet_name="Competitors",
        index=False
    )


# ============================================================
# END
# ============================================================

print("\n" + "=" * 70)
print("PYTHON ANALYSIS FINISHED")
print("=" * 70)

print(
    "\nAnalysis output saved to:"
)

print(output_file)