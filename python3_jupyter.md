## code_snippet
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
