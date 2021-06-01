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

To avoid creating reference instead of a true copy, use the .copy() method.
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