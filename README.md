# Timeseries anomaly detection

This repo takes timeseries data in csv format as input. Facebook's prophet algorithm at its core is comprised of trend, weekly seasonality, yearly seasonality and holidays. The csv files are examples and `prophet-test.py` is the python code that trains the model and plots the graph. This code works in MacOS and Linux operating systems. 


# CSV files

The csv data files have 2 columns namely ds and y. The first column ds is the timestamp of the timeseries data and second column y is the numerical value.

## Pre-requisites
Install python version 3.8.3


Install conda from https://docs.anaconda.com/anaconda/install/ and add `/home/ubuntu/anaconda3/condabin` to PATH environment variable


Run the requirements.txt
`pip install -r requirements.txt`

If running in Linux then install Mobaxterm.

## Prophet-test.py

After importing pandas and plotly graph libraries, the dataframe is initialized with the CSV file.

	`df = pd.read_csv('request_duration_seconds_count.csv')`

The prophet object is then initialized with the dataframe by calling the fit method

	`m.fit(df)`

Predictions are then made for a period (defined as a number of days)

`future = m.make_future_dataframe(periods=3)`

The forecast is then plotted in a graph by calling the plot method and passing the forecast dataframe.

`m.plot(forecast)`

Forecast components trend, weekly and yearly seasonality are then displayed 

`fig2 = m.plot_components(forecast)`


## Run the python file (Run from Mobaxterm if executing on Linux)

`python prophet-test.py`

This will display the graphs for the example_wp_log_peyton_manning.csv. This csv contains number of visits to Peyton Manning's wiki page by scraping the  Wikipediatrend package in R. It predicts the trends in the visits to the Peyton Manning wiki page for 365 days beyond the last timestamp (2016-01-20) in the csv file. The graph also shows the seasonality.

```