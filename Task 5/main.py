import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


conn = sqlite3.connect("Chinook_Sqlite.sqlite")

# 1. Top-Selling Products
query_top_products = """
SELECT t.Name AS Product, SUM(il.Quantity) AS Total_Units_Sold
FROM InvoiceLine il
JOIN Track t ON il.TrackId = t.TrackId
GROUP BY t.Name
ORDER BY Total_Units_Sold DESC
LIMIT 10;
"""
top_products = pd.read_sql_query(query_top_products, conn)
print("\nTop-Selling Products:\n", top_products)

# 2. Revenue Per Region
query_revenue_region = """
SELECT c.Country, ROUND(SUM(il.Quantity * il.UnitPrice), 2) AS Revenue
FROM InvoiceLine il
JOIN Invoice i ON il.InvoiceId = i.InvoiceId
JOIN Customer c ON i.CustomerId = c.CustomerId
GROUP BY c.Country
ORDER BY Revenue DESC;
"""
revenue_region = pd.read_sql_query(query_revenue_region, conn)
print("\nRevenue Per Region:\n", revenue_region)

# 3. Monthly Performance
query_monthly_performance = """
SELECT strftime('%Y-%m', i.InvoiceDate) AS Month,
       ROUND(SUM(il.Quantity * il.UnitPrice), 2) AS Monthly_Revenue
FROM InvoiceLine il
JOIN Invoice i ON il.InvoiceId = i.InvoiceId
GROUP BY Month
ORDER BY Month;
"""
monthly_performance = pd.read_sql_query(query_monthly_performance, conn)
print("\nMonthly Performance:\n", monthly_performance)


# 4. Top Artist by Revenue
query_top_artist = """
SELECT ar.Name AS Artist, ROUND(SUM(il.Quantity * il.UnitPrice), 2) AS Revenue
FROM InvoiceLine il
JOIN Track t ON il.TrackId = t.TrackId
JOIN Album al ON t.AlbumId = al.AlbumId
JOIN Artist ar ON al.ArtistId = ar.ArtistId
GROUP BY ar.Name
ORDER BY Revenue DESC
LIMIT 5;
"""
top_artist = pd.read_sql_query(query_top_artist, conn)
print("\nTop Artists by Revenue:\n", top_artist)

# 5. Ranking with Window Function 
query_rank_products = """
SELECT t.Name AS Product,
SUM(il.Quantity) AS Total_Units_Sold,
RANK() OVER (ORDER BY SUM(il.Quantity) DESC) AS RankPosition
FROM InvoiceLine il
JOIN Track t ON il.TrackId = t.TrackId
GROUP BY t.Name
ORDER BY RankPosition
LIMIT 10;
"""
ranked_products = pd.read_sql_query(query_rank_products, conn)
print("\nTop-Selling Products with Rank:\n", ranked_products)

conn.close()

plt.figure(figsize=(10,6))
plt.barh(top_products['Product'], top_products['Total_Units_Sold'], color='skyblue')
plt.xlabel("Units Sold")
plt.title("Top 10 Selling Products")
plt.gca().invert_yaxis()  
plt.show()
