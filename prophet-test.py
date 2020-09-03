# Python
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from fbprophet import Prophet
df = pd.read_csv('example_wp_log_peyton_manning.csv')
df.head()
m = Prophet()
m.fit(df)
future = m.make_future_dataframe(periods=365)
future.tail()
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
fig1 = m.plot(forecast)
fig2 = m.plot_components(forecast)
from fbprophet.plot import plot_plotly, plot_components_plotly
plot_plotly(m, forecast)
plot_components_plotly(m, forecast)
plt.show()
