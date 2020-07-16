## Python Class and Objects
Python is an object oriented programming language. Almost everything in Python is an object with its properties and methods. A Class is like an object constructor, or a "blueprint" for creating objects. ->[classes](https://docs.python.org/3/tutorial/classes.html)
- [01_Creation](https://github.com/krystinli/code_snippet_collection/blob/master/class_objects.md#01_creation) - an example of class
- [02__init__()]()
- [03_solve]()

### 01_Creation
Classes and objects in their simplest form:
```python
# Create a class named MyClass, with a property named x:
class MyClass:
  x = 5

# Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x) # 5
```

### 02__init__()
All classes have a built-in function called __init__() and is always executed when the class is being initiated. Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name) # "John"
print(p1.age) # 36
```

General form 
```python
class ABC:
   def __init__(self,input1,input2...)
      self.input1=input1
      self.input2=input2
   
   def method1(self):
      ...
   
   def method2(self):
      ...
```

The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class. For example, 
```python
class Person:
   def __init__(self, firstname, lastname, age)
      self.firstname = firstname
      self.lastname = lastname
      self.age = age
   
   def greetings(self):
      print("Hello!" + self.firstname)

# call the class
p1 = Person("Butter","Fly",2)
p1.greetings()
```

### 03_solve
- [find-the-torsional-angle](https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem)
