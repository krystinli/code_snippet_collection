## Python Class and Objects
Python is an object oriented programming language. Almost everything in Python is an object, with its properties and methods. A Class is like an object constructor, or a "blueprint" for creating objects.

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
