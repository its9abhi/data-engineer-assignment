import pandas as pd
import sqlite3

# Connect to the SQLite3 database {Replace it with Database name}
conn = sqlite3.connect('your_database_file.db')

# Extract total quantities of each item bought per customer aged 18-35
query = """
 	SELECT s.customer_id AS Customer, c.age AS Age, s.item_id AS Item, SUM(s.quantity) AS Quantity
    FROM Orders AS o
	LEFT JOIN Sales AS s
	ON o.sales_id = s.sales_id
    LEFT JOIN Customers AS c 
	ON s.customer_id = c.customer_id
	LEFT JOIN Items AS i
	ON o.item_id = i.item_id
    WHERE c.age BETWEEN 18 AND 35 AND s.quantity IS NOT NULL
    GROUP BY s.customer_id, c.age, s.item_id
    HAVING SUM(s.quantity) > 0;
"""

# Execute the query and fetch the results into a DataFrame
df = pd.read_sql_query(query, conn)

# Store the results to a CSV file with semicolon delimiter
df.to_csv('customer_analysis.csv', sep=';', index=False)
