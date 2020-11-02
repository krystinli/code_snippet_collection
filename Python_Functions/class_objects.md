## Class and Objects
Python is an object oriented programming language. Almost everything in Python is an object. 
- Use the `__init__()` function to assign values to object properties. The __init__() function is called automatically every time the class is being used to create a new object.
- The `self` parameter is a reference to the current instance of the class, used to access variables that belongs to the class; it has to be the first parameter of any function in the class.

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
