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
		description="""This tool is designed to optimize a portfolio of financial assets by finding for you the most optimal weight allocation based on your needs.

This desktop app has been developed using the **CustomTkinter Python framework** for the frontend and **Python** for the backend. I also utilized the Python library '**PyPortfolioOpt**', which aided in performing many complex mathematical calculations. 

The app's logic is grounded in several famous and internationally recognized financial and mathematical theories. The most notable is the '**Modern Portfolio Theory**' (MPT), developed in 1952 by Nobel Prize-winning financial expert **Harry Markowitz**. MPT is an investment theory that enables investors to construct an asset portfolio maximizing expected return for a given level of risk. 

Another key model is the **Black-Litterman model**, which extends modern portfolio theory by incorporating investor views of expected returns. Lastly, the **Monte Carlo simulation** is used, a method for modeling future outcomes by generating random possibilities based on specific assumptions.

To use the app, you will need to choose between manually entering each asset in the portfolio or generating a portfolio of assets using AI (**GPT-3.5**). Then, select a start date and an end date, as the app will fetch price data for this period. You must also choose the financial model you wish to use: **MPT**, **Black-Litterman**, or **Monte Carlo**. 

After filling in all parameters, click on '**continue**'. You will be directed to a page depending on the chosen model. Here, you'll need to select additional parameters before obtaining your results.
""",
		languages_used='Python, CustomTkinter, Pandas, Numpy',
		link_url='https://github.com/Juicyyyyyyy/portfolio_optimizer',
		image_url='portfolio_optimizer_.png',
		video_url='portfolio_artist.mp4'
	)

	project3 = Project(
		# project data here
		title='Component Generator',
		short_description=""" A Tailwind CSS component generator based on artificial intelligence.""",
		description="""The component generator website leverages **Django** and the **GPT-3.5 API** to deliver an innovative and powerful solution. It enables developers to generate custom Tailwind CSS components tailored to their specific needs, thanks to a user-friendly interface.
	""",
		languages_used='Python, Django, OpenAI API, Tailwind CSS, Javascript',
		link_url='https://github.com/Juicyyyyyyy/component_generator',
		image_url='component_generator.png',
		video_url='portfolio_artist.mp4'
	)

	project4 = Project(
		# project data here
		title='TrendVista Swing Indicator',
		short_description="""A trading tool based on bollinger bands and average true range giving buy/sell signals on key levels.""",
		description="""###Overview

The swing indicator is designed to offer traders a comprehensive analysis of market trends and volatility by integrating Bollinger Bands and the Average True Range (ATR). It aids in the visualization of price movements and volatility across multiple time frames, thereby providing insights into potential buy and sell opportunities.

###Key Features

- Multitimeframe Analysis: By default, the indicator examines the market across the following time frames: 1 Day (1D), 4 Hours (4H), 1 Hour (1H), and 15 Minutes (15min). Users have the flexibility to modify these time frames to suit their trading strategy by adjusting the indicator's settings.

- Buy and Sell Timings: The indicator identifies optimal buy signals when the price drops below the lower Bollinger Band and subsequently re-enters the band's range. Additionally, a buy signal is generated during high volatility periods—signified by the ATR exceeding its 10-day average—helping traders spot potential liquidation points. Sell signals are tailored for traders looking to exit long positions rather than for initiating short positions.

- Bollinger Bands Phases: The indicator categorizes the market condition into three phases based on Bollinger Bands movement:
- Neutral Phase: When the closing price is within the Bollinger Bands' upper and lower limits.
- Bullish Phase: Signaled by the price closing above the upper Bollinger Band, suggesting an upward trend until the price closes below the middle band.
- Bearish Phase: Initiated when the price closes below the lower Bollinger Band, indicating a downtrend until the price closes above the middle band.

Users can opt to exclude the neutral phase from the analysis through the indicator's settings for a more focused view on bullish or bearish trends.

###Indicator Customization

The swing indicator is versatile, allowing users to customize the time frames and phase visibility according to their preferences. This feature ensures that traders can tailor the indicator to match their specific analysis needs and trading strategies.

###Considerations

- The signals provided by the swing indicator are not symmetrically designed for both buy and sell actions. The indicator primarily optimizes for identifying long positions, particularly in bull markets. The sell signals are intended for exiting existing long positions rather than for short selling.
		""",
		languages_used='pinescript',
		link_url='https://www.tradingview.com/script/R12WO2J5-TrendVista-Swing-Indicator/',
		image_url='trendvista.png',
		video_url='portfolio_artist.mp4'
	)

	# Add them to the session
	db.session.add(project1)
	db.session.add(project2)
	db.session.add(project3)
	db.session.add(project4)

	db.session.commit()
