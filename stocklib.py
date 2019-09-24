import urllib
import urllib.request
import json
import time
import datetime

class Stock:
    def __init__(self,ticker_input,interval=5):
        self.downloaded_json = self.download_data(ticker_input,interval)
        self.ticker = ticker_input
        self.interval = interval
        self.current_datetime, self.last_updated, self.current_price, self.volume, self.history = self.parse_data(self.downloaded_json,interval)

    def download_data(self, symbol, interval_min=5):
        """Function that downloads stock data  
        Argument: stock trading symbol (str)
        Argument: trading interval in minutes (str), defaults to 5 min.  Value must be 1, 5, 15, 30, 60 per alphvantage api
        Returns a json object """

        apikey = "5704M4LMCEJ4DP91"
        url = ( 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY'
        f'&symbol={symbol}&interval={interval_min}min&apikey={apikey}')
        text = urllib.request.urlopen(url).read()  
        return json.loads(text.decode('utf-8'))

    def parse_data(self, data_json, time_series_int=5):
        """Function that parses json for a stock ticker
        Argument: json object to parse (json)
        Argument: time series interval (str), defaults to 5 min
        Return values: current time (time), date of trading day (str), most recent closing price, most recent volume, history of prices for the day
        """
        
        last_updated_datetime = data_json["Meta Data"]["3. Last Refreshed"]
        current_time = time.ctime()
        close_prices = []
        
        for date in data_json[f'Time Series ({time_series_int}min)']:

            if date[0:11] == last_updated_datetime[0:11]:
                close_prices.append(data_json[f'Time Series ({time_series_int}min)'][date]['4. close'])
        
        most_recent_close = data_json[f'Time Series ({time_series_int}min)'][last_updated_datetime]['4. close']
        most_recent_volume = data_json[f'Time Series ({time_series_int}min)'][last_updated_datetime]['5. volume']
        
        return current_time, last_updated_datetime, most_recent_close, most_recent_volume, close_prices

    def refresh(self):
        """Function that downloads the latest data for an existing Stock object 
        Arguments: None
        Return value: None
        """
        self.current_datetime, self.last_updated, self.current_price, self.volume, self.history = self.parse_data(self.downloaded_json,self.interval)

if __name__ == '__main__':
    msft = Stock('FDS',15)
    print(msft.ticker)
    print(msft.current_price)
    print(msft.volume)
    print(msft.last_updated)
    print(msft.history)
    
    msft.refresh()
    print(msft.ticker)
    print(msft.current_price)
    print(msft.volume)
    print(msft.last_updated)
    print(msft.history)



        