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
		date_posted="2024-01-27 11:09:49",
		image_url=image_url
	)

	title = "Logarithmes Naturels démystifiés"

	body = """
Lorsqu'on parle de croissance exponentielle, il est commun de penser à quelque chose qui grandit très rapidement. Cependant, la croissance exponentielle désigne un type spécifique de croissance, distincte de la croissance polynomiale, telle que celle décrite par les fonctions \(x^2\), \(x^3\), ou \(x^{300}\). Ces dernières, bien qu'accélérant rapidement, ne se comparent pas à la vitesse de la croissance exponentielle, qui est proportionnelle à la taille de la population ou du montant en question. 

## Le Principe de la Croissance Exponentielle
La croissance exponentielle s'observe dans de nombreux phénomènes naturels et financiers, tels que la reproduction des lapins ou l'accumulation des intérêts sur un montant d'argent. Cette croissance n'est pas seulement rapide, mais sa vitesse augmente proportionnellement à sa grandeur actuelle.

## Intérêt Composé et le Nombre \( e \)
Prenons un exemple avec un compte bancaire offrant un intérêt annuel de 100 %. Si vous déposez un dollar, ce montant deviendra deux dollars en un an. Cependant, les intérêts ne sont pas seulement calculés à la fin de l'année. En réalité, ils sont souvent calculés plus fréquemment, ce qui accélère la croissance de votre argent.

## Expérimentation avec le Taux de Composition
Supposons que l'intérêt soit calculé deux fois par an, chaque semestre. Dans ce cas, votre dollar initial deviendra 2.25 dollars à la fin de l'année. Si l'intérêt est calculé chaque mois, le montant atteint sera environ 2.61 dollars. Ce montant continue d'augmenter avec la fréquence de calcul de l'intérêt, approchant une limite à mesure que la fréquence de calcul devient infiniment grande.

## Découverte du Nombre \( e \)
Lorsque l'intérêt est calculé en continu, c'est-à-dire à une fréquence infinie, le montant final converge vers une valeur spécifique, environ 2.71828, connue sous le nom de \( e \), le nombre d'Euler. Ce nombre est fondamental en mathématiques et en sciences, car il décrit des taux de croissance ou de décroissance proportionnels à la grandeur actuelle d'un système.

## Signification du Nombre \( e \)
Le nombre \( e \) apparaît naturellement dans de nombreux contextes, y compris la croissance des populations, la décomposition radioactive, et le refroidissement des objets. Il représente un taux de croissance ou de décroissance proportionnel à la taille actuelle de l'entité observée.

## Conclusion
Le nombre \( e \) n'est pas simplement un nombre arbitraire; il émerge naturellement de la structure du monde autour de nous, illustrant des principes de croissance et de décroissance proportionnels. Que ce soit en finance, en biologie, ou en physique, \( e \) joue un rôle crucial dans notre compréhension des phénomènes naturels et artificiels.

			"""
	image_url = "../../static/img/blog_posts/log_nat.png"

	post2 = Post(
		title=title,
		content=body,
		date_posted="2024-04-20 13:12:13",
		image_url=image_url
	)

	title = "Understanding the Vocabulary of Object-Oriented Programming (OOP)"

	body = """
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects," which can contain data, in the form of fields (often known as attributes or properties), and code, in the form of procedures (often known as methods). OOP languages are diverse, but they all support the fundamental features that leverage the following key terms and concepts. Understanding these terms is crucial for anyone learning or working with OOP languages like Java, C++, Python, or others.

## 1. Class
A **class** is a blueprint for creating objects. It defines a datatype by bundling data (attributes) and methods that work on the data into a single unit. For instance, a class `Car` might include attributes like `color` and `model`, and methods like `drive()` and `brake()`.

```python
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def drive(self):
        return "This car is driving."
```

## 2. Object
An **object** is an instance of a class. When a class is defined, no memory is allocated until an object is created from the class. Each object has a separate identity and a set of attributes which are defined by the class.

```python
my_car = Car(model="Toyota Camry", color="Blue")
```

## 3. Method
A **method** is a function defined in a class that describes the behaviors of an object. It is where the logic of a class is defined. A method might manipulate the internal state of an object or perform actions related to the object's attributes.

```python
def drive(self):
    return "This car is driving."
```

## 4. Property (Attribute)
**Properties** hold the state of the object, with each object created from a class having its own set of data. Properties are data elements used within a class.

```python
self.model = model
self.color = color
```

## 5. Inheritance
**Inheritance** is a way to form new classes using classes that have already been defined. The new class, known as a derived class, inherits attributes and methods from the existing class, called the base class. This feature promotes code reusability and relationship establishment between objects.

```python
class ElectricCar(Car):
    def __init__(self, model, color, battery_size):
        super().__init__(model, color)
        self.battery_size = battery_size
```

## 6. Encapsulation
**Encapsulation** is the concept of wrapping the data (attributes) and the code acted on the data (methods) together as a single unit. In encapsulation, the data is not accessed directly; it is accessed through the methods present in the class. This helps protect the integrity of the data.

```python
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color
```

## 7. Polymorphism
**Polymorphism** allows methods to do different things based on the object it is acting upon. With polymorphism, a single interface can represent different underlying forms (data types).

```python
def drive(self):
    return "This car is driving quietly." if isinstance(self, ElectricCar) else "This car is driving."
```

## 8. Abstraction
**Abstraction** allows making complex systems simpler by setting aside unnecessary details to focus on features that are crucial for understanding and using the system.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass
```

## 9. Constructor
A **constructor** is a special method called when an object is instantiated. It usually initializes the various properties of the object.

```python
def __init__(self, model, color):
    self.model = model
    self.color = color
```

## 10. Destructor
**Destructor** is a method that is called when an object is destroyed. Its main purpose is resource deallocation and other cleanup necessary for the object being destroyed.

```python
def __del__(self):
    print("Car object is being deleted.")
```

## 11. Interface
An **interface** in Python can be implemented using abstract base classes that define methods that must be created in any subclass.

```python
class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass
```

## 12. Abstract Class
An **abstract class** cannot be instantiated and is used as

 a base class. It can contain both abstract methods and regular methods.

```python
class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass
```

## 13. Composition and Aggregation
**Composition** involves creating classes that contain objects of other classes; **aggregation** uses references to other objects.

```python

class Engine:
    def start(self):
        return "Engine is starting."

class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.engine = Engine()  # Composition

    def start_engine(self):
        return self.engine.start()
```

By mastering these foundational concepts, you’ll be well-prepared to dive into object-oriented programming and effectively design applications using its principles. Whether you are a beginner or looking to refresh your knowledge, these concepts form the backbone of any robust OOP-based application.
				"""
	image_url = "../../static/img/blog_posts/oop_vocabulary.png"

	post3 = Post(
		title=title,
		content=body,
		date_posted="2024-04-21",
		image_url=image_url
	)

	# Add the post to the session
	db.session.add(post1)
	db.session.add(post2)
	db.session.add(post3)

	# db.session.query(Project).delete()
	# Commit the changes
	db.session.commit()
