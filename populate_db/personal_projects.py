from populate_db import app, db, kill_db, Project

with app.app_context():
	db.session.query(Project).delete()
	project1 = Project(
		# project data here
		title='Multi Indicator',
		short_description='This tool presents an overview of the market in a tabular format, organized into five distinct categories of trading indicators.',
		description="""# Comprehensive Trading Tool Overview

This tool presents an **overview of the market** in a tabular format, organized into five distinct categories of trading indicators:

### 1. Volatility
- **Average True Range (ATR)**
- **Bollinger Bands**

### 2. Trend
- **Average Directional Index (ADX)**
- **Exponential Moving Averages (EMAs)** (four types)
- **Aroon**
- **Parabolic SAR**
- **Supertrend**

### 3. Momentum
- **Stochastic Relative Strength Index (StochRSI)**
- **Money Flow Index (MFI)**
- **Williams %R**
- **Relative Strength Index (RSI)**
- **Commodity Channel Index (CCI)**

### 4. Reversal
- **Parabolic SAR**
- **Moving Average Convergence Divergence (MACD)**
- **PP Supertrend**

### 5. Volume
- **Volume Exponential Moving Average (EMA)**

Each category includes a series of indicators that are widely used in the trading community.

## Indicator States
- **Bullish Color (Green by default)**: Indicates bullishness or high volatility.
- **Bearish Color (Red by default)**: Indicates bearishness or low volatility.
- **Very Bullish Color (Dark Green by default)**: Represents a strong bullish signal.
- **Very Bearish Color (Dark Red by default)**: Represents a strong bearish signal.
- **Neutral Color (Gray by default)**: Displayed when the indicator does not give a clear signal.

_Note: Some indicators do not have a very bullish or very bearish state. For volatility indicators, the colors represent different levels of volatility._

## Customization and Usability
- **Customizable Indicators**: Traders can choose which indicators and categories to display.
- **Reduces Chart Clutter**: Allows traders to reduce the number of indicators on their chart for better readability.
- **Quick Market View**: Provides a quick and easily readable view of the market.

This tool is designed to offer a **clear and concise view of the market**, helping traders make informed decisions with ease.""",
		languages_used='Pinescript',
		link_url='https://www.tradingview.com/script/EKlYtPwv/',
		image_url='multi_indicator.png',
		video_url='multi_indicator.mp4'
	)

	project2 = Project(
		# project data here
		title='Portfolio Optimizer',
		short_description=""" This tool is designed to optimize a portfolio of financial assets by finding for you the most 
		optimal weight allocation based on your needs.""",
		description="""This desktop app is developed using the **CustomTkinter Python framework** for the frontend and **Python** for the backend. I also utilized the Python library '**PyPortfolioOpt**', which aided in performing many complex mathematical calculations. 

The app's logic is grounded in several famous and internationally recognized financial and mathematical theories. The most notable is the '**Modern Portfolio Theory**' (MPT), developed in 1952 by Nobel Prize-winning financial expert **Harry Markowitz**. MPT is an investment theory that enables investors to construct an asset portfolio maximizing expected return for a given level of risk. 

Another key model is the **Black-Litterman model**, which extends modern portfolio theory by incorporating investor views of expected returns. Lastly, the **Monte Carlo simulation** is used, a method for modeling future outcomes by generating random possibilities based on specific assumptions.

To use the app, you will need to choose between manually entering each asset in the portfolio or generating a portfolio of assets using AI (**GPT-3.5**). Then, select a start date and an end date, as the app will fetch price data for this period. You must also choose the financial model you wish to use: **MPT**, **Black-Litterman**, or **Monte Carlo**. 

After filling in all parameters, click on '**continue**'. You will be directed to a page depending on the chosen model. Here, you'll need to select additional parameters before obtaining your results.

		""",
		languages_used='Python, CustomTkinter, Pandas, Numpy',
		link_url='https://github.com/Juicyyyyyyy/portfolio_optimizer',
		image_url='portfolio-optimizer.png',
		video_url='portfolio_artist.mp4'
	)

	# Add them to the session
	db.session.add(project1)
	db.session.add(project2)

	db.session.commit()
