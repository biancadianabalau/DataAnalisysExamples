import pandas as pd
data = pd.read_csv(r"C:\Users\User\DataAnalisysExamples\OnlineSalesData.csv", sep=',')

print(data.head())
print(data.columns)

print(data.describe())

filtered_sales = data[data['Sales'] > 300]
print(filtered_sales)
filtered_category_b = data[data['Category'] == 'Books']
print(filtered_category_b)

sales_by_category = data.groupby('Category')['Sales'].sum()
print(sales_by_category)

import matplotlib.pyplot as plt
sales_by_category.plot(kind='bar', title='Category Sales')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.show()

filtered_sales.to_csv(r"C:\Users\User\DataAnalisysExamples\filtered_sales.csv", sep=';', index=False)

