# pd.snippet
```py
# 0) types
df.dtypes

# Prints a summary of columns count and its dtypes but not per column information:
df.info(verbose=False)
df.describe

# 1) counting
df.col.count() # select count(*)
df.col.nunique() # select count(distinct col_nm)
df.drop_duplicates() # drop dup rows

# 2) sorting
df.sort_values(by=['some_col'], ascending=False, inplace=True) # order by desc
df.sort_values('col', ascending=True).head(10) # order by rank limit 10 

# 3) rename 
df = df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'})

# name first row as col names
df.rename(columns=df.iloc[0])

# 4) condition on rows
pd.where(condition, value) # Where cond is True, keep the original value. Where False, replace with corresponding value from other.
pd.mask(condition, value) # Where cond is False, keep the original value. Where True, replace with corresponding value from other. 

# if condition
df.loc[df["Column1"]=xxx, "Column2"] = "New value for Column2"

# 5) splitting the object, applying a function, and combining the results
df.groupby(by=["b"], dropna=False).sum()

# reset_index
df.reset_index(drop=True)

# 6) constructing DataFrame from a dictionary
>>> d = {'col1': [1, 2], 'col2': [3, 4]}
>>> df = pd.DataFrame(data=d)

# To enforce a single dtype and set col names
>>> df = pd.DataFrame(data=d, dtype=np.int8, columns = ['col1','col2' ..])

7) remove header
data = data.xs('Category: All categories', axis=1, drop_level=True)

# drop columns
df.drop(["Column1"], axis=1)

8) convert pd series into data frame
new_df = some_col.to_frame()

9) extract a single value from panda series row
df[df[col]==A][col2].tolist()[0]
```

### [pd.fillna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html#pandas.DataFrame.fillna)
```python
# 1) Fill NA/NaN values using the specified method
df.fillna(value=0, inplace=True)

# 2) Replace all NaN elements in column ‘A’, ‘B’, ‘C’, and ‘D’, with 0, 1, 2, and 3 respectively.
values = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
df.fillna(value=values)

# 3) Drop the rows where at least one element is missing
df.dropna(inplace=True)

# 4) Define in which columns to look for missing values
df.dropna(subset=['name', 'toy'])

# 5) Drop the rows where all elements are missing
df.dropna(how='all')

# 6) Show which entries in a DataFrame are NA.
df.isna()

# 7) replace str None with NaN
df.replace({None:np.nan}, inplace=True)

# 8) count num of NaNs in a columns
df[col].isnull().sum() 

# 9) count num of NaNs in the entire df
df.isnull().sum().sum()

# 10) case
df["col_name"] = df["col_name"].str.lower()
df["col_name"] = df["col_name"].str.upper()
```

### [pd.merge](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)
horizontally combining the dfs
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

### [pd.concat](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.concat.html)
vertically combining the dfs
```py
union_df = pd.concat([df1, df2], ignore_index=True)
union_df = df1.append(df2, ignore_index=True) # df cannot be empty [] to start with 
```

### [pd.apply](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html)
```python
# 1) apply sum as a reducing function on either axis
df.apply(np.sum, axis=0)
df.apply(np.sum, axis=1)

# 2) apply to entire df
df.apply(np.sqrt)

# 3) lambda apply
df.apply(lambda x: pd.Series([1, 2], index=['foo', 'bar']), axis=1)
df.apply(lambda x: func(x['col1'], x['col2']), axis=1)
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

### [pd.memory_usage](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.memory_usage.html)
```py
# The memory footprint of object dtype columns is ignored by default:
>>> df.memory_usage()
Index           128
int64         40000
float64       40000
complex128    80000
object        40000
bool           5000
dtype: int64

>>> df.memory_usage(deep=True)
Index            128
int64          40000
float64        40000
complex128     80000
object        180000
bool            5000
dtype: int64

# Use a Categorical for efficient storage of an object-dtype column with many repeated values:
>>> df['object'].astype('category').memory_usage(deep=True)
5244

# Attempt to infer better dtypes for object columns:
df.infer_objects().dtypes
```
