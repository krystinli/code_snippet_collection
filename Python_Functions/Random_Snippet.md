# TOC
- Data_Load
- String_Attributes
- time.time()




## Data_Load
With Dask vs. Pandas chunksize option
```python
# 1) data loading with pandas 
df_chunk = pd.read_csv("test_data.csv", chunksize=100000) 

chunk_list = []  
for chunk in df_chunk:  
    chunk_list.append(chunk)
data = pd.concat(chunk_list)

# 2) data loading with dask 
data = dask.dataframe.read_csv("test_data.csv").compute()
```
<br />

## String_Attributes
```python
.strip() # remove whitespace
.lower()
.replace(old,new)

#  splits the string into substrings if it finds instances of the separator
a = "Hello, World!"
a.split(",") # returns ['Hello', ' World!']
```
<br />

## Random_Number
```python
import random
random.randrange(1,10)
```
<br />

## time.time()
runtime measure
```python
# 1) time.time()
import time
start_time = time.time()
...
print("This process takes %s seconds" %(time.time()-start_time))

# 2) %timeit magic function
import numpy as np

a = np.random.randn(100,100)
%timeit np.dot(a, a)
>> 35.6 µs ± 256 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
```
<br />
