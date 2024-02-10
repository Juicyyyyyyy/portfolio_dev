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
	conclusion = "From his early days in New York to his lasting impact on global art, Edward Hopper's journey is a tribute to the enduring power of art to encapsulate human emotions and experiences. His work, a blend of realism and emotion, continues to inspire, educate, and move audiences today."
	image_url = "../../static/img/jcb_banner.png"  # replace with the actual image URL

	post = Post(
		title=title,
		content=body,
		date_posted=datetime.utcnow(),
		image_url=image_url
	)

	# Add the post to the session
	db.session.add(post)

	# db.session.query(Project).delete()
	# Commit the changes
	db.session.commit()
