import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA

file_path = r"C:\Users\User\DataAnalisysExamples\data_series.csv"

data = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')

print(data.head())

data.plot()
plt.title('Time Series View')
plt.show()

result = seasonal_decompose(data['Sales'], model='additive')
result.plot()
plt.show()

model = ARIMA(data['Sales'], order=(1,1,1))
result = model.fit()

plt.figure(figsize=(10, 6))
plt.plot(data['Sales'], label='Original')
plt.plot(result.predict(start=pd.to_datetime('2023-01-01'),
end=pd.to_datetime('2023-12-31'),
dynamic=False),
label='Forecast')
plt.legend()
plt.show()
