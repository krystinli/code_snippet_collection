# pandas

### Basica
```python
# name first row as col names
df.rename(columns=df.iloc[0])

# select first 3 rows
data[:2]
```

### Jupyter_Notebooks
```python
# notebook viewing option
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)
```

### File_Transfer
```python
# avoid saving or getting index_col
pd.read_csv("filename.csv", index_col=0)
data.to_csv("filename.csv", index=False)

# remove index
pd.read_csv("filename.csv", sep=",").drop(["unnamed 0"], axis=1) 
pd.read_csv("folder/filename.csv", sep="|" , header=None, names= ["col1_nm","col2_nm",...]) # assign new col names 
```

### Value_Setting
```python
new_df = pd.DataFrame(data, columns = ['colname1','colname2','colname3'])

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

### NaN/NULL
```python
# count NaN
df[col].isnull().sum() # count num of NaNs in a columns
df.isnull().sum().sum() # count num of NaNs in the entire df

# replace str None with NaN
df.replace({None:np.nan}, inplace=True)
```

### SQL
```python
# counting
df.col_nm.count() # select count(*)
df.col_nm.nunique() # select count(distinct col_nm)
df.drop_duplicates() # drop dup rows

# sorting
df.sort_values(by=['some_col'], ascending=False, inplace=True) # order by desc
df['rank'] = some_col.rank(ascending=False) # adding rank col to the df 
df.sort_values('rank', ascending=True).head(10) # order by rank limit 10 

# where stmt 
df[df['county'=='CA']] # select * from df where country = 'CA'
df[df['county'=='CA']].memberID.unique() # select count(distinct memberID) from df where country = 'CA'

# group by 
df.groupby(['colname']).count()
df.groupby(['colname']).nunique() # group by + count distinct 

# new col 
df = df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'})
```

### Joining
```python
# left join
new_df = pd.merge(df_left, df_right, how='left', on=['key1','key2',...])
new_df = pd.merge(df_left, df_right, how='left', left_on='key1', right_on='key1') # join with different col_name
new_df_append = pd.merge(df1, df2, right_index=True, left_index=True) # this is joining on index 

# union 
union_df = df1.append(df2, ignore_index=True) # df cannot be empty [] to start with 
union_df = pd.concat([df1, df2], ignore_index=True)

# convert pd series into data frame
new_df = some_col.to_frame()

# creating a new df with a subset of columns
df2 = df1[['col_1', 'col4', 'col5']]
```
