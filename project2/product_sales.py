import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r"C:\Users\User\DataAnalisysExamples\product_sales.csv")

plt.figure(figsize=(10,6))
plt.hist(df['Sales_Amount'], bins=20, color='blue', alpha=0.7, edgecolor='black')
plt.title('Distribution of Product Sales Amount', fontsize=14)
plt.xlabel('Sales Amount', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(axis='y', alpha=0.75)
plt.show()


plt.figure(figsize=(10,6))
sns.boxplot(x='Product_Category', y='Sales_Amount', data=df, palette='Set2')
plt.title('Boxplot of Sales Amount by Product Category', fontsize=14)
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Sales Amount', fontsize=12)
plt.grid(True)
plt.show()


plt.figure(figsize=(10,6))
df.groupby('Region')['Sales_Amount'].sum().plot(kind='bar', color='green', edgecolor='black')
plt.title('Total Sales Amount by Region', fontsize=14)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Total Sales Amount', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.75)
plt.show()

