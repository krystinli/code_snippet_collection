## Class and Objects
Python is an object oriented programming language. Almost everything in Python is an object. <br />
- A class is a blueprint for an object.
- An object is always an instance of a class. One class can have many instances.
- Use the `__init__()` function to assign values to object properties. The __init__() function is called automatically every time the class is being used to create a new object.
- The `self` parameter is a reference to the current instance of the class, used to access variables that belongs to the class; it has to be the first parameter of any function in the class.
- When we call a method on an object, Python automatically fills in the first variable, which we call self by convention. This first variable is a reference to the object itself, hence it’s name. We can use this variable to reference other instance variables and functions of this object, like `self.firstname` and `self.greetings()`.

```python
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
   
    def greetings(self):
        print("hello, " + self.firstname + self.lastname)

p1 = Person("Butter", "Fly", 2)
p1.greetings()

>>> "hello, ButterFly"
```

## Method
When a function is part of an object, ie. `greetings()`

## Inheritance
Inheritance is bascially a class of class, allowing us to define a class that inherits all the methods and properties from another class.
- Parent class is the class being inherited from, also called base class.
- Child class is the class that inherits from another class, also called derived class.
- When you add the `__init__()` function, the child class no longer inherits the parent's `__init__()`, unless:

```python

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

p2 = Student("Mike", "Olsen")
p2.greetings()
```

## Super_Init
It makes the child class inherit all the methods and properties from its parent:
- By using the `super()` function, you do not have to use the name of the parent element.

```python
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

p3 = Student("Mike", "Olsen")
p3.greetings()


# Add Properties
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

p4 = Student("Mike", "Olsen")
p4.graduationyear


# or
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

p5 = Student("Mike", "Olsen", 2020)
p5.graduationyear


# Add New Methods in Child Class:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

p6 = Student("Mike", "Olsen", 2020)
p6.welcome()
```
