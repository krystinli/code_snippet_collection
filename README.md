# pandas_code_snippet 

### 01_reading file
```python
import pandas as pd
import os

# file handling
cwd = os.get_cwd()
cwd # check current dir 

pd.read_csv('filename.csv', sep=',')
pd.read_csv('folder/filename.csv', sep='|' , header=None, names= ['col1_nm','col2_nm',...])
```

### 02_sql_operations
```python
# counting
df.col_nm.count() # select count(*)
df.col_nm.nunique() # select count(distinct col_nm)

# where stmt 
df_ca = df[df['county'=='CA']] # select * from df where country = 'CA'
df[df['county'=='CA']].memberID.unique() # select count(distinct memberID) from df where country = 'CA'

# group by 
df.groupby(['colname']).count()
df.groupby(['colname']).nunique() # group by + count distinct 

# left join
pd.merge(df_left, df_right, how='left', on=['key1','key2',...])
pd_merge = pd.merge(df_mem, df_act, how='left', on=['memberID']) # df_mem left join df_act on memberID
appending_merge = pd.merge(df1, df2, right_index=True, left_index=True) # this is joining on index 

# union 
df = df.append(df2, ignore_index=True) # df cannot be empty [] to start with 
df = pd.concat(df2)
df = [df1, df2] 

# sort
df['rank'] = some_col.rank(ascending=False) # adding rank col to the df 
df.sort_values('rank', ascending=True).head(10) # order by rank limit 10 
df.sort_values('rank', ascending=True).tail(10)

# new col 
df = df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'})

# convert pd series into data frame
new_df = some_col.to_frame()

# creating a new df with a subset of columns
df2 = df1[['col_1', 'col4', 'col5']]
```
