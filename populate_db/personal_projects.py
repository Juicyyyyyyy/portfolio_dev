from populate_db import app, db, kill_db, Project

with app.app_context():
	db.session.query(Project).delete()
	project1 = Project(
		# project data here
		title='Multi Indicator',
		short_description='This tool presents an overview of the market in a tabular format, organized into five distinct categories of trading indicators',
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
		optimal weight allocation based on your needs.  """,
		description=""" This desktop app is made using CustomTkinter python framework for the frontend and python for
		the backend. I also used the python library 'PyPortfolioOpt' which helped me for many complex math calculus.
		The app logic is based on some famous and internationally recognized financial and mathematical theories.
		The most famous one being the 'Modern Portfolio Theory' developed in 1952 by the financial Nobel price winner: 
		Harry Markowitz. he Modern Portfolio Theory (MPT) refers to an investment theory that allows investors to assemble 
		an asset portfolio that maximizes expected return for a given level of risk.""",
		languages_used='Python, CustomTkinter, Pandas, Numpy',
		link_url='https://github.com/Juicyyyyyyy/portfolio_artist',
		image_url='portfolio-optimizer.png',
		video_url='portfolio_artist.mp4'
	)

	project3 = Project(
		# project data here
		title='Website generator',
		short_description="A no-code website generator",
		description="This is an advanced frontend generator, developed leveraging the robust Laravel framework coupled with Vue.js. We've incorporated a proprietary algorithm based on GPT prompts to engineer a website generator, which facilitates the production of highly customized websites by adjusting a set of simple parameters. We are currently in the process of expanding our offerings, with imminent plans to introduce not just a frontend generator, but a comprehensive full-stack generator, to cater to a wider range of user needs.",
		languages_used='Laravel, Vue.js, Open ai API, Prompting, Git',
		link_url='https://justclickbuild.com',
		image_url='jcb_main_page.png',
		video_url=''
	)

	# Add them to the session
	db.session.add(project1)
	db.session.add(project2)
	db.session.add(project3)

	db.session.commit()
