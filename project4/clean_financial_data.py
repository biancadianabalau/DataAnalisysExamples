import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from scipy import stats

file_path = r"C:\Users\User\DataAnalisysExamples\financial_data.xlsx"
data = pd.read_excel(file_path)

for column in ["Revenue", "Expenses", "Profit"]:
    data[column] = data[column].fillna(data[column].median()) # Fill missing values with median

for column in ["Revenue", "Expenses", "Profit"]:
    Q1 = data[column].quantile(0.25) # indentify outliers using IQR method
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    data.loc[data[column] < lower_bound, column] = lower_bound #replace outliers with bounds
    data.loc[data[column] > upper_bound, column] = upper_bound

scaler = StandardScaler()

data[["Revenue", "Expenses", "Profit"]] = scaler.fit_transform(data[["Revenue", "Expenses", "Profit"]]) # Normalize numerical columns

encoder = OneHotEncoder(sparse_output=False)
encoded_regions = encoder.fit_transform(data[["Region"]])
encoded_region_df = pd.DataFrame(encoded_regions, columns=encoder.get_feature_names_out(["Region"]))
data = pd.concat([data, encoded_region_df], axis=1).drop("Region", axis=1) 

output_path = r"C:\Users\User\DataAnalisysExamples\cleaned_financial_data.xlsx"
data.to_excel(output_path, index=False)
print("Data cleaning complete. Cleaned data saved to:", output_path)



