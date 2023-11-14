from populate_db import app, db, CryptoPrice, Cryptocurrency
import ccxt
from datetime import datetime, timedelta

def fetch_ohlcv_data(symbol, since, till):
    binance = ccxt.binance()
    return binance.fetch_ohlcv(symbol, '1d', since, till)

def fetch_and_store_historical_crypto_data(symbol, start_date):
    with app.app_context():
        current_date = datetime.now()
        while current_date > start_date:
            try:
                # Calculate the time range for the current day
                since = int((current_date - timedelta(days=1)).timestamp()) * 1000
                till = int(current_date.timestamp()) * 1000

                # Fetch OHLCV data
                ohlcv = fetch_ohlcv_data(symbol, since, till)
                print(ohlcv)
                # Check if the cryptocurrency exists in the database
                crypto = Cryptocurrency.query.filter_by(symbol=symbol).first()

                # If it doesn't exist, create a new record
                if crypto is None:
                    crypto = Cryptocurrency(
                        name=symbol,  # You may want to fetch the actual name from an external source
                        symbol=symbol,
                        market_cap=None,  # You may update this information later
                        volume=None,  # You may update this information later
                        logo_url='[URL to Crypto Logo]'
                    )
                    db.session.add(crypto)

                # Store OHLCV data for the current day

                price = CryptoPrice(
                    crypto=crypto,
                    date=datetime.utcfromtimestamp(ohlcv[0][0] / 1000).date(),
                    price=ohlcv[0][4],  # Closing price
                    high=ohlcv[0][2],  # High price
                    low=ohlcv[0][3],   # Low price
                    open=ohlcv[0][1],  # Opening price
                    close=ohlcv[0][4],  # Closing price
                    volume=ohlcv[0][5]  # Trading volume
                )
                db.session.add(price)

                # Commit the changes to the database for the current day
                db.session.commit()

            except Exception as e:
                print(f"Error for {symbol} on {current_date}: {e}")

            # Move to the previous day
            current_date -= timedelta(days=1)

def main():
    symbols = ["BTC/USDT", "ETH/USDT", "XRP/USDT", "BNB/USDT", "SOL/USDT", "ADA/USDT", "DOGE/USDT"]

    start_date = datetime(2023, 11, 1)

    for symbol in symbols:
        fetch_and_store_historical_crypto_data(symbol, start_date)

if __name__ == '__main__':
    main()
