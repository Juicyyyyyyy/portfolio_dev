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
import asyncio


data_fetcher = HistoricalDataFetcher()

crypto_correlation_route = Blueprint('crypto_correlation_map', __name__)

async def fetch_crypto_data_async(since_date, till_date):
    cryptocurrencies = db.session.query(Cryptocurrency).all()
    correlation_data = {}
    symbols = [crypto.symbol for crypto in cryptocurrencies]

    tasks = []
    for symbol in symbols:
        task = asyncio.ensure_future(fetch_and_process_data(symbol, since_date, till_date, correlation_data))
        tasks.append(task)

    await asyncio.gather(*tasks)
    return symbols, correlation_data

async def fetch_and_process_data(symbol, since_date, till_date, correlation_data):
    data = db.session.query(CryptoPrice).join(CryptoPrice.crypto).filter(
        and_(Cryptocurrency.symbol == symbol, CryptoPrice.date >= since_date, CryptoPrice.date <= till_date)
    ).all()

    df = pd.DataFrame([(entry.date, entry.close) for entry in data], columns=['timestamp', 'close'])
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Aggregate data by daily averages
    df = df.resample('D', on='timestamp').mean()

    returns = data_fetcher.calculate_returns(df)
    correlation_data[symbol] = returns

async def generate_correlation_plot_async(symbols, correlation_data):
    correlation_matrix = pd.DataFrame()
    for symbol1, symbol2 in combinations(symbols, 2):
        corr = correlation_data[symbol1]['return'].corr(correlation_data[symbol2]['return'])
        correlation_matrix.loc[symbol1, symbol2] = corr
        correlation_matrix.loc[symbol2, symbol1] = corr

    fig = px.imshow(correlation_matrix, x=symbols, y=symbols)
    fig.update_xaxes(side="top")
    fig.update_layout(
        title="Crypto Correlation Matrix",
        xaxis_title="Cryptocurrencies",
        yaxis_title="Cryptocurrencies",
        margin=dict(l=0, r=0, b=50, t=50)
    )

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

    return fig


@crypto_correlation_route.route('/crypto_correlation_map', methods=['GET', 'POST'])
async def create_correlation_matrix():
    if request.method == 'POST':
        since_date = datetime.strptime(request.form['since_date'], '%Y-%m-%d')
        till_date = datetime.strptime(request.form['till_date'], '%Y-%m-%d')
    else:
        today_date = datetime.now()
        since_date = today_date - timedelta(days=600)
        till_date = today_date

    symbols, correlation_data = await fetch_crypto_data_async(since_date, till_date)
    fig = await generate_correlation_plot_async(symbols, correlation_data)

    return render_template('crypto_correlation_map.html', correlation_matrix=fig.to_html())
