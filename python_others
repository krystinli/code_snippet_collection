## Jupyter_Functions
functions specific for notebooks
```python
# notebook viewing option for pandas
pd.set_option('display.max_columns', 999)
pd.set_option('display.max_rows', 999)

# latex conversion or HTML
%%latex
Some important equations:$E = mc^2$
$e^{i pi} = -1$

%%HTML
This is <em>really</em> neat!

%load imports.py
load another py file, a great way to store all the imports

%run imports.py
run a py file

# plotting
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

# or
%matplotlib notebook
```

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

## matplotlib
```python
%matplotlib inline
import matplotlib.pyplot as plt

plt.plot(np.random.randn(50).cumsum())
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
