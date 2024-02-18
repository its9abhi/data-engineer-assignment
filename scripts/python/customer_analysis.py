import pandas as pd
import sqlite3

# Connect to the SQLite database {Replace it with Database name}
conn = sqlite3.connect('your_database.db')

# Load data into Pandas dataframes using SQL queries
df_orders = pd.read_sql_query("SELECT * FROM Orders", conn)
df_sales = pd.read_sql_query("SELECT * FROM Sales", conn)
df_customers = pd.read_sql_query("SELECT * FROM Customer", conn)
df_items = pd.read_sql_query("SELECT * FROM Items", conn)

# Merge the dataframes
df_merged = pd.merge(df_orders, df_sales, left_on='sales_id', right_on='sales_id', how='left')
df_merged = pd.merge(df_merged, df_customers, left_on='customer_id', right_on='customer_id', how='left')
df_merged = pd.merge(df_merged, df_items, left_on='item_id', right_on='item_id', how='left')

# Filter rows based on age and quantity
df_filtered = df_merged[(df_merged['Age'].between(18, 35)) & (df_merged['quantity'].notnull())]

# Group by and aggregate
df_grouped = df_filtered.groupby(['customer_id', 'Age', 'item_id']).agg({'quantity': 'sum'}).reset_index()

# Filter out rows with Quantity > 0
df_final = df_grouped[df_grouped['quantity'] > 0]

# Select desired columns
df_result = df_final.rename(columns={'customer_id': 'Customer', 'Age': 'Age', 'item_id': 'Item', 'quantity': 'Quantity'})
df_result = df_result[['Customer', 'Age', 'Item', 'Quantity']]

# Store the results to a CSV file with semicolon delimiter
df_result.to_csv('customer_analysis.csv', sep=';', index=False)
