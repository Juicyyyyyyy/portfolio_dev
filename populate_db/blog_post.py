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
		date_posted="2024-04-16 13:12:13",
		image_url=image_url
	)

	title = "Vocabulary of Object-Oriented Programming (OOP)"

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
		date_posted="2024-04-18",
		image_url=image_url
	)

	title = "Arrays vs Lists: the differences"

	body = """
In programming, the choice between using lists and arrays can significantly impact both the functionality and performance of an application. While the terminology can vary between languages, the core concepts remain largely the same. This blog post explores these two essential data structures—arrays and lists—across various programming languages, emphasizing their differences and uses.

## What is an Array?

An array is a fundamental data structure in many programming languages, characterized by its fixed size and ability to store elements of the same type at contiguous memory locations. Arrays are especially popular in low-level programming due to their efficient memory usage and quick access times.

## Key Features of Arrays:
- **Fixed Size:** The number of elements an array can store is set at the time of its declaration and cannot be changed.
- **Homogeneous Data Types:** All elements in an array must be of the same type.
- **Efficient Access:** Arrays allow for rapid access to their elements via direct indexing, which is computationally inexpensive.

In languages like C, arrays are a cornerstone of system programming, used for their speed and direct memory access.

## What is a List?

Unlike arrays, lists are more dynamic and can expand or contract as needed. Lists do not require continuous memory allocation, and they can typically store elements of various types, though in strongly typed languages like C++, Java, or C#, elements generally need to be of the same generic type or inherit from the same base class.

## Key Features of Lists:
- **Dynamic Sizing:** Lists can adjust their size automatically as elements are added or removed.
- **Potentially Heterogeneous:** In some languages, lists can hold different types of data.
- **Flexible Management:** Lists often come with built-in methods for easy manipulation of data, such as insertion, deletion, and traversal functionalities.

In high-level languages, lists are implemented with complex data structures like linked lists, array lists, or other types of collections.

## Conclusion

Arrays offer straightforward, efficient storage and access for fixed-size collections of homogeneous elements, making them ideal for performance-critical applications. Lists, on the other hand, provide flexibility and ease of manipulation, which is beneficial in scenarios where the size of the data set changes dynamically. Choosing the right data structure depends on the specific requirements of your application, such as performance considerations, type safety, and memory management."""
	image_url = "../../static/img/blog_posts/list_vs_array.png"

	post4 = Post(
		title=title,
		content=body,
		date_posted="2024-04-21",
		image_url=image_url
	)

	title = "Linked Lists: An Essential Data Structure"

	body = """
Linked lists are a fundamental data structure in computer science, often used for efficiently managing collections of elements. Unlike arrays, which store elements in contiguous memory locations, linked lists consist of nodes that are connected using pointers. This structure allows for dynamic memory utilization and offers an efficient way to insert and delete elements. In this blog post, we'll explore the concept of linked lists, their types, advantages, and common applications.	

## What is a Linked List?

A linked list is a sequence of nodes, where each node contains a piece of data and a reference (or link) to the next node in the sequence. This simple yet powerful structure allows for efficient insertion and deletion of elements as it does not require the elements to be contiguous in memory.

## Types of Linked Lists

There are several types of linked lists, each serving different purposes:

![Single and double linked list](../../static/img/blog_posts/linked_lists_illustration.png)

1. **Singly Linked List**: This is the simplest type of linked list, where each node contains data and a single link to the next node. Navigation is only possible in one direction, from the start to the end of the list.

2. **Doubly Linked List**: In a doubly linked list, each node has two links: one pointing to the next node and the other to the previous node. This bidirectional structure allows for easier navigation (forward and backward through the list).

3. **Circular Linked List**: A circular linked list can be either singly or doubly linked but with a twist: the last node in the sequence points back to the first node, making the list circular. This is useful for applications that require a continuous, cyclic access to the elements (e.g., a round-robin scheduler).

## Advantages of Linked Lists

Linked lists offer several benefits over other data structures like arrays, including:

- **Dynamic Size**: The size of a linked list can grow or shrink dynamically, which is particularly advantageous in scenarios where the number of elements is not known in advance or can change frequently.

- **Efficient Operations**: Insertions and deletions at any position in a linked list can be done in constant time if the position is known (i.e., you have a pointer to the node before the place of insertion or deletion). This is more efficient than the same operations in an array, which require shifting elements to maintain continuity.

- **Memory Efficient**: Since linked lists do not require memory in contiguous blocks, they can make more efficient use of available memory. This avoids the overhead of reserving large blocks of memory, which might not be fully utilized.

## Applications of Linked Lists

Linked lists are used in many areas of computer science and software development. Some common applications include:

- **Implementing other data structures**: Structures like stacks, queues, and other abstract data types can be efficiently implemented using linked lists.
  
- **Dynamic memory allocation**: The operating system may use linked lists to keep track of free blocks of memory, helping manage allocations and deallocations dynamically.
  
- **Performance-sensitive applications**: In applications where performance is critical, linked lists can provide faster access and manipulation compared to other data structures that require reorganizing or reallocating memory.

## Conclusion

Linked lists are a versatile and essential part of the data structure toolkit, offering flexible and efficient management of data. They shine in scenarios where the amount of data varies dynamically and where quick insertion and deletion are crucial. Understanding linked lists and their applications can significantly enhance one’s ability to design and implement efficient systems."""
	image_url = "../../static/img/blog_posts/linked_lists.png"

	post5 = Post(
		title=title,
		content=body,
		date_posted="2024-04-22",
		image_url=image_url
	)

	title = "Big O Notation: The Language of Algorithm Efficiency"

	body = """
In the world of programming and computer science, Big O notation is a fundamental concept that helps engineers and developers understand the performance of their algorithms. Whether you're a seasoned developer, a student learning computer science, or just a tech enthusiast, getting to grips with Big O notation can significantly sharpen your understanding of how algorithms work and their implications on performance. This blog post will demystify Big O notation and explain its importance in designing efficient algorithms.

## What is Big O Notation?

Big O notation is a mathematical representation used to describe the efficiency of an algorithm in terms of time (execution time) and space (memory usage). Specifically, it focuses on how the runtime or space requirements grow as the size of the input data increases. The notation helps predict the worst-case scenario for an algorithm, providing a high-level understanding of its scalability and efficiency.

## How Big O Notation Works

To explain how Big O notation works, consider that you have a function or an algorithm that processes a set of data. The "O" in Big O stands for "order of," indicating the order of growth of the function. This growth rate provides insight into how well an algorithm will scale as the size of its input data increases.

Here are some common Big O notations and what they signify:

- **O(1) – Constant Time**: An algorithm is said to run in constant time when its performance does not depend on the size of the input data. For example, accessing any element in an array by index is an O(1) operation.

- **O(log n) – Logarithmic Time**: This denotes that the algorithm’s execution time increases logarithmically as the input size increases. A typical example is binary search, which halves the search space with each step.

- **O(n) – Linear Time**: The execution time increases linearly with the input size. If you need to scan each element in a list once, this is a linear time complexity, or O(n).

- **O(n log n) – Log-linear Time**: This is more efficient than quadratic time but less efficient than linear time. Many efficient sorting algorithms, such as mergesort and heapsort, have log-linear time complexity.

- **O(n^2) – Quadratic Time**: This occurs when the execution time is proportional to the square of the input size. Algorithms with nested loops over the data typically fall into this category, such as bubble sort or insertion sort.

- **O(2^n) – Exponential Time**: The execution time doubles with each addition to the input data set. Algorithms that solve problems by computing all combinations of certain data are often exponential.

- **O(n!) – Factorial Time**: The execution time grows factorially based on the size of the input data. An example is solving the traveling salesman problem via a brute-force search.

## Why Big O Notation Matters

Understanding the Big O notation of an algorithm is crucial for several reasons:

1. **Performance Prediction**: Big O notation allows developers to predict how algorithms will perform as data volume grows, which is essential for applications dealing with large datasets.

2. **Algorithm Comparison**: It provides a clear basis for comparing the efficiency of different algorithms and choosing the most appropriate one for a given problem and data size.

3. **System Scalability**: Knowing the time or space complexity of algorithms helps in designing systems that scale well with increasing data or user base.

4. **Resource Management**: Efficient algorithms can help in better resource management, reducing costs associated with computing power and storage.

## Conclusion

Big O notation is more than just theoretical knowledge; it's a practical tool that helps in making informed decisions about which algorithms to use based on their potential impact on system performance and scalability. Whether you are optimizing a database, developing a real-time processing system, or simply sorting a list, understanding Big O notation will enable you to build more efficient and effective solutions."""
	image_url = "../../static/img/blog_posts/big_o_notation.png"

	post6 = Post(
		title=title,
		content=body,
		date_posted="2024-04-23",
		image_url=image_url
	)

	# Add the post to the session
	db.session.add(post2)
	db.session.add(post3)
	db.session.add(post4)
	db.session.add(post5)
	db.session.add(post6)

	# db.session.query(Project).delete()
	# Commit the changes
	db.session.commit()
