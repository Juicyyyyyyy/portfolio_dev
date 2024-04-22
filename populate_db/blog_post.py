from populate_db import app, kill_db, db, Post, datetime

with app.app_context():
	db.session.query(Post).delete()

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

	title = "Arrays vs Lists : the differences"

	body = """
	# Understanding Lists and Arrays Across Programming Languages with C Examples

In programming, the choice between using lists and arrays can significantly impact both the functionality and performance of an application. While the terminology can vary between languages, the core concepts remain largely the same. This blog post explores these two essential data structures—arrays and lists—across various programming languages, emphasizing their differences and uses. We'll illustrate these concepts with examples in the C programming language.

## What is an Array?

An array is a fundamental data structure in many programming languages, characterized by its fixed size and ability to store elements of the same type at contiguous memory locations. Arrays are especially popular in low-level programming due to their efficient memory usage and quick access times.

### Key Features of Arrays:
- **Fixed Size:** The number of elements an array can store is set at the time of its declaration and cannot be changed.
- **Homogeneous Data Types:** All elements in an array must be of the same type.
- **Efficient Access:** Arrays allow for rapid access to their elements via direct indexing, which is computationally inexpensive.

In languages like C, arrays are a cornerstone of system programming, used for their speed and direct memory access.

## What is a List?

Unlike arrays, lists are more dynamic and can expand or contract as needed. Lists do not require continuous memory allocation, and they can typically store elements of various types, though in strongly typed languages like C++, Java, or C#, elements generally need to be of the same generic type or inherit from the same base class.

### Key Features of Lists:
- **Dynamic Sizing:** Lists can adjust their size automatically as elements are added or removed.
- **Potentially Heterogeneous:** In some languages, lists can hold different types of data.
- **Flexible Management:** Lists often come with built-in methods for easy manipulation of data, such as insertion, deletion, and traversal functionalities.

In high-level languages, lists are implemented with complex data structures like linked lists, array lists, or other types of collections.

## Arrays vs. Lists in C

In C, arrays are part of the core language, offering efficient storage and data access. Lists, however, are not built-in and must be implemented manually using more complex data structures like linked lists. Here’s a look at how these two structures might be implemented and utilized in C:

### Array Example in C:

```c
#include <stdio.h>

int main() {
    int a[4] = {1, 2, 3, 4};  // Declaration of an array of integers

    // Accessing array elements
    printf("First element of array: %d\n", a[0]);  // Outputs: 1

    // Arrays are fixed size
    // a[4] = 5;  // Uncommenting this would lead to a runtime error

    return 0;
}
```

### List Example in C (Using a Linked List):

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Function to add a node at the beginning of the list
void push(Node** head_ref, int new_data) {
    Node* new_node = (Node*) malloc(sizeof(Node));
    new_node->data = new_data;
    new_node->next = (*head_ref);
    (*head_ref) = new_node;
}

// Function to print the list
void printList(Node* node) {
    while (node != NULL) {
        printf("%d ", node->data);
        node = node->next;
    }
}

int main() {
    Node* head = NULL;

    push(&head, 4);
    push(&head, 3);
    push(&head, 2);
    push(&head, 1);

    printf("Created Linked List: ");
    printList(head);
    return 0;
}
```

## Conclusion

Arrays offer straightforward, efficient storage and access for fixed-size collections of homogeneous elements, making them ideal for performance-critical applications. Lists, on the other hand, provide flexibility and ease of manipulation, which is beneficial in scenarios where the size of the data set changes dynamically. Choosing the right data structure depends on the specific requirements of your application, such as performance considerations, type safety, and memory management."""
	image_url = "../../static/img/blog_posts/list_vs_array.png"

	post4 = Post(
		title=title,
		content=body,
		date_posted="2024-04-23",
		image_url=image_url
	)

	# Add the post to the session
	db.session.add(post2)
	db.session.add(post3)
	db.session.add(post4)

	# db.session.query(Project).delete()
	# Commit the changes
	db.session.commit()
