-- ============================================================
-- A2B BUSINESS INTELLIGENCE PROJECT
-- SQL ANALYSIS
-- Database: a2b_business_intelligence
-- ============================================================

USE a2b_business_intelligence;


-- ============================================================
-- 1. VERIFY TOTAL OUTLETS
-- ============================================================

SELECT COUNT(*) AS total_outlets
FROM a2b_outlets;


-- ============================================================
-- 2. CHECK FOR DUPLICATE OUTLET IDs
-- ============================================================

SELECT
    outlet_id,
    COUNT(*) AS duplicate_count
FROM a2b_outlets
GROUP BY outlet_id
HAVING COUNT(*) > 1;


-- ============================================================
-- 3. CHECK FOR MISSING OUTLET IDs
-- ============================================================

SELECT COUNT(*) AS missing_outlet_ids
FROM a2b_outlets
WHERE outlet_id IS NULL
   OR outlet_id = '';


-- ============================================================
-- 4. CHECK FOR MISSING OUTLET NAMES
-- ============================================================

SELECT COUNT(*) AS missing_outlet_names
FROM a2b_outlets
WHERE outlet_name IS NULL
   OR outlet_name = '';


-- ============================================================
-- 5. CHECK FOR MISSING REGIONS
-- ============================================================

SELECT COUNT(*) AS missing_regions
FROM a2b_outlets
WHERE official_region IS NULL
   OR official_region = '';


-- ============================================================
-- 6. OUTLETS BY REGION
-- ============================================================

SELECT
    official_region,
    COUNT(*) AS outlet_count
FROM a2b_outlets
GROUP BY official_region
ORDER BY outlet_count DESC;


-- ============================================================
-- 7. REGIONAL OUTLET SHARE
-- ============================================================

SELECT
    official_region,
    COUNT(*) AS outlet_count,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM a2b_outlets),
        2
    ) AS outlet_share_pct
FROM a2b_outlets
GROUP BY official_region
ORDER BY outlet_share_pct DESC;


-- ============================================================
-- 8. YEAR-OVER-YEAR REVENUE GROWTH
-- ============================================================

SELECT
    financial_year,
    revenue_operations_cr,
    ROUND(
        (
            revenue_operations_cr -
            LAG(revenue_operations_cr)
            OVER (ORDER BY financial_year)
        )
        /
        LAG(revenue_operations_cr)
        OVER (ORDER BY financial_year) * 100,
        2
    ) AS revenue_growth_pct
FROM a2b_financials;


-- ============================================================
-- 9. YEAR-OVER-YEAR PAT GROWTH
-- ============================================================

SELECT
    financial_year,
    pat_cr,
    ROUND(
        (
            pat_cr -
            LAG(pat_cr)
            OVER (ORDER BY financial_year)
        )
        /
        LAG(pat_cr)
        OVER (ORDER BY financial_year) * 100,
        2
    ) AS pat_growth_pct
FROM a2b_financials;


-- ============================================================
-- 10. NET PROFIT MARGIN
-- ============================================================

SELECT
    financial_year,
    revenue_operations_cr,
    pat_cr,
    ROUND(
        pat_cr / revenue_operations_cr * 100,
        2
    ) AS net_profit_margin_pct
FROM a2b_financials;


-- ============================================================
-- 11. HIGHEST-OUTLET REGION
-- ============================================================

SELECT
    official_region,
    COUNT(*) AS outlet_count
FROM a2b_outlets
GROUP BY official_region
ORDER BY outlet_count DESC
LIMIT 1;


-- ============================================================
-- 12. AVERAGE MENU PRICE
-- ============================================================

SELECT
    ROUND(AVG(web_price), 2) AS average_web_price
FROM a2b_menu;


-- ============================================================
-- 13. HIGHEST-PRICED PRODUCTS
-- ============================================================

SELECT
    product_name,
    category,
    web_price
FROM a2b_menu
ORDER BY web_price DESC;


-- ============================================================
-- 14. LOWEST-PRICED PRODUCTS
-- ============================================================

SELECT
    product_name,
    category,
    web_price
FROM a2b_menu
ORDER BY web_price ASC
LIMIT 3;


-- ============================================================
-- 15. PRODUCTS BY CATEGORY
-- ============================================================

SELECT
    category,
    COUNT(*) AS product_count
FROM a2b_menu
GROUP BY category
ORDER BY product_count DESC;


-- ============================================================
-- 16. FINANCIAL PERFORMANCE SUMMARY
-- ============================================================

SELECT
    financial_year,
    revenue_operations_cr AS revenue_cr,
    pat_cr AS profit_cr,

    ROUND(
        pat_cr / revenue_operations_cr * 100,
        2
    ) AS profit_margin_pct,

    ROUND(
        (
            revenue_operations_cr -
            LAG(revenue_operations_cr)
            OVER (ORDER BY financial_year)
        )
        /
        LAG(revenue_operations_cr)
        OVER (ORDER BY financial_year) * 100,
        2
    ) AS revenue_growth_pct,

    ROUND(
        (
            pat_cr -
            LAG(pat_cr)
            OVER (ORDER BY financial_year)
        )
        /
        LAG(pat_cr)
        OVER (ORDER BY financial_year) * 100,
        2
    ) AS profit_growth_pct

FROM a2b_financials
ORDER BY financial_year;