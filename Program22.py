# Read sales data from CSV and plot bar chart

import pandas as pd
import matplotlib.pyplot as plt

# Create sample CSV file
data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Headphones", "Camera"],
    "Sales": [50000, 70000, 30000, 20000, 40000]
}

df = pd.DataFrame(data)
df.to_csv("sales.csv", index=False)

# Read CSV file
df = pd.read_csv("sales.csv")

print("Sales Data:\n", df)
# Output:
#       Product  Sales
# 0      Laptop  50000
# 1      Mobile  70000
# 2      Tablet  30000
# 3  Headphones  20000
# 4      Camera  40000

# Plot bar chart
plt.bar(df["Product"], df["Sales"])

# Add title and labels
plt.title("Product-wise Sales")     # Output: Title shown on graph
plt.xlabel("Products")             # Output: X-axis labeled Products
plt.ylabel("Sales (₹)")            # Output: Y-axis labeled Sales

# Show plot
plt.show()                         # Output: Bar chart displayed