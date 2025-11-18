import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\User\DataAnalisysExamples\Stock_Price_Data.csv")

data['Date'] = pd.to_datetime(data['Date'])
data['Days'] = (data['Date'] - data['Date'].min()).dt.days

X = data[['Days']]
y = data['Stock_Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model= LinearRegression()
model.fit(X_train, y_train) 

y_pred = model.predict(X_test)

# visuzalization

plt.scatter(X_test, y_test, color='blue', label='True')
plt.plot(X_test, y_pred, color='red', label='Previzions')
plt.title('Prediction of action price using linear regresion model')
plt.xlabel('Days')
plt.ylabel('Action Price')
plt.legend()
plt.show()

