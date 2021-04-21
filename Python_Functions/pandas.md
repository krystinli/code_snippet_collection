### pd.DataFrame
```py
# Constructing DataFrame from a dictionary
>>> d = {'col1': [1, 2], 'col2': [3, 4]}
>>> df = pd.DataFrame(data=d)
    col1  col2
0     1     3
1     2     4

# The inferred dtype is int64
>>> df.dtypes
col1    int64
col2    int64
dtype: object

# To enforce a single dtype
>>> df = pd.DataFrame(data=d, dtype=np.int8)
>>> df.dtypes
col1    int8
col2    int8
dtype: object

# Generally:
new_df = pd.DataFrame(data, columns = ['col1','col2' ..])

# Constructing DataFrame from numpy ndarray
df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])
>>>
   a  b  c
0  1  2  3
1  4  5  6
2  7  8  9

# Prints a summary of columns count and its dtypes but not per column information:
df.info(verbose=False)
>>>
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Columns: 3 entries, int_col to float_col
dtypes: float64(1), int64(1), object(1)
memory usage: 248.0+ bytes

# The memory_usage parameter allows deep introspection mode, specially useful for big DataFrames and fine-tune memory optimization:
df.info(memory_usage='deep')
```

### Basic
```python
# name first row as col names
df.rename(columns=df.iloc[0])

# select first 3 rows
data[:2]

# remove header
data = data.xs('Category: All categories', axis=1, drop_level=True)

# union 
union_df = df1.append(df2, ignore_index=True) # df cannot be empty [] to start with 
union_df = pd.concat([df1, df2], ignore_index=True)

# convert pd series into data frame
new_df = some_col.to_frame()

# creating a new df with a subset of columns
df2 = df1[['col_1', 'col4', 'col5']]
```

### Value_Setting
```python
# case
df["col_name"] = df["col_name"].str.lower()
df["col_name"] = df["col_name"].str.upper()

# if condition
df.loc[df["Column1"]=xxx, "Column2"] = "New value for Column2"

# extract a single value from panda series row
df[df[col]==A][col2].tolist()[0]

# drop columns
df.drop(["Column1"], axis=1)

# reset_index
df.reset_index(drop=True)
```
