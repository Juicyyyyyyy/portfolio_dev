from populate_db import app, db, kill_db, Experience

with app.app_context():
	#db.session.query(Experience).delete()
	experience1 = Experience(
		name='Waldata',
		description="""While working at Waldata I had to use my
										programming competences and my comprehension in mathematical trading indicators
										since I've worked in implementing new trading indicators, using their own
										programming language (very similar to pinescript), in their own software.
										Additionally, I
										contributed to one of their websites by doing some JavaScript and CSS tasks.""",
		url='https://www.waldata.fr/logiciels/WalMaster-Xe',
		img_src='/static/img/waldata.jpg',
		languages_used='Pinescript, Css, Javascript'
	)

	experience2 = Experience(
		name='Runbot',
		description="""At runbot I had to use again my comprehension in
										mathematical trading indicators and algorithmic logic but this time I discovered a
										whole new universe
										using for the first time the Django framework and git in a professional environment.
										I've learned a lot on the importance of backend optimisation while working on
										massive datas.""",
		url='https://runbot.io/',
		img_src='/static/img/runbot.png',
		languages_used='Python, Django'
	)

	experience3 = Experience(
		name='Codyweb',
		description="""At Codyweb I've been able to work on plenty of
										websites ordered by clients, I've done fullstack programming using Php, Css, Css
										frameworks. I've been able to create and manage professional databases used in the
										clients websites.""",
		url='https://www.codyweb.fr/',
		img_src='/static/img/codyweb.png',
		languages_used='Php, Css'
	)

	# Add them to the session
	db.session.add(experience1)
	db.session.add(experience2)
	db.session.add(experience3)

	db.session.commit()

