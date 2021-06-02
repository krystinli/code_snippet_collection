## Numpy
NumPy stands for Numerical Python, and is good for domain of linear algebra, fourier transform, and matrices.
- In Python we have `lists` that serve the purpose of arrays, but they are slow to process;
- NumPy aims to provide an array object that is up to 50x faster that traditional Python lists;
- Why? NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written in C or C++.

The array object in NumPy is called **ndarray**.
```py
import numpy as np

arr = np.array([1, 2, 3,])
arr >>> array([1, 2, 3])

type(arr) >>> numpy.ndarray
```

### Dimension
```py
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
arr_0 = np.array(5)
arr_0 >>> array(5)

# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
arr_1 = np.array([1, 2, 3,])
arr_1 >>> array([1, 2, 3])

# An array that has 1-D arrays as its elements is called a 2-D array. These are often used to represent matrix or 2nd order tensors.
arr_2 = np.array([[1, 2, 3], [4, 5, 6]])
arr_2 >>> array([[1, 2, 3],
       [4, 5, 6]])

# NumPy has a whole sub module dedicated towards matrix operations called numpy.mat
# Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:
arr_3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
arr_3 >>> 
array([[[1, 2, 3],
        [4, 5, 6]],

       [[1, 2, 3],
        [4, 5, 6]]])

# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
arr_3.ndim >>> 3

arr_4 = np.array([1, 2, 3, 4], ndmin=4)
arr_4 >>> array([[[[1, 2, 3, 4]]]])
```
