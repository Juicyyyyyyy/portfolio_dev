from populate_db import app, db, kill_db, Experience

with app.app_context():
	db.session.query(Experience).delete()
	experience1 = Experience(
		name='JustClickBuild',
		short_description="""At JustClickBuild I worked mostly on backend developement, more specificly I imagined and created 
		the complete website generation algorithm by myself.""",
		description="""I co-founded **JustClickBuild** with my hardworking and coding-genius friend, [**Tahirou Laouan Magagi**](https://www.linkedin.com/in/tahirou-laouan-magagi-b07a49245/). At JCB, I worked primarily on backend development. More specifically, I conceptualized and developed the complete website generation algorithm independently.

Additionally, as the co-founder of JustClickBuild, I devoted a significant amount of time to creating a roadmap for the project, managing it, and organizing our tasks. To achieve this, we established a professional environment using **Notion**, which enabled us to keep track of each task, step, and modification of the project. For versioning, we utilized **Git** and are proud to share that we made more than **350 commits in one year**, while managing our studies and company internships simultaneously.

This website was developed using **Laravel, Vue.js, and the OpenAI API**. I would love to share more about how we created JCB, but as this project was designed with the goal of being profitable, I must keep some secrets to myself!

		""",
		url='https://justclickbuild.com',
		img_src='/static/img/jcb_main_page.png',
		languages_used='Laravel, Vue.js, Open AI API, Prompt Engineering'
	)

	experience2 = Experience(
		name='Runbot',
		short_description='Runbot',
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

	# Add them to the session
	db.session.add(experience1)
	db.session.add(experience2)

	db.session.commit()

