import os
from dotenv import load_dotenv
import pandas as pd
from flask import Flask, request, jsonify, Blueprint, render_template
from .trading_functions import HistoricalDataFetcher
from datetime import datetime, date, timedelta
from app.models.cryptos import CryptoPrice, Cryptocurrency
from app import db
from sqlalchemy import and_
from itertools import combinations
import plotly.express as px
import plotly.graph_objs as go

data_fetcher = HistoricalDataFetcher()

crypto_correlation_route = Blueprint('crypto_correlation_map', __name__)

@crypto_correlation_route.route('/crypto_correlation_map', methods=['GET', 'POST'])
def create_correlation_matrix():
    if request.method == 'POST':
        # Convert selected dates to timestamps
        since_date = datetime.strptime(request.form['since_date'], '%Y-%m-%d')
        till_date = datetime.strptime(request.form['till_date'], '%Y-%m-%d')

        # Fetch historical data from the database for all cryptocurrencies
        cryptocurrencies = db.session.query(Cryptocurrency).all()
        correlation_data = {}

        # Create a list of symbol names for all cryptocurrencies
        symbols = [crypto.symbol for crypto in cryptocurrencies]

        for symbol in symbols:
            data = db.session.query(CryptoPrice).join(CryptoPrice.crypto).filter(
                and_(Cryptocurrency.symbol == symbol, CryptoPrice.date >= since_date, CryptoPrice.date <= till_date)
            ).all()

            # Convert the data to a DataFrame
            df = pd.DataFrame([(entry.date, entry.open, entry.high, entry.low, entry.close, entry.volume) for entry in data],
                              columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            df['timestamp'] = pd.to_datetime(df['timestamp'])

            # Calculate returns
            returns = data_fetcher.calculate_returns(df)
            correlation_data[symbol] = returns

        # Calculate correlations between all pairs of cryptocurrencies
        correlation_matrix = pd.DataFrame()
        for symbol1, symbol2 in combinations(symbols, 2):
            corr = correlation_data[symbol1]['return'].corr(correlation_data[symbol2]['return'])
            correlation_matrix.loc[symbol1, symbol2] = corr
            correlation_matrix.loc[symbol2, symbol1] = corr

        # Convert the correlation matrix to a Plotly heatmap
        fig = px.imshow(correlation_matrix, x=symbols, y=symbols)
        fig.update_xaxes(side="top")  # Place the x-axis labels on top
        fig.update_layout(
            title="Crypto Correlation Matrix",
            xaxis_title="Cryptocurrencies",
            yaxis_title="Cryptocurrencies",
            margin=dict(l=0, r=0, b=50, t=50),  # Adjust the margin for better layout
        )

        # Add annotations to display numbers in the middle of the cells
        annotations = []
        for i, symbol1 in enumerate(symbols):
            for j, symbol2 in enumerate(symbols):
                annotations.append(
                    dict(
                        x=i,
                        y=j,
                        text=f'{correlation_matrix.loc[symbol1, symbol2]:.2f}',
                        showarrow=False,
                        font=dict(size=12),
                    )
                )
        fig.update_layout(annotations=annotations)

        # Render the template and pass the Plotly figure to it
        return render_template('crypto_correlation_map.html', correlation_matrix=fig.to_html())
    else:
        today_date = datetime.now()
        since_date = today_date - timedelta(days=600)

        # Fetch historical data from the database for all cryptocurrencies
        cryptocurrencies = db.session.query(Cryptocurrency).all()
        correlation_data = {}

        # Create a list of symbol names for all cryptocurrencies
        symbols = [crypto.symbol for crypto in cryptocurrencies]

        for symbol in symbols:
            data = db.session.query(CryptoPrice).join(CryptoPrice.crypto).filter(
                and_(Cryptocurrency.symbol == symbol, CryptoPrice.date >= since_date, CryptoPrice.date <= today_date)
            ).all()

            # Convert the data to a DataFrame
            df = pd.DataFrame(
                [(entry.date, entry.open, entry.high, entry.low, entry.close, entry.volume) for entry in data],
                columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            df['timestamp'] = pd.to_datetime(df['timestamp'])

            # Calculate returns
            returns = data_fetcher.calculate_returns(df)
            correlation_data[symbol] = returns

        # Calculate correlations between all pairs of cryptocurrencies
        correlation_matrix = pd.DataFrame()
        for symbol1, symbol2 in combinations(symbols, 2):
            corr = correlation_data[symbol1]['return'].corr(correlation_data[symbol2]['return'])
            correlation_matrix.loc[symbol1, symbol2] = corr
            correlation_matrix.loc[symbol2, symbol1] = corr

        # Convert the correlation matrix to a Plotly heatmap
        fig = px.imshow(correlation_matrix, x=symbols, y=symbols)
        fig.update_xaxes(side="top")  # Place the x-axis labels on top
        fig.update_layout(
            title="Crypto Correlation Matrix",
            xaxis_title="Cryptocurrencies",
            yaxis_title="Cryptocurrencies",
            margin=dict(l=0, r=0, b=50, t=50),  # Adjust the margin for better layout
        )

        # Add annotations to display numbers in the middle of the cells
        annotations = []
        for i, symbol1 in enumerate(symbols):
            for j, symbol2 in enumerate(symbols):
                annotations.append(
                    dict(
                        x=i,
                        y=j,
                        text=f'{correlation_matrix.loc[symbol1, symbol2]:.2f}',
                        showarrow=False,
                        font=dict(size=12),
                    )
                )
        fig.update_layout(annotations=annotations)

        # Render the template and pass the Plotly figure to it
        return render_template('crypto_correlation_map.html', correlation_matrix=fig.to_html(),
                               today_date=today_date.strftime('%Y-%m-%d'))