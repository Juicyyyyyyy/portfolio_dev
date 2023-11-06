import os
from dotenv import load_dotenv
import pandas as pd
from flask import Flask, request, jsonify, Blueprint, render_template
from .trading_functions import HistoricalDataFetcher
from datetime import datetime
from app.models.cryptos import CryptoPrice, Cryptocurrency
from app import db
from sqlalchemy import and_
import plotly.graph_objs as go

data_fetcher = HistoricalDataFetcher()

crypto_correlation_route = Blueprint('crypto_correlation_map', __name__)

@crypto_correlation_route.route('/crypto_correlation_map', methods=['GET', 'POST'])
def create_correlation_matrix():
    if request.method == 'POST':
        # Get the form values submitted by the user
        selected_symbols = request.form.getlist('symbols')

        # Convert selected dates to timestamps
        since_date = datetime.strptime(request.form['since_date'], '%Y-%m-%d')
        till_date = datetime.strptime(request.form['till_date'], '%Y-%m-%d')

        # Fetch historical data from the database
        historical_data = {}
        for symbol in selected_symbols:
            # Query the CryptoPrice table for the selected symbol and date range
            data = db.session.query(CryptoPrice).join(CryptoPrice.crypto).filter(
                and_(Cryptocurrency.symbol == symbol, CryptoPrice.date >= since_date, CryptoPrice.date <= till_date)
            ).all()

            # Convert the data to a DataFrame
            df = pd.DataFrame([(entry.date, entry.open, entry.high, entry.low, entry.close, entry.volume) for entry in data],
                              columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            df['timestamp'] = pd.to_datetime(df['timestamp'])

            # Calculate returns
            returns = data_fetcher.calculate_returns(df)
            historical_data[symbol] = returns

        # Calculate correlations
        correlation_data = {}
        for symbol, returns in historical_data.items():
            correlation_matrix = data_fetcher.calculate_correlations([returns])
            correlation_data[symbol] = correlation_matrix

            # Create a correlation matrix plot
            plot_data = []
            for symbol, corr_matrix in correlation_data.items():
                fig = go.Figure(data=go.Heatmap(
                    z=corr_matrix.values,
                    x=corr_matrix.columns,
                    y=corr_matrix.index,
                    colorscale='Viridis',
                ))
                fig.update_layout(
                    title=f'Correlation Matrix for {symbol}',
                    xaxis_title='Cryptocurrencies',
                    yaxis_title='Cryptocurrencies',
                )
                plot_data.append(fig.to_html(full_html=False, include_plotlyjs='cdn'))

            return render_template('crypto_correlation_map.html', plot_data=plot_data,
                                   selected_symbols=selected_symbols,
                                   since_date=since_date, till_date=till_date)
    else:
        cryptocurrencies = db.session.query(Cryptocurrency).all()
        return render_template('crypto_correlation_map.html', cryptocurrencies=cryptocurrencies)