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
