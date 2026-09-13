# A2B Business Intelligence & Data Analytics
## Project Documentation

---

## 1. Project Overview

This project analyzes A2B business data to understand the company's financial performance, retail outlet distribution, international expansion, product pricing, and competitive landscape.

The project follows an end-to-end Business Intelligence workflow, starting with raw data preparation and ending with an interactive Power BI dashboard.

---

## 2. Project Objectives

The main objectives are:

1. Analyze A2B's financial performance.
2. Measure revenue and profit growth.
3. Evaluate profit margins.
4. Analyze retail outlet distribution by region.
5. Identify regional concentration in the outlet network.
6. Examine A2B's international presence.
7. Analyze product categories and pricing.
8. Compare A2B's footprint with selected competitors.
9. Present the findings through an interactive Power BI dashboard.

---

## 3. Data Sources

The project uses structured business datasets covering:

- Financial performance
- Retail outlets
- International locations
- Product and menu pricing
- Competitor information

Some information, particularly international and competitor information, is based on publicly available data.

---

## 4. Data Preparation

The data preparation process involved:

- Organizing raw datasets
- Cleaning and structuring data
- Standardizing column names
- Preparing numerical fields for analysis
- Removing/handling unsuitable formatting
- Preparing datasets for Python and Power BI
- Verifying outlet records and duplicate Outlet IDs

---

## 5. Financial Analysis

Financial analysis covers FY2023 to FY2025.

### Key Metrics

| Metric | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Revenue (₹ Cr) | 1193.20 | 1392.70 | 1487.52 |
| PAT (₹ Cr) | — | 39.12 | 36.19 |

### FY2025 Metrics

- Revenue: ₹1,487.52 Cr
- PAT: ₹36.19 Cr
- Revenue Growth: 6.81%
- Profit Growth: -7.49%
- Profit Margin: 2.43%

### Interpretation

A2B's revenue increased in FY2025, while PAT declined compared with FY2024.

This indicates that revenue growth did not translate into equivalent profit growth.

---

## 6. Retail Outlet Analysis

The project analyzes 114 retail outlets.

### Key Findings

- Total retail outlets: 114
- Duplicate Outlet IDs: 0
- Top 2 regional concentration: 72.81%

The concentration of outlets in the top two regions indicates that a substantial portion of the physical retail network is concentrated geographically.

---

## 7. International Expansion

The international dataset covers 6 countries.

The analysis is used to understand A2B's geographic presence outside its primary domestic footprint.

---

## 8. Product & Pricing Analysis

The available public product dataset contains 8 products.

### Key Metrics

- Products tracked: 8
- Product categories: 1
- Average product price: ₹264.58
- Highest product price: ₹392.86
- Lowest product price: ₹190.47

The current product sample is concentrated in the Sweet category.

---

## 9. Competitor Analysis

The project tracks 3 competitor records using publicly available footprint information.

The competitor analysis is intended to provide contextual information about A2B's market footprint.

---

## 10. Python Analysis

Python was used for:

- Data loading
- Data cleaning
- Aggregation
- Growth calculations
- Margin calculations
- Outlet analysis
- Product pricing analysis
- Competitive analysis
- Visualization
- Excel output generation

Main Python file:

`04_Python/A2B_Analysis.py`

---

## 11. SQL Analysis

SQL was used to structure and work with outlet-related data.

Main SQL file:

`03_SQL/A2B_Load_114_Outlets.sql`

---

## 12. Power BI Dashboard

The Power BI report contains three main pages:

### Executive Overview

Provides a high-level view of:

- Revenue
- PAT
- Revenue growth
- Profit growth
- Profit margin
- Revenue trend
- Profit trend
- Regional outlet distribution
- Product overview

### Expansion Intelligence

Focuses on:

- Regional outlet distribution
- Top 2 region concentration
- Retail outlet count
- International locations
- International expansion

### Customer & Menu Intelligence

Focuses on:

- Product pricing
- Product price comparison
- Competitor landscape
- Competitor footprint
- Menu intelligence

---

## 13. Business Insights

The analysis identifies the following major insights:

### Financial

Revenue continues to grow, but FY2025 PAT declined.

### Profitability

The FY2025 profit margin is 2.43%, indicating that only a small portion of operating revenue is retained as PAT.

### Geographic Concentration

The top two regions account for 72.81% of the retail outlet network.

### International Expansion

A2B has an international presence across 6 countries in the analyzed dataset.

### Pricing

The tracked product sample has an average price of ₹264.58, with prices ranging from ₹190.47 to ₹392.86.

### Competition

Competitor footprint information provides additional context for evaluating A2B's market presence.

---

## 14. Limitations

The analysis has several limitations:

- The available product dataset contains only 8 publicly tracked products.
- Customer transaction-level data was not available.
- Competitor analysis is based on selected public information.
- Historical outlet expansion data is limited.
- The project focuses on descriptive and diagnostic analytics rather than prediction.

---

## 15. Future Scope

Future improvements could include:

- Customer transaction analysis
- Customer segmentation
- Product-level sales analysis
- Region-level revenue analysis
- Historical outlet expansion analysis
- Automated data pipelines
- Automated Power BI refresh
- Forecasting after sufficient historical data becomes available
- Expanded competitor benchmarking

---

## 16. Conclusion

This project demonstrates an end-to-end Business Intelligence workflow using Python, SQL, Excel, and Power BI.

The analysis converts business data into structured insights covering financial performance, geographic distribution, international expansion, product pricing, and competitive positioning.

The final Power BI dashboard provides a consolidated view that can help users quickly understand A2B's business performance and identify areas requiring further investigation.