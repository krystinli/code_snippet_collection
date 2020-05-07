## general_snippet

data loading
```python

# runtime measure
import time
time.time()

# data loading with pandas 
df_chunk = pd.read_csv("test_data.csv", chunksize=100000) 

chunk_list = []  
for chunk in df_chunk:  
    chunk_list.append(chunk)
data = pd.concat(chunk_list)

# data loading with dask 
data = dask.dataframe.read_csv("test_data.csv").compute()
```

random 
```
import random
random.randrange(1,10)
```

## string
```
.strip() # remove whitespace
.lower()
.replace(old,new)

#  splits the string into substrings if it finds instances of the separator
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

```
