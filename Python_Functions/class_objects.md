## Class_and_Objects
Python is an object oriented programming language. Almost everything in Python is an object. 
- Use the `__init__()` function to assign values to object properties. The __init__() function is called automatically every time the class is being used to create a new object.
- 

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

>>> hello, ButterFly
```
