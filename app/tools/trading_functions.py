import ccxt
import pandas as pd

class HistoricalDataFetcher:
    def __init__(self):
        self.exchange = ccxt.binance({
            'enableRateLimit': True,  # this option is required to minimize the risk of being banned by the exchange
        })

    def fetch_historical_data(self, symbol, timeframe, since, till):
        # Fetch OHLCV (Open, High, Low, Close, Volume) data
        ohlcv = self.exchange.fetch_ohlcv(symbol, timeframe, since, till)

        # Convert to DataFrame
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

        return df

    def calculate_returns(self, df):
        # Ensure the data is sorted by timestamp
        df = df.sort_values('timestamp')

        # Calculate the percentage change in closing price
        df['return'] = df['close'].pct_change()

        # Drop the rows with missing values (this will be the first row)
        df = df.dropna()

        return df

    def calculate_correlations(self, returns):
        # Merge all return series into one DataFrame, using timestamp as index
        merged_returns = pd.concat(returns, axis=1)

        # Calculate the correlation matrix
        corr_matrix = merged_returns.corr()

        return corr_matrix
