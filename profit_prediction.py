import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

file_path = r"C:\Users\User\DataAnalisysExamples\cleaned_financial_data.xlsx"
data = pd.read_excel(file_path)

X = data.drop(columns=["Date", "Profit"])
y = data["Profit"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Splitting the dataset into training and testing...")

model = LinearRegression()
model.fit(X_train, y_train)
print("The model was trained...")

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Model performance:")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")

predictions = pd.DataFrame({"Real Profit": y_test.values, "Predicted Profit": y_pred})

output_file_path = r"C:\Users\User\DataAnalisysExamples\financial_data_predictions.xlsx"
predictions.to_excel(output_file_path, index=False)
print(f"The output file was saved to: {output_file_path}")