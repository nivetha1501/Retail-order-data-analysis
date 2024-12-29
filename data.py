
import streamlit as st

import mysql.connector

import pandas as pd

import re

 

 

# Function to establish database connection
mydb = mysql.connector.connect(

 host="localhost",

 user="root",
 
 password="nivi"
 )
mycursor = mydb.cursor(dictionary=True)
st.success("Connected to the database successfully!")

        
st.title('RETAIL ORDERS')
st.write('MY PROJECT')
    
mycursor.execute('use retail_order')


if st.button("query 1"):
    st.markdown("Find top 10 highest revenue generating products:")
    mycursor.execute('''SELECT product_id, SUM(sale_price) AS revenue
FROM retail_order2
GROUP BY Product_id
order BY revenue DESC
LIMIT 10;
''')
    st.table(mycursor)



if st.button("query 2"):
    st.markdown("Find the top 5 cities with the highest profit margins:")
    mycursor.execute('''SELECT city,
    MAX(product_id) AS product_id,  
    SUM(sale_price - cost_price) AS total_profit
FROM retail_order2
INNER JOIN retail_order1 ON retail_order2.order_id = retail_order1.order_id
GROUP BY city
ORDER BY total_profit DESC
LIMIT 5;''')
    st.table(mycursor)

if st.button("query 3"):
    st.markdown("Calculate the total discount given for each category:")
    mycursor.execute('''SELECT retail_order2.sub_category, 
    SUM(retail_order2.discount) AS total_discount
FROM retail_order1 
RIGHT JOIN retail_order2 ON retail_order1.category = retail_order2.order_id
GROUP BY retail_order2.sub_category
ORDER BY retail_order2.sub_category
LIMIT 0, 1000;''')
    st.table(mycursor)



if st.button("query 4"):
    st.markdown("Find the average sale price per product category:")
    mycursor.execute('''
SELECT retail_order2.sub_category, 
    AVG(retail_order2.sale_price) AS average_sale_price
FROM retail_order1 
RIGHT JOIN retail_order2 ON retail_order1.category = retail_order2.order_id
GROUP BY retail_order2.sub_category
ORDER BY retail_order2.sub_category
LIMIT 0, 1000;''')
    st.table(mycursor)

if st.button("query 5"):
    st.markdown("Find the region with the highest average sale price:")
    mycursor.execute('''SELECT retail_order1.region, 
    AVG(retail_order2.sale_price) AS average_sale_price
FROM retail_order2
JOIN retail_order1 ON retail_order2.order_id = retail_order1.order_id
GROUP BY retail_order1.region
ORDER BY average_sale_price DESC
LIMIT 1;''')
    st.table(mycursor)

if st.button("query 6"):
    st.markdown("Identify the top 3 segments with the highest quantity of orders:")
    mycursor.execute('''SELECT retail_order1.category, 
    SUM(retail_order2.sale_price - retail_order2.cost_price) AS total_profit
FROM retail_order2
JOIN retail_order1 ON retail_order2.order_id = retail_order1.order_id
GROUP BY retail_order1.category
ORDER BY total_profit DESC
LIMIT 0, 1000;''')
    st.table(mycursor)


if st.button("query 7"):
    st.markdown("Identify the top 3 segments with the highest quantity of orders:")
    mycursor.execute('''SELECT retail_order1.segment, 
    SUM(retail_order2.quantity) AS total_quantity
FROM retail_order2 retail_order2
JOIN retail_order1 retail_order1 ON retail_order2.order_id = retail_order1.order_id
GROUP BY retail_order1.segment
ORDER BY total_quantity DESC
LIMIT 3;''')
    st.table(mycursor)

if st.button("query 8"):
    st.markdown("Determine the average discount percentage given per region:")
    mycursor.execute('''
SELECT retail_order1.region, 
    AVG(retail_order2.discount_percent) AS average_discount_percentage
FROM retail_order2 retail_order2
JOIN retail_order1 retail_order1 ON retail_order2.order_id = retail_order1.order_id
GROUP BY retail_order1.region
ORDER BY average_discount_percentage DESC;''')
    st.table(mycursor)

if st.button("query 9"):
    st.markdown("Find the product category with the highest total profit:")
    mycursor.execute('''SELECT category, 
    SUM((sale_price - cost_price) * retail_order2.quantity) AS total_profit
FROM retail_order2
JOIN retail_order1 ON retail_order2.order_id = retail_order1.order_id
GROUP BY retail_order1.category
ORDER BY total_profit 
LIMIT 1;''')
    st.table(mycursor)

if st.button("query 10"):
    st.markdown("Calculate the total revenue generated per year:")
    mycursor.execute('''
SELECT YEAR(retail_order1.order_date) AS year, 
       SUM(retail_order2.sale_price * retail_order2.quantity) AS total_revenue
FROM retail_order1 
JOIN retail_order2  ON retail_order1.order_id = retail_order2.order_id
GROUP BY YEAR(retail_order1.order_date)
ORDER BY year;''')
    st.table(mycursor)


st.header('MY QUERIES')

if st.button("query 11"):
    st.markdown("Count of Total Orders retail_order1:")
    mycursor.execute('''SELECT COUNT(order_id) AS total_orders 
FROM retail_order1;''')
    st.table(mycursor)

if st.button("query 12"):
    st.markdown("Count of Total Orders retail_order2:")
    mycursor.execute('''SELECT COUNT(order_id) AS total_orders 
FROM retail_order2;''')
    st.table(mycursor)

if st.button("query 13"):
    st.markdown("determine the most popular ship mode used for orders:")
    mycursor.execute('''SELECT 
    ship_mode, 
    COUNT(*) AS order_count
FROM retail_order1
GROUP BY ship_mode
ORDER BY order_count DESC
LIMIT 1;''')
    st.table(mycursor)

if st.button("query 14"):
    st.markdown("list the state with the highest number of orders:")
    mycursor.execute('''SELECT state, COUNT(*) AS order_count
FROM retail_order1
GROUP BY state
ORDER BY order_count DESC
LIMIT 1;''')
    st.table(mycursor)

if st.button("query 15"):
    st.markdown("Total Revenue for Each Product:")
    mycursor.execute('''
SELECT product_id, SUM(sale_price * quantity) AS total_revenue
FROM retail_order2
GROUP BY product_id;''')
    st.table(mycursor)

if st.button("query 16"):
    st.markdown("Find the Product with the Highest Discount Given:")
    mycursor.execute('''SELECT product_id, MAX(discount_percent) AS highest_discount
FROM retail_order2
GROUP BY product_id;''')
    st.table(mycursor)

if st.button("query 17"):
    st.markdown("Total Discount Given by Product:")
    mycursor.execute('''SELECT product_id, SUM(discount) AS total_discount
FROM retail_order2
GROUP BY product_id;''')
    st.table(mycursor)

if st.button("query 18"):
    st.markdown("Find the Average profit by Product:")
    mycursor.execute('''SELECT product_id, AVG(profit) AS avg_profit
FROM retail_order2
GROUP BY product_id;''')
    st.table(mycursor)

if st.button("query 19"):
    st.markdown("Top 5 Cities by Quantity Sold:")
    mycursor.execute('''SELECT retail_order1.city, 
       SUM(retail_order2.quantity) AS total_quantity_sold
FROM retail_order2 retail_order2
JOIN retail_order1 retail_order1 ON retail_order2.order_id = retail_order1.order_id  
GROUP BY retail_order1.city
ORDER BY total_quantity_sold DESC
LIMIT 5;''')
    st.table(mycursor)

if st.button("query 20"):
    st.markdown("Find the total profit per segment:")
    mycursor.execute('''
SELECT retail_order1.segment, 
    SUM(retail_order2.sale_price - retail_order2.cost_price) AS total_profit
FROM retail_order2
JOIN retail_order1 ON retail_order2.order_id = retail_order1.order_id
GROUP BY retail_order1.segment
ORDER BY total_profit DESC
LIMIT 0, 1000;''')
    st.table(mycursor)

if st.button("query 21"):
    st.markdown("Top 3 Products by Discount Given:")
    mycursor.execute('''SELECT product_id, SUM(discount) AS total_discount
FROM retail_order2
GROUP BY product_id
ORDER BY total_discount DESC
LIMIT 3;''')
    st.table(mycursor)