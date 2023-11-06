import openai
from multiprocessing import Pool
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, Blueprint, render_template
from .trading_functions import HistoricalDataFetcher

data_fetcher = HistoricalDataFetcher()

crypto_correlation_route = Blueprint('crypto_correlation_map', __name__)

@crypto_correlation_route.route('/crypto_correlation_map', methods=['GET', 'POST'])
def create_correlation_map():
    if request.method == 'POST':
        # Get the form values submitted by the user
        selected_symbols = request.form.getlist('symbols')
        timeframe = request.form['timeframe']
        since_timestamp = int(request.form['since_timestamp'])
        till_timestamp = int(request.form['till_timestamp'])

        # Fetch historical data for the selected symbols
        historical_data = {}
        for symbol in selected_symbols:
            df = data_fetcher.fetch_historical_data(symbol, timeframe, since_timestamp, till_timestamp)
            returns = data_fetcher.calculate_returns(df)
            historical_data[symbol] = returns

        # Calculate correlations
        correlation_data = {}
        for symbol, returns in historical_data.items():
            correlation_matrix = data_fetcher.calculate_correlations(returns)
            correlation_data[symbol] = correlation_matrix

        # Pass the correlation data and form parameters to the template
        return render_template('crypto_correlation_map.html', correlation_data=correlation_data,
                               selected_symbols=selected_symbols, timeframe=timeframe,
                               since_timestamp=since_timestamp, till_timestamp=till_timestamp)
    else:
        # Render the initial form with default parameters
        return render_template('crypto_correlation_map.html')
