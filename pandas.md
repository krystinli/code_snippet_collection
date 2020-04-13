# pandas

### General
```python
# JP notebook viewing option
pandas.set_option('display.max_rows', 10)

# turn list of list into df, useful when looping over the same process and computer different metrics 
data.append([item1, item2, item3)]
new_df = pd.DataFrame(data, columns = ['colname1','colname2','colname3'])

# case
df["col_name"] = df["col_name"].str.lower()
df["col_name"] = df["col_name"].str.upper()

# null condition
df.isnull # IS NULL in sql
df.notnull # IS NOT NULL

# replace str with something else 
df.replace({None:np.nan}, inplace=True)

# if condition
df.loc[df['column name'] condition, 'new column name'] = 'value if condition is met'

# drop columns
df.drop(['B', 'C'], axis=1)

# extract a single value from panda series row
df[df[col]==A][col2].tolist()[0]
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
df = df.append(df2, ignore_index=True) # df cannot be empty [] to start with 
df = pd.concat(df2)
df = [df1, df2] 

# convert pd series into data frame
new_df = some_col.to_frame()

# creating a new df with a subset of columns
df2 = df1[['col_1', 'col4', 'col5']]
```

### File_Transfer
```python
import pandas as pd
import os

# avoid saving or getting index_col
pd.read_csv("file0.csv", index_col=0)
data.to_csv("file1.csv", index=False)

# file handling
cwd = os.get_cwd()
cwd # check current dir 

pd.read_csv('filename.csv', sep=',').drop(['unnamed 0'], axis=1) # remove index
pd.read_csv('folder/filename.csv', sep='|' , header=None, names= ['col1_nm','col2_nm',...])

# files to_csv
df_output = pd.DataFrame(lst_output, columns=["col1","col2","col3"])
df_output.to_csv('filename.csv', sep=',')
```
