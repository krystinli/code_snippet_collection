### duck_typing
- we don't care about type of an object rather only whether it has certain methods or behaviour
```py
# verify if an obj is iterable by checking if it's implementable in iterator protocol:
def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError: 
        return False

isiterable('foo')  >>> True # a str is iterable
isiterable(5) >>> False # an int is not iterable

# this is useful to test input of a given function: (if it's not, convert it to be)
x = (1,2,3)

if not isinstance(x, list) and isiterable(x):
    x = list(x)
x >>> [1, 2, 3]
```

### attributes_and_methods
Objects in Python have 2 things:
- attributes: other Python objects stored inside the class - obj of obj
- methods: functions associated with an object, that have access to the object's internal data
```py
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
   
    def greetings(self):
        print("hello, " + self.firstname + self.lastname + " :)")

# initiate an instance of classs Person
new_person = Person("Butter", "Fly", 2)
new_person.greetings() >>> hello, ButterFly :)
```

### variable_assignment
- When assigning a variable in Python, you're creating a **reference to the object**.
- Assignment is referred to as **binding**, as we are binding a name to an object.
```py
# a and b now actually refers to the same object. 
a = [1,2,3]
b = a

# Updating either a or b updates both of them:
a.append(4)
a >>> [1, 2, 3, 4]
b >>> [1, 2, 3, 4]

# To avoid creating reference instead of a true copy, use the .copy() method.
c = a.copy()
a.append(5)

a >>> [1, 2, 3, 4, 5]
c >>> [1, 2, 3, 4]
```
- When you pass objects as arguments to a function, new **local variables** are created referencing the original objects.
- If you bind a new object to a variable inside a function, that change will not be reflected in the parent scope.
```py
def add_elements(lst, item):
    lst.append(item)

# evaluation
data = [1,2,3]
add_elements(data, 4)
data >>> [1, 2, 3, 4]
```
