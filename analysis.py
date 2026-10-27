"""Reproduce the sales totals and charts from data_sample_sales.csv using SQLite."""
import csv, sqlite3, pathlib
base = pathlib.Path(__file__).parent
con = sqlite3.connect(':memory:')
con.execute('CREATE TABLE sales (order_id INT, region TEXT, category TEXT, quantity INT, unit_price REAL, sales REAL)')
with open(base / 'data_sample_sales.csv') as f:
    rows = list(csv.DictReader(f))
con.executemany('INSERT INTO sales VALUES (?,?,?,?,?,?)',
                [(r['order_id'], r['region'], r['category'], r['quantity'], r['unit_price'], r['sales']) for r in rows])
print('Total:', con.execute('SELECT COUNT(*), ROUND(SUM(sales),2), ROUND(AVG(sales),2) FROM sales').fetchone())
print('By region:', con.execute('SELECT region, ROUND(SUM(sales),2) FROM sales GROUP BY region ORDER BY SUM(sales) DESC').fetchall())
print('By category:', con.execute('SELECT category, ROUND(SUM(sales),2) FROM sales GROUP BY category ORDER BY SUM(sales) DESC').fetchall())
