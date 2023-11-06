from datetime import datetime, timedelta
from populate_db import app, db, kill_db, CryptoPrice, Cryptocurrency
from app.tools.crypto_correlation_map import data_fetcher

import ccxt
from datetime import datetime


def fetch_and_store_historical_crypto_data():
    # Initialize the Binance exchange
    binance = ccxt.binance()

    # Define the list of cryptocurrency symbols you want to fetch
    symbols = ["BTC/USDT", "ETH/USDT", "XRP/USDT", "BNB/USDT", "USDC/USDT", "SOL/USDT", "ADA/USDT", "DOGE/USDT", "TRX/USDT", "TON/USDT", "LINK/USDT", "MATIC/USDT", "DOT/USDT", "WBTC/USDT", "DAI/USDT", "LTC/USDT", "SHIB/USDT", "BCH/USDT", "AVAX/USDT", "LEO/USDT", "XLM/USDT", "TUSD/USDT", "OKB/USDT", "ATOM/USDT", "XMR/USDT", "UNI/USDT", "ETC/USDT", "FIL/USDT", "BUSD/USDT", "HBAR/USDT", "ICP/USDT", "LDO/USDT", "CRO/USDT", "APT/USDT", "NEAR/USDT", "VET/USDT", "ARB/USDT", "OP/USDT", "INJ/USDT", "AAVE/USDT", "MKR/USDT", "MNT/USDT", "QNT/USDT", "EGLD/USDT", "GRT/USDT", "IMX/USDT", "RUNE/USDT", "ALGO/USDT", "NEO/USDT", "BSV/USDT", "STX/USDT", "RNDR/USDT", "AXS/USDT", "THETA/USDT", "SAND/USDT", "XTZ/USDT", "MANA/USDT", "EOS/USDT", "FTM/USDT", "XDC/USDT", "USDD/USDT", "SNX/USDT", "FDUSD/USDT", "KAVA/USDT", "BGB/USDT", "CHZ/USDT", "FLOW/USDT", "MINA/USDT", "XEC/USDT", "CFX/USDT", "TWT/USDT", "CAKE/USDT", "APE/USDT", "GALA/USDT", "KCS/USDT", "IOTA/USDT", "CRV/USDT", "RPL/USDT", "XAUt/USDT", "PEPE/USDT", "FXS/USDT", "SUI/USDT", "PAXG/USDT", "ZEC/USDT", "KLAY/USDT", "USDP/USDT", "ROSE/USDT", "ETHDYDX/USDT", "AR/USDT", "BTT/USDT", "GMX/USDT", "CSPR/USDT", "WOO/USDT", "COMP/USDT", "HT/USDT", "RUNE/USDT"]

    # Define the start date (5 years ago from today)
    start_date = datetime.now() - timedelta(days=5*365)

    # Loop through each day
    current_date = datetime.now()
    while current_date > start_date:
        for symbol in symbols:
            try:
                # Fetch OHLCV data for the current day and symbol
                since = int((current_date - timedelta(days=1)).timestamp()) * 1000
                till = int(current_date.timestamp()) * 1000
                ohlcv = binance.fetch_ohlcv(symbol, '1d', since, till)

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
            except:
                continue

            # Store OHLCV data for the current day
            for data in ohlcv:
                price = CryptoPrice(
                    crypto=crypto,
                    date=datetime.utcfromtimestamp(data[0] / 1000).date(),
                    price=data[4],  # Closing price
                    high=data[2],  # High price
                    low=data[3],   # Low price
                    open=data[1],  # Opening price
                    close=data[4],  # Closing price
                    volume=data[5]  # Trading volume
                )
                db.session.add(price)

        # Commit the changes to the database for the current day
        db.session.commit()

        # Move to the previous day
        current_date -= timedelta(days=1)

if __name__ == '__main__':
    with app.app_context():
        fetch_and_store_historical_crypto_data()