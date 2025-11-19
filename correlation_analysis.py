import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = r"C:\Users\User\DataAnalisysExamples\data_correlation.csv"
df = pd.read_csv(file_path)

correlation_matrix = df.corr(method='pearson')
print("Correlatoin matrix:")
print(correlation_matrix)

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("correlation matrix - Heat Map")
plt.show()