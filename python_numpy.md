## Numpy
NumPy stands for Numerical Python, and is good for domain of linear algebra, fourier transform, and matrices.
- In Python we have lists that serve the purpose of arrays, but they are slow to process;
- NumPy aims to provide an array object that is up to 50x faster that traditional Python lists;
- Why? NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written in C or C++.

The array object in NumPy is called ndarray.
```py
import numpy as np

arr = np.array([1, 2, 3,])
arr >>> array([1, 2, 3])

type(arr) >>> numpy.ndarray
```
