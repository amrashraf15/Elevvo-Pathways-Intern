# 📊 Task 5: SQL-Based Analysis of Product Sales

## 📌 Task Description
In this task, we use the **Chinook Database** (available on Kaggle) to analyze product sales through SQL queries.  
The objective is to extract **business insights** from relational data by answering key questions such as:
- What are the **top-selling products**?
- What is the **revenue per region**?
- How is the **monthly performance** trending over time?

This analysis demonstrates how to combine **raw sales and product data** using SQL joins and aggregations.

---
## 🛠️ Tools & Libraries

This project uses the following major technologies:

- ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)  
- ![BigQuery](https://img.shields.io/badge/BigQuery-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)  

---
## 🎯 Covered Topics
- Writing **SQL queries**  
- Using **JOINs** across multiple tables  
- Performing **aggregations** (`SUM`, `COUNT`, `GROUP BY`)  
- Applying **business logic** to raw sales data  
- Bonus: Using **Window Functions** (`ROW_NUMBER`, `RANK`)  
---
<img width="1045" height="706" alt="Image" src="https://github.com/user-attachments/assets/11ee41e4-2407-449c-800e-c604f9a8e5ff" />
## 📝 SQL Queries

### 1. Top-Selling Products
```sql
SELECT 
    t.Name AS Product, 
    SUM(il.Quantity) AS Total_Units_Sold
FROM InvoiceLine il
JOIN Track t ON il.TrackId = t.TrackId
GROUP BY t.Name
ORDER BY Total_Units_Sold DESC
LIMIT 10;
```
### 2. Revenue Per Country
 ```sql
SELECT 
    i.BillingCountry AS Country,
    SUM(i.Total) AS Total_Revenue
FROM invoice i
GROUP BY i.BillingCountry
ORDER BY Total_Revenue DESC;
```
### 3. Monthly Sales Performance
 ```sql
SELECT 
    DATE_FORMAT(i.InvoiceDate, '%Y-%m') AS Month,
    SUM(i.Total) AS Monthly_Revenue
FROM invoice i
GROUP BY Month
ORDER BY Month;
```
### 4. Best 5 Customers
 ```sql
SELECT 
    c.CustomerId,
    CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName,
    SUM(i.Total) AS Total_Spending
FROM customer c
JOIN invoice i ON c.CustomerId = i.CustomerId
GROUP BY c.CustomerId, CustomerName
ORDER BY Total_Spending DESC
LIMIT 5;
```
### 5. Top 5 Genres
 ```sql
SELECT 
    g.Name AS Genre,
    SUM(il.Quantity) AS Total_Units_Sold
FROM InvoiceLine il
JOIN Track t ON il.TrackId = t.TrackId
JOIN Genre g ON t.GenreId = g.GenreId
GROUP BY g.Name
ORDER BY Total_Units_Sold DESC
LIMIT 5;
```
### 6. Top 10 Albums By Revenue
 ```sql
SELECT 
    a.Title AS Album,
    ar.Name AS Artist,
    SUM(il.UnitPrice * il.Quantity) AS Album_Revenue
FROM InvoiceLine il
JOIN Track t ON il.TrackId = t.TrackId
JOIN Album a ON t.AlbumId = a.AlbumId
JOIN Artist ar ON a.ArtistId = ar.ArtistId
GROUP BY a.AlbumId, a.Title, ar.Name
ORDER BY Album_Revenue DESC
LIMIT 10;
```
### 7. Top-Earning Tracks Ranked Within Each Genre
 ```sql
SELECT 
    g.Name AS Genre,
    t.Name AS Track,
    SUM(il.UnitPrice * il.Quantity) AS Revenue,
    RANK() OVER (PARTITION BY g.GenreId ORDER BY SUM(il.UnitPrice * il.Quantity) DESC) AS Rank_in_Genre
FROM InvoiceLine il
JOIN Track t ON il.TrackId = t.TrackId
JOIN Genre g ON t.GenreId = g.GenreId
GROUP BY g.GenreId, g.Name, t.TrackId, t.Name
ORDER BY g.Name, Rank_in_Genre;
```
