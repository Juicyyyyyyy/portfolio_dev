from populate_db import app, kill_db, db, Post, datetime

with app.app_context():
	db.session.query(Post).delete()
	title = "De simples étudiants en BTS à pionniers d'un marché 🚀"

	body = """

## Voici notre histoire :

Dès la sortie de la première version de Chat GPT, j'ai été immédiatement captivé par ce formidable outil. Un univers entier de possibilités s'est dévoilé à moi. J'ai tout de suite vu cette innovation comme un outil à grand potentiel de productivité et donc lucratif.

Très vite, j'ai cherché à utiliser cet outil de la meilleure des manières possibles pour augmenter largement ma productivité en automatisant des tâches tout en gardant un travail de la même qualité. Par la même occasion, j'ai découvert le "prompt engineering", un mot compliqué qui signifie simplement le fait d'optimiser les instructions fournies à Chat GPT pour obtenir des réponses de la meilleure qualité possible.

À partir de ce moment, j'eus une idée dont je fis part à mon fidèle associé et ami, Tahirou Laouan Magagi. Pourquoi ne pas utiliser la puissance de GPT pour automatiser le processus de création de sites internet dans le but de les vendre par la suite ?

Ce à quoi Tahirou a surenchéri en proposant une idée encore plus innovante. Au lieu de se placer en tant que simple vendeur, pourquoi ne pas viser plus loin et devenir le vendeur des vendeurs? Pourquoi ne pas vendre la pioche plutôt que l'or ?

Au début, cela me paraissait complètement irréalisable, bien trop ambitieux pour de simples étudiants dans la vingtaine, découvrant à peine la vie adulte et le milieu de l'entrepreneuriat. Mais, aimant le risque et l'aventure, j'ai accepté son idée et je l'ai suivi dans cette folle aventure entrepreneuriale.

Après des mois de dévouement, jonglant entre nos cours, nos jobs en alternance et notre projet, nous sommes fiers d'annoncer la naissance de [justclickbuild.com](https://justclickbuild.com) : le premier générateur de sites web 100% alimenté par IA et no-code ! 🚀

### OFFRE DE LANCEMENT

Pour célébrer ce lancement, recevez 25€ de crédit. Générez et personnalisez votre site avec notre outil no-code. Essayez sur [justclickbuild.com](https://justclickbuild.com) et laissez vous surprendre par la magie de l'IA. 🎉

Envie d'en savoir plus, d'échanger avec notre équipe, ou de partager vos retours? 👉 Rejoignez-nous dès maintenant sur notre serveur [Discord](https://discord.gg/8hbSFXSTHu)


		"""
	image_url = "../../static/img/jcb_banner.png"

	post1 = Post(
		title=title,
		content=body,
		date_posted=datetime.utcnow(),
		image_url=image_url
	)

	title = "Logarithmes Naturels démystifiés"

	body = """

	# Introduction
Lorsqu'on parle de croissance exponentielle, il est commun de penser à quelque chose qui grandit très rapidement. Cependant, la croissance exponentielle désigne un type spécifique de croissance, distincte de la croissance polynomiale, telle que celle décrite par les fonctions \(x^2\), \(x^3\), ou \(x^{300}\). Ces dernières, bien qu'accélérant rapidement, ne se comparent pas à la vitesse de la croissance exponentielle, qui est proportionnelle à la taille de la population ou du montant en question. 

# Le Principe de la Croissance Exponentielle
La croissance exponentielle s'observe dans de nombreux phénomènes naturels et financiers, tels que la reproduction des lapins ou l'accumulation des intérêts sur un montant d'argent. Cette croissance n'est pas seulement rapide, mais sa vitesse augmente proportionnellement à sa grandeur actuelle.

# Intérêt Composé et le Nombre \( e \)
Prenons un exemple avec un compte bancaire offrant un intérêt annuel de 100 %. Si vous déposez un dollar, ce montant deviendra deux dollars en un an. Cependant, les intérêts ne sont pas seulement calculés à la fin de l'année. En réalité, ils sont souvent calculés plus fréquemment, ce qui accélère la croissance de votre argent.

# Expérimentation avec le Taux de Composition
Supposons que l'intérêt soit calculé deux fois par an, chaque semestre. Dans ce cas, votre dollar initial deviendra 2.25 dollars à la fin de l'année. Si l'intérêt est calculé chaque mois, le montant atteint sera environ 2.61 dollars. Ce montant continue d'augmenter avec la fréquence de calcul de l'intérêt, approchant une limite à mesure que la fréquence de calcul devient infiniment grande.

# Découverte du Nombre \( e \)
Lorsque l'intérêt est calculé en continu, c'est-à-dire à une fréquence infinie, le montant final converge vers une valeur spécifique, environ 2.71828, connue sous le nom de \( e \), le nombre d'Euler. Ce nombre est fondamental en mathématiques et en sciences, car il décrit des taux de croissance ou de décroissance proportionnels à la grandeur actuelle d'un système.

# Signification du Nombre \( e \)
Le nombre \( e \) apparaît naturellement dans de nombreux contextes, y compris la croissance des populations, la décomposition radioactive, et le refroidissement des objets. Il représente un taux de croissance ou de décroissance proportionnel à la taille actuelle de l'entité observée.

# Conclusion
Le nombre \( e \) n'est pas simplement un nombre arbitraire; il émerge naturellement de la structure du monde autour de nous, illustrant des principes de croissance et de décroissance proportionnels. Que ce soit en finance, en biologie, ou en physique, \( e \) joue un rôle crucial dans notre compréhension des phénomènes naturels et artificiels.

			"""
	image_url = "../../static/img/blog_posts/log_nat.png"

	post2 = Post(
		title=title,
		content=body,
		date_posted=datetime.utcnow(),
		image_url=image_url
	)

	# Add the post to the session
	db.session.add(post1)
	db.session.add(post2)

	# db.session.query(Project).delete()
	# Commit the changes
	db.session.commit()
