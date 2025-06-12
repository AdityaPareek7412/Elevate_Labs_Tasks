# TASK 7: Get Basic Sales Summary from SQLite

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create a SQLite database and sales table with sample data
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create table (only run once or check if exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Optional: Insert sample data (skip if already inserted)
sample_data = [
    ('Apple', 10, 1.2),
    ('Banana', 15, 0.5),
    ('Orange', 8, 0.8),
    ('Apple', 5, 1.2),
    ('Banana', 10, 0.5),
    ('Orange', 12, 0.8),
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
conn.commit()

# Step 2: Run SQL query to get summary
query = """
SELECT 
    product,
    SUM(quantity) AS total_quantity,
    ROUND(SUM(quantity * price), 2) AS revenue
FROM sales
GROUP BY product
"""
df = pd.read_sql_query(query, conn)

# Step 3: Display the summary
print("=== Sales Summary ===")
print(df)

# Step 4: Plot a bar chart of revenue by product
plt.figure(figsize=(8,5))
df.plot(kind='bar', x='product', y='revenue', color='skyblue', legend=False)
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Optional: Save the chart
plt.savefig("sales_chart.png")

# Show plot
plt.show()

# Close the connection
conn.close()
