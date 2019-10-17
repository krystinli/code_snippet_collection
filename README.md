# pandas_code_snippet 

```python
import pandas as pd
import os

# file handling
cwd = os.get_cwd()
cwd # check current dir 

pd.read_csv('filename.csv', sep=',')
pd.read_csv('folder/filename.csv', sep='|' , header=None, names= ['col1_nm','col2_nm',...])

# counting
df.col_nm.count() # select count(*)
df.col_nm.nunique() # select count(distinct col_nm)

# where stmt 
df_ca = df[df['county'=='CA']] # select * from df where country = 'CA'
df[df['county'=='CA']].memberID.unique() # select count(distinct memberID) from df where country = 'CA'

# group by 


# left join 

# union 
```
