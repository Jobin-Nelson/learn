# C Sharp
- Much like Java developed by Microsoft

## Concepts
- **Constructor**
	- Has the same name as the class 
	- Used to instantiate an Object when called with arguments
- **Overloading**
	- Technique for creating same methods (methods and constructors) with different parameters
	- Name + parameters = unique signature
- **Inheritance**
	- 1 or more child classes receiving fields, methods, etc from a common parent class
- **Polymorphism**
	- Greek word that means to "have many forms"
	- Objects can be identified by more than one type
	- Eg: A Dog is also: Canine, Animal and Organism
- **Generic**
	- Not a specific to a particular type of data
	- add <T> to: classes, methods, fields etc
	- allows code reusability for different data types
- **Threading**
	- using System.Threading;
	- We can use multiple threads to perform different tasks of our program at the same time
	- Current thread running is main thread

## Keywords
- **Static**
	- Modifier to declare a static member
	- This member belongs to the class itself rather than to any specific object
- **Abstract**
	- Modifier that indicates missing components or incomplete implementation
	- Abstract classes are not instantiable
- **Virtual**
	- A virtual method is created in base class which can be overriden in the derived class
- **Override**
	- Provides a new version of method inherited from parent class
	- Method that is inherited must be: abstract, virtual or already overriden
	- Has the same signature as the parent method
	- Used with ToString() and polymorphism
- **Interfaces**
	- Defines a contract/rule that all classes inheriting from should follow
	- An interfaces declares "What a class should have"
	- An inheriting class defines "How it should do it"
	- Benefits = security + multiple-inheritance 
- **Enums**
	- Special class that contains a set of named integer constants
	- Use enums when you have values that you know will not change
