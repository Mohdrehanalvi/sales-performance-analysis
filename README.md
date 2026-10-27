# Sales Performance Analysis

**Question:** Which regions and product categories drive sales, and where should a team focus next?

**Data:** Sample retail data created for this project (500 orders, `data_sample_sales.csv`). This is demonstration data, not real company data.

## Tools
SQL (SQLite), Python (pandas-style analysis with sqlite3), matplotlib

## Findings (computed from the sample data)
- 500 orders, total sales $822,579.27, average order $1,645.16
- Top region: Central, $233,723.49
- Top category: Electronics, $411,050.23, followed by Furniture at $349,819.74
- Office Supplies had 164 orders but only $61,709.30 in sales, so it drives order volume, not revenue

## Sales by region
![Sales by region](charts/sales_by_region.png)

## Sales by category
![Sales by category](charts/sales_by_category.png)

## What this means
- Focus growth effort on Central and on Electronics, where revenue is concentrated.
- Review Office Supplies pricing or bundling, since it moves units without moving revenue much.
- These are sample-data findings, used to show the analysis method, not a real business recommendation.

## Files
- `data_sample_sales.csv` — sample order data
- `sql/queries.sql` — the SQL used for the regional and category summaries
- `analysis.py` — the Python script that reproduces the totals and charts
