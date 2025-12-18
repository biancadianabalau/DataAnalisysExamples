import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

file_path = r"C:\Users\User\DataAnalisysExamples\sales_data_clustering.csv"
data = pd.read_csv(file_path)

data_clustering = data[['Price', 'Sales', 'Discount']]

scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_clustering)

kmeans = KMeans(n_clusters=4, random_state=42)
data['Cluster'] = kmeans.fit_predict(data_scaled)


output_file_path = r'C:\Users\User\DataAnalisysExamples\sales_data_clustering_results.csv'
data.to_csv(output_file_path, index=False)
print(f"The clustered data was saved in the file {output_file_path}")

pca = PCA(n_components=2)
data_pca = pca.fit_transform(data_scaled)

plt.figure(figsize=(10, 6))
scatter = plt.scatter(data_pca[:, 0], data_pca[:, 1], c=data['Cluster'], cmap='viridis', alpha=0.7)
plt.colorbar(scatter, label="Cluster")
plt.xlabel('Principal Component 1')
plt.ylabel('Second Component 2')
plt.title('View Clusters Using PCA')
plt.show()

output_file_path = r'C:\Users\User\DataAnalisysExamples\sales_data_clustered_results.csv'
output_data = pd.concat([data[data['Cluster'] == i]['ID_Produs'].reset_index(drop=True) for i in sorted(data['Cluster'].unique())], axis=1)
output_data.columns = [f'Cluster_{i + 1}' for i in range(len(output_data.columns))]
output_data.to_csv(output_file_path, index=False)
print(f"The clustered data was saved in the file {output_file_path}")
