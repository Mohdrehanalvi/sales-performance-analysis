-- Total orders, total sales, average order value
SELECT COUNT(*) AS orders, ROUND(SUM(sales), 2) AS total_sales, ROUND(AVG(sales), 2) AS avg_order
FROM sales;

-- Sales by region, highest first
SELECT region, COUNT(*) AS orders, ROUND(SUM(sales), 2) AS total_sales
FROM sales
GROUP BY region
ORDER BY total_sales DESC;

-- Sales by category, highest first
SELECT category, COUNT(*) AS orders, ROUND(SUM(sales), 2) AS total_sales, ROUND(AVG(quantity), 1) AS avg_quantity
FROM sales
GROUP BY category
ORDER BY total_sales DESC;
