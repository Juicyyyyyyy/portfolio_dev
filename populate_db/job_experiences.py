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
		short_description='In my role at Runbot, I was tasked with integrating a variety of trading indicators into a user-friendly, no-code platform.',
		description="""In my role at **Runbot**, I was tasked with integrating a variety of trading indicators into a user-friendly, no-code platform. This responsibility required leveraging my in-depth knowledge of both **mathematical and financial trading indicators**, enabling me to efficiently transform these concepts into well-structured, optimal, and modular classes and functions.

Our work at Runbot involved handling extensive datasets, primarily consisting of **asset price data**, necessitating the development of functions optimized for both **time and memory efficiency**. This was critical as any inefficiency in these functions could result in significant delays for our users.

Furthermore, a profound understanding of the **Django framework** was essential for the accurate implementation of these functions, ensuring seamless integration with the **Vue.js frontend**. Additionally, my role involved utilizing a professional **Git** environment for effective version control, ensuring robust management and tracking of code changes.
""",
		url='https://runbot.io/',
		img_src='/static/img/runbot.png',
		languages_used='Python, Django'
	)

	# Add them to the session
	db.session.add(experience1)
	db.session.add(experience2)

	db.session.commit()

