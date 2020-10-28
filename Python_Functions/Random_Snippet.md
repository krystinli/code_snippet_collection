# TOC
- Data_Load
- String_Attributes

## Data_Load
With Dask vs. Pandas chunksize option
```python

# runtime measure
import time
start_time = time.time()

# data loading with pandas 
df_chunk = pd.read_csv("test_data.csv", chunksize=100000) 

chunk_list = []  
for chunk in df_chunk:  
    chunk_list.append(chunk)
data = pd.concat(chunk_list)

# data loading with dask 
data = dask.dataframe.read_csv("test_data.csv").compute()

print("This process takes %s seconds" %(time.time()-start_time))
```

random 
```python
import random
random.randrange(1,10)
```

## String_Attributes
```python
.strip() # remove whitespace
.lower()
.replace(old,new)

#  splits the string into substrings if it finds instances of the separator
a = "Hello, World!"
a.split(",") # returns ['Hello', ' World!']

```
