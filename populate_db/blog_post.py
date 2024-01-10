from populate_db import app, kill_db, db, Post, datetime

with app.app_context():
	db.session.query(Post).delete()
	title = "Edward Hopper: Capturing the Essence of Solitude in American Art"

	body = """

	Curabitur consequat nec neque sit amet dapibus. Nulla facilisi. Donec convallis eros nec tempor pretium. Sed cursus, justo eget aliquam luctus, urna urna convallis enim, sit amet condimentum odio nisi sit amet erat. Mauris cursus nulla leo, sit amet aliquet lorem scelerisque at. Nam ac enim nulla. Suspendisse pellentesque eros sit amet justo sagittis tempor. Nunc vulputate viverra ante, in interdum mauris. Fusce condimentum euismod dolor. Lorem ipsum dolor sit amet, consectetur adipiscing elit.

	Morbi vel feugiat leo. Vestibulum maximus velit risus, ac sollicitudin sem lobortis ut. Curabitur ornare odio tellus, vitae tristique mauris maximus in. Mauris cursus nulla orci, a dignissim orci venenatis et. Nam ac sapien eu nisl tincidunt finibus. Quisque vel ultrices lorem. Maecenas eget finibus libero. Quisque sed nisi ac est vehicula commodo id sit amet eros. Quisque ut iaculis ipsum.

	Donec sit amet orci faucibus ante eleifend commodo sit amet vel eros. Mauris eu sem placerat tellus facilisis mattis. Proin facilisis magna id mauris tristique sagittis. Praesent sodales pulvinar erat vitae dictum. Phasellus tortor augue, rhoncus ut sollicitudin sed, scelerisque nec dui. Sed lobortis et lacus vitae volutpat. Quisque at sollicitudin leo, vitae aliquam ipsum. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Ut ut justo ac magna elementum rhoncus eget at nisi. Suspendisse ut mauris a enim gravida viverra. Donec id cursus diam. Integer at risus at elit vestibulum malesuada. Nunc gravida condimentum vestibulum.

	Proin eget nunc felis. Fusce luctus maximus nulla sit amet accumsan. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec blandit mauris et ligula ornare, nec tristique risus scelerisque. Etiam egestas tempor libero. Aliquam ac pharetra erat. Nullam et semper massa. Maecenas eget ipsum nisl. Curabitur non iaculis nulla, sed consectetur tortor. Maecenas blandit, nulla finibus pharetra sagittis, felis nunc dignissim libero, a commodo sapien felis a quam. Nunc non quam odio. Suspendisse potenti. Maecenas eu diam vel lacus imperdiet consequat. Cras quis convallis nulla. Proin ut sapien a nunc facilisis commodo quis eu arcu. Donec venenatis laoreet magna, et accumsan dolor hendrerit vitae.
		"""
	conclusion = "From his early days in New York to his lasting impact on global art, Edward Hopper's journey is a tribute to the enduring power of art to encapsulate human emotions and experiences. His work, a blend of realism and emotion, continues to inspire, educate, and move audiences today."
	image_url = "https://m.media-amazon.com/images/I/A1zF6cUJxnL._AC_UF1000,1000_QL80_.jpg"  # replace with the actual image URL

	post = Post(
		title=title,
		content=body,
		date_posted=datetime.utcnow(),
		image_url=image_url
	)

	# Add the post to the session
	db.session.add(post)

	title = "Alan Turing: Unveiling the Architect of the Modern Computer"
	body = """

	Suspendisse vulputate viverra sem. Nulla cursus quis enim sit amet condimentum. Suspendisse at eros vehicula, ultrices justo id, rutrum risus. Nam finibus ante in sollicitudin lobortis. Quisque id elit eget nulla vestibulum ultrices. Sed pellentesque, massa sit amet auctor tincidunt, lacus est posuere velit, ac interdum nulla leo sit amet est. Etiam sodales, dolor sit amet aliquam vestibulum, orci lacus consectetur metus, quis laoreet velit ante vel nunc.

	Etiam euismod odio eu ornare posuere. Fusce eget interdum urna. Maecenas quis blandit ante, ac vehicula felis. Donec egestas ac dolor ac finibus. Curabitur interdum congue quam, ac tristique lectus suscipit quis. Donec placerat lorem sed ornare rhoncus. Quisque tristique justo in quam fringilla, et suscipit neque laoreet. Quisque maximus aliquam erat rutrum pulvinar. Proin vestibulum, lacus eget molestie lacinia, justo felis venenatis lectus, a tincidunt lorem sapien sit amet mi. Aenean in odio tellus. Vivamus pellentesque leo et quam dictum iaculis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus suscipit felis et cursus iaculis. Cras maximus gravida dictum. Ut arcu sem, aliquam vitae dui in, venenatis tempus massa. Donec hendrerit porta nisl quis pretium.

	Vestibulum iaculis posuere ultrices. Maecenas elementum, urna sit amet mollis hendrerit, justo magna maximus lectus, sit amet fermentum elit libero eget nulla. Curabitur malesuada felis justo, nec finibus augue malesuada vel. Morbi lacinia massa mi, non dictum sapien vehicula nec. Sed mi quam, tincidunt ut libero eget, fringilla ultrices mi. Integer mollis semper ante, non congue libero commodo vitae. Nam imperdiet est eu tempor mollis. Vestibulum sodales suscipit massa, vitae rutrum urna vestibulum id. Duis venenatis et velit at gravida. Aliquam lectus diam, tempor eget nisl vitae, commodo venenatis justo. Suspendisse tristique libero sit amet ante varius iaculis. Aenean luctus leo id ex scelerisque hendrerit. In dapibus enim leo, id scelerisque diam gravida non. Donec vestibulum, velit at lacinia aliquet, tellus metus aliquet neque, quis posuere ex nisl sit amet eros.

	Sed ultrices pharetra dui, quis fringilla quam varius molestie. Curabitur non sem pellentesque, rhoncus ligula a, tincidunt sem. Morbi nec nunc porta, sodales lorem non, egestas ligula. Etiam venenatis tellus dolor, gravida suscipit urna suscipit ut. Nulla et libero ac nisl porta sodales. Morbi auctor elit ut augue mollis, id tempus augue elementum. Nulla scelerisque auctor nibh, ac ultricies leo malesuada sit amet. In turpis orci, varius eget orci eget, finibus euismod augue. In eget felis tempus, dignissim velit et, fermentum tellus. Sed mollis pretium varius.
		"""

	image_url = "https://assets.sportheroesgroup.com/articles/56faabbd475c1fed4a3d3539/alan-turing-running-1080x675.jpg?v=1658831997"  # replace with the actual image URL

	post = Post(
		title=title,
		content=body,
		date_posted=datetime.utcnow(),
		image_url=image_url
	)

	# Add the post to the session
	db.session.add(post)

	body = """


	Cras consectetur malesuada ornare. Mauris in erat nisl. Donec vitae elit sit amet libero tempus mollis. Sed finibus laoreet tincidunt. Nulla iaculis mattis condimentum. Mauris ac enim leo. In hac habitasse platea dictumst. Sed semper pellentesque finibus. Sed hendrerit dapibus elit, eget condimentum enim rutrum ac. In hac habitasse platea dictumst. Mauris quis pretium orci. Sed scelerisque dapibus sapien, sed lobortis metus interdum at. Integer tellus justo, blandit sit amet lorem non, molestie scelerisque sem.

	Proin quis massa sit amet ipsum gravida posuere. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nullam ipsum urna, tempor in tincidunt eget, dapibus in nisi. Nullam viverra imperdiet erat a vestibulum. Nulla lobortis, lacus non condimentum lobortis, lacus enim bibendum felis, tempor iaculis leo dolor in nunc. Mauris maximus tempus est, eget euismod eros. Quisque volutpat ultrices risus, vel sodales tellus maximus quis. In volutpat nunc lorem.

	Pellentesque at dapibus lectus. Vestibulum gravida nunc augue, sed accumsan diam ultrices a. Etiam pretium sagittis nisi et feugiat. Integer gravida tristique metus, sed iaculis mi condimentum id. Aliquam sapien nulla, mattis vel suscipit non, cursus sed erat. Ut tortor dolor, bibendum vitae ligula at, consectetur lobortis mi. Praesent id suscipit massa.

	Vivamus faucibus, sapien at porttitor condimentum, sapien sem ultricies lacus, a volutpat justo velit eu dui. Nullam rhoncus risus eget ullamcorper pharetra. Phasellus tincidunt sagittis suscipit. Donec blandit metus vitae sapien condimentum, ac porta arcu aliquam. Suspendisse potenti. Pellentesque auctor mi odio, in bibendum enim finibus et. Nulla non ligula a ante fringilla auctor. Nam neque ante, interdum viverra eros nec, malesuada efficitur risus. Nulla facilisi.
		"""
	image_url = "https://backoffice.staging.lalettredumusicien.fr/articles/articlelesmorceauxenformedepoirederiksatie0320230935520000.jpeg"  # replace with the actual image URL

	post = Post(
		title=title,
		content=body,
		date_posted=datetime.utcnow(),
		image_url=image_url
	)

	# Add the post to the session
	db.session.add(post)

	title = "Cartier: The Crown Jeweler"
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
		content=body,
		date_posted=datetime.utcnow(),
		image_url=image_url
	)

	# Add the post to the session
	db.session.add(post)

	# db.session.query(Project).delete()
	# Commit the changes
	db.session.commit()
