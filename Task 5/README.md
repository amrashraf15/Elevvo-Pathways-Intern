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
## 📝 Example SQL Queries

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
