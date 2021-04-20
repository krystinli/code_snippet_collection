# Pandas
- pd.merge
- read_csv

### [pd.merge](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)
```python
# 1) inner join and left join 
df1.merge(df2, how='inner', on='a')
df1.merge(df2, how='left', on='a') # or cross 

# 2) full outer join with left and right suffixes appended to any overlapping columns
df1.merge(df2, left_on='lkey', right_on='rkey', suffixes=('_left', '_right')) 

>>> lkey  column_left rkey  column_right
0   foo        1      foo          5
1   foo        1      foo          8
2   foo        5      foo          5

# 3) join to create a new df
df3 = pd.merge(df_left, df_right, how='left', on=['key1','key2',...])
df3 = pd.merge(df_left, df_right, how='left', left_on='key1', right_on='key2') 

# 4) joining on index 
new_df = pd.merge(df1, df2, right_index=True, left_index=True) 
```

### [pd.read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
```python
# 1) avoid saving or getting index_col
data.to_csv("path/filename.csv", index=False)
pd.read_csv("path/filename.csv", index_col=0)

# 2) remove index
pd.read_csv("filename.csv", sep=",").drop(["unnamed 0"], axis=1) 
pd.read_csv("folder/filename.csv", sep="|" , header=None, names= ["col1_nm","col2_nm",...]) # assign new col names 

# 3) reading with chunksize option 
df_chunk = pd.read_csv("test_data_75MB.csv", chunksize=100000) # 10% of total rows#
chunk_list = []  

for chunk in df_chunk:  
    chunk_list.append(chunk)
data = pd.concat(chunk_list)
```
