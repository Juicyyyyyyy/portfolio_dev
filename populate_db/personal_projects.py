from populate_db import app, db, kill_db, Project

with app.app_context():
	db.session.query(Project).delete()
	project1 = Project(
		# project data here
		title='Multi Indicator',
		description='This is a comprehensive trading tool that presents an overview of the market in a tabular format. It consists of five distinct categories of trading indicators : Volatility , Trend, Momentum, Reversal, and Volume . Each category includes a series of indicators that are widely used in the trading community.',
		languages_used='Pinescript',
		link_url='https://www.tradingview.com/script/EKlYtPwv/',
		image_url='multi_indicator.png',
		video_url='multi_indicator.mp4'
	)

	project2 = Project(
		# project data here
		title='AI artist portfolio',
		description="This is a portfolio project displaying my AI art. Since the portfolio is made using the Django framework, I've made the galleries adaptively which mean you simply need to add a new folder inside the static/gallery folder and add images inside, and it will automatically add the new collections and use the title of the folders and files as captions.",
		languages_used='Python, Django, Css, Javascript, Git',
		link_url='https://github.com/Juicyyyyyyy/portfolio_artist',
		image_url='portfolio_artist.png',
		video_url='portfolio_artist.mp4'
	)

	project3 = Project(
		# project data here
		title='Website generator',
		description="This is an advanced frontend generator, developed leveraging the robust Laravel framework coupled with Vue.js. We've incorporated a proprietary algorithm based on GPT prompts to engineer a website generator, which facilitates the production of highly customized websites by adjusting a set of simple parameters. We are currently in the process of expanding our offerings, with imminent plans to introduce not just a frontend generator, but a comprehensive full-stack generator, to cater to a wider range of user needs.",
		languages_used='Laravel, Vue.js, Open ai API, Prompting, Git',
		link_url='https://justclickbuild.com',
		image_url='justclickbuildd.png',
		video_url=''
	)

	# Add them to the session
	db.session.add(project1)
	db.session.add(project2)
	db.session.add(project3)

	db.session.commit()
