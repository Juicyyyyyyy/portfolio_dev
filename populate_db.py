from flask import Flask

from app import db
from app import Project, Category, Experience, Skill, Post
from datetime import datetime
import os


# Vide toutes les tables de la database
def kill_db():
	meta = db.metadata
	for table in reversed(meta.sorted_tables):
		db.session.execute(table.delete())
	db.session.commit()


def create_app():
	# Create the Flask application
	app = Flask(__name__)

	# Set the configuration for the application
	app.config[
		'SQLALCHEMY_DATABASE_URI'] = os.getenv('JAWSDB_MARIA_URL')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	# Initialize SQLAlchemy with this application
	db.init_app(app)

	return app


app = create_app()
with app.app_context():
	# POPULATE PROJECTS
	kill_db()
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
		languages_used='Python, Django, Css, Javascript',
		link_url='https://github.com/Juicyyyyyyy/portfolio_artist',
		image_url='portfolio_artist.png',
		video_url='portfolio_artist.mp4'
	)

	# Add them to the session
	db.session.add(project1)
	db.session.add(project2)

	# Create new experiences
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

	# Create new categories
	category1 = Category(name='Frontend', order=1)
	category2 = Category(name='Backend', order=2)
	category3 = Category(name='Tools', order=3)
	category4 = Category(name='Databases', order=4)

	# Add them to the session
	db.session.add(category1)
	db.session.add(category2)
	db.session.add(category3)
	db.session.add(category4)

	# Commit the changes
	db.session.commit()

	# Fetch the IDs of the categories
	frontend_id = Category.query.filter_by(name='Frontend').first().id
	backend_id = Category.query.filter_by(name='Backend').first().id
	tools_id = Category.query.filter_by(name='Tools').first().id
	databases_id = Category.query.filter_by(name='Databases').first().id

	# Insert frontend skills
	frontend_skills = [
		Skill(name='HTML5', category_id=frontend_id, icon="""<svg width="60px" height="60px" viewBox="0 0 32 32" fill="none"
                                             xmlns="http://www.w3.org/2000/svg">
                                            <path d="M6 28L4 3H28L26 28L16 31L6 28Z" fill="#E44D26"/>
                                            <path d="M26 5H16V29.5L24 27L26 5Z" fill="#F16529"/>
                                            <path d="M9.5 17.5L8.5 8H24L23.5 11H11.5L12 14.5H23L22 24L16 26L10 24L9.5 19H12.5L13 21.5L16 22.5L19 21.5L19.5 17.5H9.5Z"
                                                  fill="white"/>
                                        </svg>"""),
		Skill(name='CSS', category_id=frontend_id, icon="""<svg width="60px" height="60px" viewBox="0 0 32 32" fill="none"
                                             xmlns="http://www.w3.org/2000/svg">
                                            <path d="M6 28L4 3H28L26 28L16 31L6 28Z" fill="#1172B8"/>
                                            <path d="M26 5H16V29.5L24 27L26 5Z" fill="#33AADD"/>
                                            <path d="M19.5 17.5H9.5L9 14L17 11.5H9L8.5 8.5H24L23.5 12L17 14.5H23L22 24L16 26L10 24L9.5 19H12.5L13 21.5L16 22.5L19 21.5L19.5 17.5Z"
                                                  fill="white"/>
                                        </svg>"""),
		Skill(name='Tailwind CSS', category_id=frontend_id, icon="""<svg width="60px" height="60px" viewBox="0 0 32 32"
                                             xmlns="http://www.w3.org/2000/svg"><title>file_type_tailwind</title>
                                            <path d="M9,13.7q1.4-5.6,7-5.6c5.6,0,6.3,4.2,9.1,4.9q2.8.7,4.9-2.1-1.4,5.6-7,5.6c-5.6,0-6.3-4.2-9.1-4.9Q11.1,10.9,9,13.7ZM2,22.1q1.4-5.6,7-5.6c5.6,0,6.3,4.2,9.1,4.9q2.8.7,4.9-2.1-1.4,5.6-7,5.6c-5.6,0-6.3-4.2-9.1-4.9Q4.1,19.3,2,22.1Z"
                                                  style="fill:#44a8b3"/>
                                        </svg>"""),
		Skill(name='JavaScript', category_id=frontend_id, icon="""<svg width="60px" height="60px" viewBox="0 0 32 32" fill="none"
                                             xmlns="http://www.w3.org/2000/svg">
                                            <rect x="2" y="2" width="28" height="28" fill="#FFCA28"/>
                                            <path d="M19 25.2879L21.0615 23.9237C21.2231 24.4313 22.2462 25.6368 23.5385 25.6368C24.8308 25.6368 25.4308 24.931 25.4308 24.463C25.4308 23.1878 24.1112 22.7382 23.4774 22.5223C23.374 22.4871 23.289 22.4581 23.2308 22.4328C23.2009 22.4198 23.1558 22.4025 23.0979 22.3804C22.393 22.1111 19.7923 21.1175 19.7923 18.2373C19.7923 15.065 22.8538 14.7002 23.5462 14.7002C23.9991 14.7002 26.1769 14.7557 27.2615 16.7939L25.2615 18.1898C24.8231 17.3015 24.0946 17.0081 23.6462 17.0081C22.5385 17.0081 22.3077 17.8201 22.3077 18.1898C22.3077 19.227 23.5112 19.6919 24.5273 20.0844C24.7932 20.1871 25.0462 20.2848 25.2615 20.3866C26.3692 20.91 28 21.7666 28 24.463C28 25.8136 26.8672 28.0002 24.0154 28.0002C20.1846 28.0002 19.1692 25.7003 19 25.2879Z"
                                                  fill="#3E3E3E"/>
                                            <path d="M9 25.5587L11.1487 24.1953C11.317 24.7026 11.9713 25.638 12.9205 25.638C13.8698 25.638 14.3557 24.663 14.3557 24.1953V15.0002H16.9982V24.1953C17.041 25.4636 16.3376 28.0002 13.2332 28.0002C10.379 28.0002 9.19242 26.3039 9 25.5587Z"
                                                  fill="#3E3E3E"/>
                                        </svg>""")
	]

	# Insert backend skills
	backend_skills = [
		Skill(name='PHP', category_id=backend_id, icon="""<svg width="60px" height="60px" viewBox="0 0 32 32" fill="none"
                                             xmlns="http://www.w3.org/2000/svg">
                                            <circle cx="16" cy="16" r="14" fill="#8892BF"/>
                                            <path d="M14.4392 10H16.1192L15.6444 12.5242H17.154C17.9819 12.5419 18.5986 12.7269 19.0045 13.0793C19.4184 13.4316 19.5402 14.1014 19.3698 15.0881L18.5541 19.4889H16.8497L17.6288 15.2863C17.7099 14.8457 17.6856 14.533 17.5558 14.348C17.426 14.163 17.146 14.0705 16.7158 14.0705L15.3644 14.0573L14.3661 19.4889H12.6861L14.4392 10Z"
                                                  fill="white"/>
                                            <path fill-rule="evenodd" clip-rule="evenodd"
                                                  d="M6.74092 12.5243H10.0036C10.9612 12.533 11.6552 12.8327 12.0854 13.4229C12.5156 14.0132 12.6576 14.8193 12.5115 15.8414C12.4548 16.3085 12.3289 16.7665 12.1341 17.2159C11.9474 17.6652 11.6878 18.0704 11.355 18.4317C10.9491 18.8898 10.5149 19.1805 10.0523 19.304C9.58969 19.4274 9.11076 19.489 8.61575 19.489H7.15484L6.69222 22H5L6.74092 12.5243ZM7.43485 17.9956L8.16287 14.0441H8.40879C8.49815 14.0441 8.5914 14.0396 8.6888 14.0309C9.33817 14.0221 9.87774 14.0882 10.308 14.2291C10.7462 14.37 10.8923 14.9031 10.7462 15.8282C10.5678 16.9296 10.2186 17.5727 9.69926 17.7577C9.1799 17.934 8.53053 18.0176 7.75138 18.0088H7.58094C7.53224 18.0088 7.48355 18.0043 7.43485 17.9956Z"
                                                  fill="white"/>
                                            <path fill-rule="evenodd" clip-rule="evenodd"
                                                  d="M24.4365 12.5243H21.1738L19.4329 22H21.1251L21.5878 19.489H23.0487C23.5437 19.489 24.0226 19.4274 24.4852 19.304C24.9479 19.1805 25.382 18.8898 25.7879 18.4317C26.1207 18.0704 26.3803 17.6652 26.567 17.2159C26.7618 16.7665 26.8877 16.3085 26.9444 15.8414C27.0905 14.8193 26.9486 14.0132 26.5183 13.4229C26.0881 12.8327 25.3942 12.533 24.4365 12.5243ZM22.5958 14.0441L21.8678 17.9956C21.9165 18.0043 21.9652 18.0088 22.0139 18.0088H22.1843C22.9635 18.0176 23.6128 17.934 24.1322 17.7577C24.6515 17.5727 25.0007 16.9296 25.1792 15.8282C25.3253 14.9031 25.1792 14.37 24.7409 14.2291C24.3107 14.0882 23.7711 14.0221 23.1217 14.0309C23.0243 14.0396 22.9311 14.0441 22.8417 14.0441H22.5958Z"
                                                  fill="white"/>
                                        </svg>"""),
		Skill(name='Python', category_id=backend_id, icon="""<svg width="60px" height="60px" viewBox="0 0 32 32" fill="none"
                                             xmlns="http://www.w3.org/2000/svg">
                                            <path fill-rule="evenodd" clip-rule="evenodd"
                                                  d="M13.0164 2C10.8193 2 9.03825 3.72453 9.03825 5.85185V8.51852H15.9235V9.25926H5.97814C3.78107 9.25926 2 10.9838 2 13.1111L2 18.8889C2 21.0162 3.78107 22.7407 5.97814 22.7407H8.27322V19.4815C8.27322 17.3542 10.0543 15.6296 12.2514 15.6296H19.5956C21.4547 15.6296 22.9617 14.1704 22.9617 12.3704V5.85185C22.9617 3.72453 21.1807 2 18.9836 2H13.0164ZM12.0984 6.74074C12.8589 6.74074 13.4754 6.14378 13.4754 5.40741C13.4754 4.67103 12.8589 4.07407 12.0984 4.07407C11.3378 4.07407 10.7213 4.67103 10.7213 5.40741C10.7213 6.14378 11.3378 6.74074 12.0984 6.74074Z"
                                                  fill="url(#paint0_linear_87_8204)"/>
                                            <path fill-rule="evenodd" clip-rule="evenodd"
                                                  d="M18.9834 30C21.1805 30 22.9616 28.2755 22.9616 26.1482V23.4815L16.0763 23.4815L16.0763 22.7408L26.0217 22.7408C28.2188 22.7408 29.9998 21.0162 29.9998 18.8889V13.1111C29.9998 10.9838 28.2188 9.25928 26.0217 9.25928L23.7266 9.25928V12.5185C23.7266 14.6459 21.9455 16.3704 19.7485 16.3704L12.4042 16.3704C10.5451 16.3704 9.03809 17.8296 9.03809 19.6296L9.03809 26.1482C9.03809 28.2755 10.8192 30 13.0162 30H18.9834ZM19.9015 25.2593C19.1409 25.2593 18.5244 25.8562 18.5244 26.5926C18.5244 27.329 19.1409 27.9259 19.9015 27.9259C20.662 27.9259 21.2785 27.329 21.2785 26.5926C21.2785 25.8562 20.662 25.2593 19.9015 25.2593Z"
                                                  fill="url(#paint1_linear_87_8204)"/>
                                            <defs>
                                                <linearGradient id="paint0_linear_87_8204" x1="12.4809" y1="2"
                                                                x2="12.4809" y2="22.7407"
                                                                gradientUnits="userSpaceOnUse">
                                                    <stop stop-color="#327EBD"/>
                                                    <stop offset="1" stop-color="#1565A7"/>
                                                </linearGradient>
                                                <linearGradient id="paint1_linear_87_8204" x1="19.519" y1="9.25928"
                                                                x2="19.519" y2="30" gradientUnits="userSpaceOnUse">
                                                    <stop stop-color="#FFDA4B"/>
                                                    <stop offset="1" stop-color="#F9C600"/>
                                                </linearGradient>
                                            </defs>
                                        </svg>"""),
		Skill(name='Laravel', category_id=backend_id, icon="""<svg width="60px" height="60px" viewBox="-4 0 264 264" version="1.1"
                                             xmlns="http://www.w3.org/2000/svg"
                                             xmlns:xlink="http://www.w3.org/1999/xlink" preserveAspectRatio="xMidYMid">
                                            <g>
                                                <path d="M255.855641,59.619717 C255.950565,59.9710596 256,60.3333149 256,60.6972536 L256,117.265345 C256,118.743206 255.209409,120.108149 253.927418,120.843385 L206.448786,148.178786 L206.448786,202.359798 C206.448786,203.834322 205.665123,205.195421 204.386515,205.937838 L105.27893,262.990563 C105.05208,263.119455 104.804608,263.201946 104.557135,263.289593 C104.464333,263.320527 104.376687,263.377239 104.278729,263.403017 C103.585929,263.58546 102.857701,263.58546 102.164901,263.403017 C102.051476,263.372083 101.948363,263.310215 101.840093,263.26897 C101.613244,263.186479 101.376082,263.1143 101.159544,262.990563 L2.07258227,205.937838 C0.7913718,205.201819 0,203.837372 0,202.359798 L0,32.6555248 C0,32.2843161 0.0515567729,31.9234187 0.144358964,31.5728326 C0.175293028,31.454252 0.24747251,31.3459828 0.288717928,31.2274022 C0.366053087,31.0108638 0.438232569,30.7891697 0.55165747,30.5880982 C0.628992629,30.4540506 0.742417529,30.3457814 0.83521972,30.2220451 C0.953800298,30.0570635 1.06206952,29.8869261 1.20127281,29.7425672 C1.31985339,29.6239866 1.4745237,29.5363401 1.60857131,29.4332265 C1.75808595,29.3094903 1.89213356,29.1754427 2.06227091,29.0774848 L2.06742659,29.0774848 L51.6134853,0.551122364 C52.8901903,-0.183535768 54.4613221,-0.183535768 55.7380271,0.551122364 L105.284086,29.0774848 L105.294397,29.0774848 C105.459379,29.1805983 105.598582,29.3094903 105.748097,29.4280708 C105.882144,29.5311844 106.031659,29.6239866 106.15024,29.7374115 C106.294599,29.8869261 106.397712,30.0570635 106.521448,30.2220451 C106.609095,30.3457814 106.727676,30.4540506 106.799855,30.5880982 C106.918436,30.7943253 106.985459,31.0108638 107.06795,31.2274022 C107.109196,31.3459828 107.181375,31.454252 107.212309,31.5779883 C107.307234,31.9293308 107.355765,32.2915861 107.356668,32.6555248 L107.356668,138.651094 L148.643332,114.878266 L148.643332,60.6920979 C148.643332,60.3312005 148.694889,59.9651474 148.787691,59.619717 C148.823781,59.4959808 148.890804,59.3877116 148.93205,59.269131 C149.014541,59.0525925 149.08672,58.8308984 149.200145,58.629827 C149.27748,58.4957794 149.390905,58.3875102 149.478552,58.2637739 C149.602288,58.0987922 149.705401,57.9286549 149.84976,57.7842959 C149.968341,57.6657153 150.117856,57.5780688 150.251903,57.4749553 C150.406573,57.351219 150.540621,57.2171714 150.705603,57.1192136 L150.710758,57.1192136 L200.261973,28.5928511 C201.538395,27.8571345 203.110093,27.8571345 204.386515,28.5928511 L253.932573,57.1192136 C254.107866,57.2223271 254.241914,57.351219 254.396584,57.4697996 C254.525476,57.5729132 254.674991,57.6657153 254.793572,57.7791402 C254.93793,57.9286549 255.041044,58.0987922 255.16478,58.2637739 C255.257582,58.3875102 255.371007,58.4957794 255.443187,58.629827 C255.561767,58.8308984 255.628791,59.0525925 255.711282,59.269131 C255.757683,59.3877116 255.824707,59.4959808 255.855641,59.619717 Z M247.740605,114.878266 L247.740605,67.8378666 L230.402062,77.8192579 L206.448786,91.6106946 L206.448786,138.651094 L247.745761,114.878266 L247.740605,114.878266 Z M198.194546,199.97272 L198.194546,152.901386 L174.633101,166.357704 L107.351512,204.757188 L107.351512,252.27191 L198.194546,199.97272 Z M8.25939501,39.7961379 L8.25939501,199.97272 L99.0921175,252.266755 L99.0921175,204.762344 L51.6392637,177.906421 L51.6237967,177.89611 L51.603174,177.885798 C51.443348,177.792996 51.3093004,177.658949 51.1597857,177.545524 C51.0308938,177.44241 50.8813791,177.359919 50.7679542,177.246494 L50.7576429,177.231027 C50.6235953,177.102135 50.5307931,176.942309 50.4173682,176.79795 C50.3142546,176.658747 50.1905184,176.540167 50.1080276,176.395808 L50.1028719,176.380341 C50.0100697,176.22567 49.9533572,176.040066 49.8863334,175.864773 C49.8193096,175.710103 49.7316631,175.565744 49.6904177,175.400762 L49.6904177,175.395606 C49.6388609,175.19969 49.6285496,174.993463 49.6079269,174.792392 C49.5873041,174.637722 49.5460587,174.483051 49.5460587,174.328381 L49.5460587,174.31807 L49.5460587,63.5689658 L25.5979377,49.7723734 L8.25939501,39.8012935 L8.25939501,39.7961379 Z M53.6809119,8.89300821 L12.3994039,32.6555248 L53.6706006,56.4180414 L94.9469529,32.6503692 L53.6706006,8.89300821 L53.6809119,8.89300821 Z M75.1491521,157.19091 L99.0972731,143.404629 L99.0972731,39.7961379 L81.7587304,49.7775291 L57.8054537,63.5689658 L57.8054537,167.177457 L75.1491521,157.19091 Z M202.324244,36.934737 L161.047891,60.6972536 L202.324244,84.4597702 L243.59544,60.6920979 L202.324244,36.934737 Z M198.194546,91.6106946 L174.24127,77.8192579 L156.902727,67.8378666 L156.902727,114.878266 L180.850848,128.664547 L198.194546,138.651094 L198.194546,91.6106946 Z M103.216659,197.616575 L163.759778,163.052915 L194.023603,145.781396 L152.778185,122.034346 L105.289242,149.374903 L62.0073307,174.292291 L103.216659,197.616575 Z"
                                                      fill="#FF2D20">

                                                </path>
                                            </g>
                                        </svg>"""),
		Skill(name='Django', category_id=backend_id, icon="""<svg width="60px" height="60px" viewBox="0 0 256 256" version="1.1"
                                             xmlns="http://www.w3.org/2000/svg"
                                             xmlns:xlink="http://www.w3.org/1999/xlink" preserveAspectRatio="xMidYMid">
                                            <g>
                                                <rect fill="#092E20" x="0" y="0" width="256" height="256" rx="28">

                                                </rect>
                                                <path d="M186.377012,94.197636 L186.377012,160.424478 C186.377012,183.243286 184.707519,194.187745 179.699037,203.649406 C175.060358,212.741266 168.937684,218.490548 156.323731,224.798721 L129.794937,212.183571 C142.410087,206.247593 148.531564,201.05481 152.427049,193.074749 C156.509231,184.91278 157.808923,175.451119 157.808923,150.593015 L157.808923,94.197636 L186.377012,94.197636 Z M140.928486,50.0787207 L140.928486,182.316986 C126.272844,185.099476 115.512688,186.212472 103.826231,186.212472 C68.9487718,186.212472 50.7686431,170.445031 50.7686431,140.205054 C50.7686431,111.079269 70.0629644,92.1583404 99.9295492,92.1583404 C104.567032,92.1583404 108.091519,92.5281423 112.359199,93.6411381 L112.359199,50.0787207 L140.928486,50.0787207 Z M102.713236,115.160254 C88.243093,115.160254 79.8944275,124.065418 79.8944275,139.647359 C79.8944275,154.860696 87.8720944,163.208164 102.527736,163.208164 C105.680028,163.208164 108.278215,163.022665 112.359199,162.467364 L112.359199,116.643052 C109.020212,115.531253 106.237722,115.160254 102.713236,115.160254 Z M186.377012,50.2307105 L186.377012,79.5419941 L157.808923,79.5419941 L157.808923,50.2307105 L186.377012,50.2307105 Z"
                                                      fill="#FFFFFD">

                                                </path>
                                            </g>
                                        </svg>""")
	]

	db_skills = [
		Skill(name='MySql', category_id=databases_id, icon="""<svg width="60px" height="60px" viewBox="-8.78 0 70 70"
                                             xmlns:dc="http://purl.org/dc/elements/1.1/"
                                             xmlns:cc="http://creativecommons.org/ns#"
                                             xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                                             xmlns="http://www.w3.org/2000/svg">
                                            <metadata>
                                                <rdf:RDF>
                                                    <cc:Work>
                                                        <dc:subject>
                                                            Data
                                                        </dc:subject>
                                                        <dc:identifier>
                                                            sql-database-generic
                                                        </dc:identifier>
                                                        <dc:title>
                                                            SQL Database (Generic)
                                                        </dc:title>
                                                        <dc:format>
                                                            image/svg+xml
                                                        </dc:format>
                                                        <dc:publisher>
                                                            Amido Limited
                                                        </dc:publisher>
                                                        <dc:creator>
                                                            Richard Slater
                                                        </dc:creator>
                                                        <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage"/>
                                                    </cc:Work>
                                                </rdf:RDF>
                                            </metadata>
                                            <path d="m 852.97077,1013.9363 c -6.55238,-0.4723 -13.02857,-2.1216 -17.00034,-4.3296 -2.26232,-1.2576 -3.98589,-2.8032 -4.66223,-4.1807 l -0.4024,-0.8196 0,-25.70807 0,-25.7081 0.31843,-0.6465 c 1.42297,-2.889 5.96432,-5.4935 12.30378,-7.0562 2.15195,-0.5305 5.2586,-1.0588 7.79304,-1.3252 2.58797,-0.2721 9.44765,-0.2307 12.02919,0.073 6.86123,0.8061 12.69967,2.6108 16.29768,5.0377 1.38756,0.9359 2.81137,2.4334 3.29371,3.4642 l 0.41358,0.8838 -0.0354,25.6303 -0.0354,25.63047 -0.33195,0.6744 c -0.18257,0.3709 -0.73406,1.1007 -1.22553,1.6216 -2.99181,3.1715 -9.40919,5.5176 -17.8267,6.5172 -1.71567,0.2038 -9.16916,0.3686 -10.92937,0.2417 z m 12.07501,-22.02839 c -0.0252,-0.0657 -1.00472,-0.93831 -2.17671,-1.93922 -1.17199,-1.00091 -2.18138,-1.86687 -2.24309,-1.92436 -0.0617,-0.0575 0.15481,-0.26106 0.48117,-0.45237 0.32635,-0.19131 0.95163,-0.7235 1.3895,-1.18265 1.2805,-1.34272 1.88466,-3.00131 1.88466,-5.17388 0,-2.1388 -0.65162,-3.8645 -1.95671,-5.1818 -1.31533,-1.3278 -2.82554,-1.8983 -5.02486,-1.8983 -3.39007,0 -5.99368,1.9781 -6.82468,5.1851 -0.28586,1.1031 -0.28432,3.33211 0.003,4.31023 0.74941,2.55136 2.79044,4.40434 5.33062,4.83946 0.8596,0.14724 0.97605,0.21071 1.5621,0.85144 0.34829,0.38078 1.06301,1.14085 1.58827,1.68904 l 0.95501,0.9967 2.53878,0 c 1.39633,0 2.51816,-0.0537 2.49296,-0.11939 z m -8.70653,-7.10848 c -0.61119,-0.31868 -0.84225,-0.56599 -1.19079,-1.27453 -0.26919,-0.54724 -0.31522,-0.85851 -0.31824,-2.15197 -0.003,-1.3143 0.0388,-1.5983 0.31987,-2.169 0.45985,-0.9339 1.09355,-1.376 2.07384,-1.4469 1.36454,-0.099 2.15217,0.5707 2.56498,2.1801 0.50612,1.97321 -0.0504,4.07107 -1.26471,4.76729 -0.63707,0.36527 -1.58737,0.40659 -2.18495,0.095 z m -11.25315,3.66269 c 2.66179,-0.5048 4.1728,-2.0528 4.1728,-4.27495 0,-1.97137 -0.97548,-3.12004 -3.6716,-4.32364 -1.54338,-0.689 -2.10241,-1.1215 -2.10241,-1.6268 0,-0.4188 0.53052,-0.8777 1.14813,-0.993 0.60302,-0.1126 2.20237,0.1652 3.14683,0.5467 l 0.79167,0.3198 0,-1.7524 0,-1.7525 -0.85923,-0.1906 c -0.53103,-0.1178 -1.64689,-0.1885 -2.92137,-0.1849 -1.80528,0 -2.15881,0.044 -2.83818,0.3138 -1.98445,0.7878 -2.92613,2.1298 -2.91107,4.1485 0.0141,1.8898 1.01108,3.06864 3.49227,4.12912 1.46399,0.62572 2.05076,1.10218 2.05076,1.66522 0,1.1965 -1.99362,1.34375 -4.10437,0.30315 -0.57805,-0.28498 -1.09739,-0.54137 -1.1541,-0.56976 -0.0567,-0.0284 -0.10311,0.79023 -0.10311,1.81917 0,1.86239 0.002,1.87137 0.33919,1.99974 1.26979,0.48278 4.07626,0.69787 5.52379,0.42335 z m 30.4308,-1.72766 0,-1.58098 -2.40584,0 -2.40583,0 0,-5.43035 0,-5.4303 -2.13089,0 -2.13088,0 0,7.0113 0,7.01131 4.53672,0 4.53672,0 0,-1.58098 z m -14.84745,-27.70503 c 4.23447,-0.2937 7.4086,-0.8482 10.20178,-1.7821 2.78264,-0.9304 4.42643,-2.0562 4.79413,-3.2834 0.14166,-0.4729 0.13146,-0.6523 -0.0665,-1.1708 -0.88775,-2.3245 -5.84694,-4.1104 -13.42493,-4.8345 -3.24154,-0.3098 -9.13671,-0.2094 -12.22745,0.2081 -4.71604,0.6372 -8.54333,1.8208 -10.2451,3.1683 -3.44251,2.726 0.19793,5.7242 8.66397,7.1354 3.67084,0.6119 8.42674,0.828 12.30414,0.559 z"
                                                  fill="#00bcf2" transform="translate(-830.906 -943.981)"/>
                                        </svg>"""),
	]

	tools_skills = [
		Skill(name='Git', category_id=tools_id, icon="""<svg width="60px" height="60px" viewBox="0 0 32 32" fill="none"
                                             xmlns="http://www.w3.org/2000/svg">
                                            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                                            <g id="SVGRepo_tracerCarrier" stroke-linecap="round"
                                               stroke-linejoin="round"></g>
                                            <g id="SVGRepo_iconCarrier">
                                                <path d="M2.58536 17.4132C1.80488 16.6327 1.80488 15.3673 2.58536 14.5868L14.5868 2.58536C15.3673 1.80488 16.6327 1.80488 17.4132 2.58536L29.4146 14.5868C30.1951 15.3673 30.1951 16.6327 29.4146 17.4132L17.4132 29.4146C16.6327 30.1951 15.3673 30.1951 14.5868 29.4146L2.58536 17.4132Z"
                                                      fill="#EE513B"></path>
                                                <path d="M12.1489 5.06152L10.9336 6.27686L14.0725 9.41577C13.9455 9.68819 13.8746 9.99201 13.8746 10.3124C13.8746 11.222 14.4461 11.9981 15.2496 12.3012V19.9798C14.4461 20.2829 13.8746 21.059 13.8746 21.9686C13.8746 23.1422 14.826 24.0936 15.9996 24.0936C17.1732 24.0936 18.1246 23.1422 18.1246 21.9686C18.1246 21.144 17.6549 20.429 16.9684 20.0768V12.3117L19.9689 15.3122C19.8481 15.5791 19.7809 15.8754 19.7809 16.1874C19.7809 17.361 20.7323 18.3124 21.9059 18.3124C23.0795 18.3124 24.0309 17.361 24.0309 16.1874C24.0309 15.0138 23.0795 14.0624 21.9059 14.0624C21.6778 14.0624 21.4582 14.0983 21.2522 14.1648L18.0297 10.9423C18.0914 10.7433 18.1246 10.5317 18.1246 10.3124C18.1246 9.13878 17.1732 8.18738 15.9996 8.18738C15.7803 8.18738 15.5688 8.22061 15.3697 8.2823L12.1489 5.06152Z"
                                                      fill="white"></path>
                                            </g>
                                        </svg>"""),
		Skill(name='Github', category_id=tools_id, icon="""<svg width="60px" height="60px" viewBox="0 -0.5 48 48" version="1.1"
                                             xmlns="http://www.w3.org/2000/svg"
                                             xmlns:xlink="http://www.w3.org/1999/xlink" fill="#000000">
                                            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                                            <g id="SVGRepo_tracerCarrier" stroke-linecap="round"
                                               stroke-linejoin="round"></g>
                                            <g id="SVGRepo_iconCarrier"><title>Github-color</title>
                                                <desc>Created with Sketch.</desc>
                                                <defs></defs>
                                                <g id="Icons" stroke="none" stroke-width="1" fill="none"
                                                   fill-rule="evenodd">
                                                    <g id="Color-" transform="translate(-700.000000, -560.000000)"
                                                       fill="#3E75C3">
                                                        <path d="M723.9985,560 C710.746,560 700,570.787092 700,584.096644 C700,594.740671 706.876,603.77183 716.4145,606.958412 C717.6145,607.179786 718.0525,606.435849 718.0525,605.797328 C718.0525,605.225068 718.0315,603.710086 718.0195,601.699648 C711.343,603.155898 709.9345,598.469394 709.9345,598.469394 C708.844,595.686405 707.2705,594.94548 707.2705,594.94548 C705.091,593.450075 707.4355,593.480194 707.4355,593.480194 C709.843,593.650366 711.1105,595.963499 711.1105,595.963499 C713.2525,599.645538 716.728,598.58234 718.096,597.964902 C718.3135,596.407754 718.9345,595.346062 719.62,594.743683 C714.2905,594.135281 708.688,592.069123 708.688,582.836167 C708.688,580.205279 709.6225,578.054788 711.1585,576.369634 C710.911,575.759726 710.0875,573.311058 711.3925,569.993458 C711.3925,569.993458 713.4085,569.345902 717.9925,572.46321 C719.908,571.928599 721.96,571.662047 724.0015,571.651505 C726.04,571.662047 728.0935,571.928599 730.0105,572.46321 C734.5915,569.345902 736.603,569.993458 736.603,569.993458 C737.9125,573.311058 737.089,575.759726 736.8415,576.369634 C738.3805,578.054788 739.309,580.205279 739.309,582.836167 C739.309,592.091712 733.6975,594.129257 728.3515,594.725612 C729.2125,595.469549 729.9805,596.939353 729.9805,599.18773 C729.9805,602.408949 729.9505,605.006706 729.9505,605.797328 C729.9505,606.441873 730.3825,607.191834 731.6005,606.9554 C741.13,603.762794 748,594.737659 748,584.096644 C748,570.787092 737.254,560 723.9985,560"
                                                              id="Github"></path>
                                                    </g>
                                                </g>
                                            </g>
                                        </svg>"""),
		Skill(name='Midjourney', category_id=tools_id, icon="""<svg version="1.0" xmlns="http://www.w3.org/2000/svg"
                                             width="60px" height="60px" viewBox="0 0 60.000000 60.000000"
                                             preserveAspectRatio="xMidYMid meet">
                                            <g transform="translate(0.000000,60.000000) scale(0.005859,-0.005859)"
                                               fill="#000000" stroke="none">
                                                <path d="M2610 8012 c-45 -46 -40 -75 33 -211 322 -590 537 -1208 602 -1731
18 -144 20 -479 5 -658 -59 -689 -297 -1317 -642 -1699 -55 -60 -65 -91 -48
-134 32 -77 91 -78 210 -5 329 204 794 374 1220 447 122 21 166 23 460 24 339
0 391 -5 680 -56 248 -44 543 -126 761 -210 74 -28 146 -53 160 -56 37 -7 84
20 99 57 17 41 -4 178 -62 404 -184 725 -604 1516 -1152 2170 -541 645 -1266
1213 -2034 1593 -207 102 -246 111 -292 65z m434 -358 c315 -173 669 -414 966
-658 840 -690 1492 -1625 1817 -2604 49 -149 113 -406 101 -411 -5 -1 -48 11
-96 27 -281 98 -619 175 -942 214 -253 31 -641 31 -861 0 -313 -44 -605 -125
-894 -247 -60 -26 -116 -49 -124 -53 -10 -4 -8 5 7 29 33 55 136 266 175 360
200 485 304 1171 256 1689 -44 477 -234 1100 -495 1622 -24 48 -44 90 -44 93
0 10 15 3 134 -61z"/>
                                                <path d="M4488 7314 c-34 -18 -48 -43 -48 -86 0 -45 11 -58 102 -120 258 -177
615 -508 801 -743 419 -527 861 -1426 1118 -2275 28 -90 58 -173 67 -183 30
-34 59 -38 144 -22 44 8 124 18 177 21 118 7 213 -16 425 -100 179 -72 222
-72 251 -2 17 41 13 59 -66 261 -239 616 -555 1206 -873 1630 -51 69 -180 230
-196 245 -3 3 -30 32 -59 65 -574 632 -1141 1093 -1551 1260 -68 27 -211 65
-245 65 -11 -1 -32 -7 -47 -16z m1052 -798 c149 -129 577 -558 704 -706 315
-367 625 -874 873 -1430 70 -157 143 -335 143 -349 0 -5 -48 7 -107 27 -104
35 -114 36 -253 36 -80 1 -165 -1 -189 -4 l-44 -4 -52 164 c-214 677 -543
1383 -902 1935 -47 72 -104 155 -126 185 -61 80 -221 272 -246 294 -11 11 -21
23 -21 28 0 11 55 -33 220 -176z"/>
                                                <path d="M8080 3632 c-47 -2 -699 -44 -1355 -87 -209 -14 -456 -29 -550 -35
-93 -6 -264 -17 -380 -25 -115 -8 -291 -19 -390 -25 -99 -6 -349 -22 -555 -35
-206 -14 -586 -38 -845 -55 -258 -17 -607 -39 -775 -50 -168 -11 -451 -29
-630 -40 -483 -29 -478 -28 -500 -96 -13 -39 -5 -60 123 -300 l65 -121 -166
-114 c-269 -185 -366 -239 -429 -239 -14 0 -37 -13 -54 -29 -41 -41 -40 -91 2
-133 29 -29 33 -30 95 -25 87 7 197 60 378 184 305 210 381 253 446 253 48 0
100 -32 259 -159 215 -171 296 -220 426 -260 108 -34 213 -38 315 -12 119 29
202 75 377 205 201 151 243 171 353 171 108 0 155 -22 295 -135 159 -129 202
-160 279 -199 91 -46 168 -64 271 -64 154 1 284 63 475 224 178 150 257 185
393 176 101 -7 160 -35 290 -141 265 -215 368 -266 545 -266 161 0 281 54 490
222 81 64 176 132 212 150 60 30 72 33 165 33 93 0 105 -2 166 -32 38 -19 114
-74 176 -127 61 -52 133 -111 159 -132 112 -86 294 -143 363 -114 36 15 61 55
61 98 0 44 -58 92 -110 92 -84 0 -145 34 -310 175 -210 180 -301 227 -466 241
-162 15 -304 -45 -524 -221 -211 -169 -307 -209 -442 -185 -55 10 -175 57
-166 65 2 2 59 31 128 66 250 125 637 344 800 453 213 142 640 463 665 500 20
28 18 86 -3 113 -20 27 -61 39 -122 35z m-280 -219 c0 -9 -274 -205 -396 -285
-230 -150 -745 -429 -916 -497 l-56 -23 -69 53 c-184 142 -385 181 -574 113
-92 -33 -171 -84 -324 -209 -66 -54 -149 -112 -185 -129 -58 -27 -75 -31 -155
-31 -133 0 -185 27 -424 222 -210 171 -383 216 -576 151 -81 -28 -154 -73
-320 -198 -77 -58 -169 -119 -205 -135 -60 -28 -74 -30 -175 -30 -106 0 -113
1 -187 37 -98 46 -143 77 -293 199 -217 174 -307 218 -424 204 l-57 -7 -56
104 c-30 57 -52 106 -49 109 6 7 241 24 791 59 173 11 560 36 860 55 300 19
718 46 930 60 212 13 493 32 625 40 132 9 449 29 705 45 609 40 1205 79 1355
89 172 12 175 12 175 4z"/>
                                            </g>
                                        </svg>""")
	]

	# Add all skills to the session
	db.session.add_all(frontend_skills)
	db.session.add_all(backend_skills)
	db.session.add_all(db_skills)
	db.session.add_all(tools_skills)

	title = "Edward Hopper: Capturing the Essence of Solitude in American Art"
	excerpt = "Unfolding the life, art, and profound impact of American realist painter Edward Hopper."
	header = "An Exploration into Edward Hopper's Substantial Influence on the American Art Scene"
	introduction = "This post uncovers the intriguing life of Edward Hopper and his unique approach to capturing solitude and introspection, deeply impacting the course of American Art."
	body = """

Curabitur consequat nec neque sit amet dapibus. Nulla facilisi. Donec convallis eros nec tempor pretium. Sed cursus, justo eget aliquam luctus, urna urna convallis enim, sit amet condimentum odio nisi sit amet erat. Mauris cursus nulla leo, sit amet aliquet lorem scelerisque at. Nam ac enim nulla. Suspendisse pellentesque eros sit amet justo sagittis tempor. Nunc vulputate viverra ante, in interdum mauris. Fusce condimentum euismod dolor. Lorem ipsum dolor sit amet, consectetur adipiscing elit.

Morbi vel feugiat leo. Vestibulum maximus velit risus, ac sollicitudin sem lobortis ut. Curabitur ornare odio tellus, vitae tristique mauris maximus in. Mauris cursus nulla orci, a dignissim orci venenatis et. Nam ac sapien eu nisl tincidunt finibus. Quisque vel ultrices lorem. Maecenas eget finibus libero. Quisque sed nisi ac est vehicula commodo id sit amet eros. Quisque ut iaculis ipsum.

Donec sit amet orci faucibus ante eleifend commodo sit amet vel eros. Mauris eu sem placerat tellus facilisis mattis. Proin facilisis magna id mauris tristique sagittis. Praesent sodales pulvinar erat vitae dictum. Phasellus tortor augue, rhoncus ut sollicitudin sed, scelerisque nec dui. Sed lobortis et lacus vitae volutpat. Quisque at sollicitudin leo, vitae aliquam ipsum. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Ut ut justo ac magna elementum rhoncus eget at nisi. Suspendisse ut mauris a enim gravida viverra. Donec id cursus diam. Integer at risus at elit vestibulum malesuada. Nunc gravida condimentum vestibulum.

Proin eget nunc felis. Fusce luctus maximus nulla sit amet accumsan. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec blandit mauris et ligula ornare, nec tristique risus scelerisque. Etiam egestas tempor libero. Aliquam ac pharetra erat. Nullam et semper massa. Maecenas eget ipsum nisl. Curabitur non iaculis nulla, sed consectetur tortor. Maecenas blandit, nulla finibus pharetra sagittis, felis nunc dignissim libero, a commodo sapien felis a quam. Nunc non quam odio. Suspendisse potenti. Maecenas eu diam vel lacus imperdiet consequat. Cras quis convallis nulla. Proin ut sapien a nunc facilisis commodo quis eu arcu. Donec venenatis laoreet magna, et accumsan dolor hendrerit vitae.
	"""
	conclusion = "From his early days in New York to his lasting impact on global art, Edward Hopper's journey is a tribute to the enduring power of art to encapsulate human emotions and experiences. His work, a blend of realism and emotion, continues to inspire, educate, and move audiences today."
	image_url = "https://www.edwardhopper.net/images/paintings/summer-evening.jpg"  # replace with the actual image URL

	post = Post(
		title=title,
		excerpt=excerpt,
		header=header,
		introduction=introduction,
		body=body,
		conclusion=conclusion,
		date_posted=datetime.utcnow(),
		image_url=image_url
	)

	# Add the post to the session
	db.session.add(post)

	title = "Alan Turing: Unveiling the Architect of the Modern Computer"
	excerpt = "A deep dive into the life and pioneering contributions of Alan Turing, the genius behind modern computing."
	header = "The Life and Legacy of Alan Turing: The Father of Modern Computing"
	introduction = "This post delves into the groundbreaking journey of Alan Turing, his pivotal role in World War II, and his enduring impact on the field of computer science."
	body = """

Suspendisse vulputate viverra sem. Nulla cursus quis enim sit amet condimentum. Suspendisse at eros vehicula, ultrices justo id, rutrum risus. Nam finibus ante in sollicitudin lobortis. Quisque id elit eget nulla vestibulum ultrices. Sed pellentesque, massa sit amet auctor tincidunt, lacus est posuere velit, ac interdum nulla leo sit amet est. Etiam sodales, dolor sit amet aliquam vestibulum, orci lacus consectetur metus, quis laoreet velit ante vel nunc.

Etiam euismod odio eu ornare posuere. Fusce eget interdum urna. Maecenas quis blandit ante, ac vehicula felis. Donec egestas ac dolor ac finibus. Curabitur interdum congue quam, ac tristique lectus suscipit quis. Donec placerat lorem sed ornare rhoncus. Quisque tristique justo in quam fringilla, et suscipit neque laoreet. Quisque maximus aliquam erat rutrum pulvinar. Proin vestibulum, lacus eget molestie lacinia, justo felis venenatis lectus, a tincidunt lorem sapien sit amet mi. Aenean in odio tellus. Vivamus pellentesque leo et quam dictum iaculis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus suscipit felis et cursus iaculis. Cras maximus gravida dictum. Ut arcu sem, aliquam vitae dui in, venenatis tempus massa. Donec hendrerit porta nisl quis pretium.

Vestibulum iaculis posuere ultrices. Maecenas elementum, urna sit amet mollis hendrerit, justo magna maximus lectus, sit amet fermentum elit libero eget nulla. Curabitur malesuada felis justo, nec finibus augue malesuada vel. Morbi lacinia massa mi, non dictum sapien vehicula nec. Sed mi quam, tincidunt ut libero eget, fringilla ultrices mi. Integer mollis semper ante, non congue libero commodo vitae. Nam imperdiet est eu tempor mollis. Vestibulum sodales suscipit massa, vitae rutrum urna vestibulum id. Duis venenatis et velit at gravida. Aliquam lectus diam, tempor eget nisl vitae, commodo venenatis justo. Suspendisse tristique libero sit amet ante varius iaculis. Aenean luctus leo id ex scelerisque hendrerit. In dapibus enim leo, id scelerisque diam gravida non. Donec vestibulum, velit at lacinia aliquet, tellus metus aliquet neque, quis posuere ex nisl sit amet eros.

Sed ultrices pharetra dui, quis fringilla quam varius molestie. Curabitur non sem pellentesque, rhoncus ligula a, tincidunt sem. Morbi nec nunc porta, sodales lorem non, egestas ligula. Etiam venenatis tellus dolor, gravida suscipit urna suscipit ut. Nulla et libero ac nisl porta sodales. Morbi auctor elit ut augue mollis, id tempus augue elementum. Nulla scelerisque auctor nibh, ac ultricies leo malesuada sit amet. In turpis orci, varius eget orci eget, finibus euismod augue. In eget felis tempus, dignissim velit et, fermentum tellus. Sed mollis pretium varius.
	"""
	conclusion = "Alan Turing's immense contributions to computer science and his pivotal role in World War II mark him as one of the most impactful figures of the 20th century. His legacy serves as an inspiration for innovation and a stark reminder of the importance of societal acceptance and justice."
	image_url = "https://assets.sportheroesgroup.com/articles/56faabbd475c1fed4a3d3539/alan-turing-running-1080x675.jpg?v=1658831997"  # replace with the actual image URL

	post = Post(
		title=title,
		excerpt=excerpt,
		header=header,
		introduction=introduction,
		body=body,
		conclusion=conclusion,
		date_posted=datetime.utcnow(),
		image_url=image_url
	)

	# Add the post to the session
	db.session.add(post)

	title = "Erik Satie: The Eccentric Impressionist"
	excerpt = "Exploring the life, works, and peculiarities of the French composer and pianist Erik Satie."
	header = "Unraveling the Enigma of Erik Satie: The Revolutionary in Music"
	introduction = "This article uncovers the intriguing journey of Erik Satie, his unique approach to composition, and his profound influence on 20th-century music."
	body = """


Cras consectetur malesuada ornare. Mauris in erat nisl. Donec vitae elit sit amet libero tempus mollis. Sed finibus laoreet tincidunt. Nulla iaculis mattis condimentum. Mauris ac enim leo. In hac habitasse platea dictumst. Sed semper pellentesque finibus. Sed hendrerit dapibus elit, eget condimentum enim rutrum ac. In hac habitasse platea dictumst. Mauris quis pretium orci. Sed scelerisque dapibus sapien, sed lobortis metus interdum at. Integer tellus justo, blandit sit amet lorem non, molestie scelerisque sem.

Proin quis massa sit amet ipsum gravida posuere. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nullam ipsum urna, tempor in tincidunt eget, dapibus in nisi. Nullam viverra imperdiet erat a vestibulum. Nulla lobortis, lacus non condimentum lobortis, lacus enim bibendum felis, tempor iaculis leo dolor in nunc. Mauris maximus tempus est, eget euismod eros. Quisque volutpat ultrices risus, vel sodales tellus maximus quis. In volutpat nunc lorem.

Pellentesque at dapibus lectus. Vestibulum gravida nunc augue, sed accumsan diam ultrices a. Etiam pretium sagittis nisi et feugiat. Integer gravida tristique metus, sed iaculis mi condimentum id. Aliquam sapien nulla, mattis vel suscipit non, cursus sed erat. Ut tortor dolor, bibendum vitae ligula at, consectetur lobortis mi. Praesent id suscipit massa.

Vivamus faucibus, sapien at porttitor condimentum, sapien sem ultricies lacus, a volutpat justo velit eu dui. Nullam rhoncus risus eget ullamcorper pharetra. Phasellus tincidunt sagittis suscipit. Donec blandit metus vitae sapien condimentum, ac porta arcu aliquam. Suspendisse potenti. Pellentesque auctor mi odio, in bibendum enim finibus et. Nulla non ligula a ante fringilla auctor. Nam neque ante, interdum viverra eros nec, malesuada efficitur risus. Nulla facilisi.
	"""
	conclusion = "Erik Satie, with his eccentric personality and innovative musical style, stands as a testament to the power of individuality in art. His legacy in the world of music serves as a reminder that breaking convention can lead to the creation of timeless masterpieces."
	image_url = "https://backoffice.staging.lalettredumusicien.fr/articles/articlelesmorceauxenformedepoirederiksatie0320230935520000.jpeg"  # replace with the actual image URL

	post = Post(
		title=title,
		excerpt=excerpt,
		header=header,
		introduction=introduction,
		body=body,
		conclusion=conclusion,
		date_posted=datetime.utcnow(),
		image_url=image_url
	)

	# Add the post to the session
	db.session.add(post)

	title = "Cartier: The Crown Jeweler"
	excerpt = "The captivating history, renowned craftsmanship, and pioneering innovations of the distinguished French luxury goods company, Cartier."
	header = "Cartier: The Pioneering Luxury Brand That Shaped The World Of Jewelry"
	introduction = "This post illuminates the enduring legacy of Cartier, its noteworthy contributions to jewelry " \
				   "design, and the timeless appeal of its exquisite creations."
	body = """


Ut eu pulvinar orci. Cras congue erat nec nunc sagittis, eget laoreet ligula sagittis. Suspendisse potenti. Phasellus luctus auctor lacus, eu bibendum velit tristique at. Proin tempor consectetur sollicitudin. Phasellus turpis ante, feugiat sed luctus et, sagittis non ligula. Sed lobortis nec mi vitae ornare. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque a aliquam eros.

Morbi ac quam turpis. Nunc rhoncus lobortis neque, at blandit ante ultricies sit amet. Donec sed luctus dui. Pellentesque massa eros, maximus nec lacinia et, efficitur nec leo. Suspendisse orci nunc, maximus nec pretium convallis, imperdiet eget odio. Aenean ut tellus purus. Duis scelerisque, turpis sed ullamcorper suscipit, tortor nunc sollicitudin odio, vel tincidunt mauris nunc ac justo.

Pellentesque libero enim, posuere non pulvinar scelerisque, pulvinar faucibus justo. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Pellentesque pretium urna ultricies odio congue vestibulum. Suspendisse interdum semper sapien ornare consectetur. Nunc sollicitudin sed lorem vel fermentum. Proin et imperdiet lectus. Suspendisse a arcu vel metus semper varius.

Ut eleifend pharetra vehicula. Curabitur eget ultricies tellus, ac finibus sem. Integer sed interdum sapien. Suspendisse vel lacus nisl. Quisque id hendrerit nulla, vel malesuada nisi. Suspendisse nisl elit, bibendum in magna ac, aliquet vehicula lacus. Ut non leo bibendum sapien dignissim porta.
	"""
	conclusion = "Cartier, with its rich history and passion for craftsmanship, continues to be a trailblazer in the world of luxury goods. Its enduring appeal and commitment to quality have cemented its status as one of the world's leading luxury brands."
	image_url = "https://cf.shopee.co.id/file/9741afc53e5683ad1c7a9f846e6da8a6"  # replace with the actual image URL

	post = Post(
		title=title,
		excerpt=excerpt,
		header=header,
		introduction=introduction,
		body=body,
		conclusion=conclusion,
		date_posted=datetime.utcnow(),
		image_url=image_url
	)

	# Add the post to the session
	db.session.add(post)

	# db.session.query(Project).delete()
	# Commit the changes
	db.session.commit()
