import pandas as pd
import matplotlib.pyplot as plt

# Read the file
data = pd.read_csv("C:\\Users\\User\\DataAnalisysExamples\\OnlineSalesData.csv", sep=',', header=0)
# Print top 5 rows
print(data.head())
# Print name of the columns
print(data.columns)

# General descriptive statistics for numerical data
print(data.describe())

# Filter products with sales greater than 500
filtered_sales = data[data['Sales'] > 500]
print(filtered_sales)

# Filter products from category Books
filtered_category_books = data[data['Category'] == 'Books']
print(filtered_category_books)

# Grouping by category and summing sales
sales_by_category = data.groupby('Category')['Sales'].sum()
print(sales_by_category)


# Create a chart with sales by category
sales_by_category.plot(kind='bar', title='Vânzările pe categorii')
plt.xlabel('Categorie')
plt.ylabel('Vânzări totale')
plt.show()

# Save filtered data to a new CSV file
filtered_sales.to_csv('C:\\Users\\User\\DataAnalisysExamples\\filtered_sales.csv', sep=';', index=False)