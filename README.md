# pandas_code_snippet 

```python
import pandas as pd
import os

# file handling
cwd = os.get_cwd()
cwd # check current dir 

pd.read_csv('filename.csv')
pd.read_csv('folder/filename.csv', header=None, names= ['col1_nm','col2_nm',...])

# counting
df.col_nm.count() # count(*)
df.col_nm.nunique() # count(distinct col_nm)



```
