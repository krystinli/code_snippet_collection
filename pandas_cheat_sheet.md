# Pandas

## [pd.merge](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)
```python
# full outer join with left and right suffixes appended to any overlapping columns
df1.merge(df2, left_on='lkey', right_on='rkey', suffixes=('_left', '_right')) 

>>> lkey  column_left rkey  column_right
0  foo          1    foo          5
1  foo          1    foo          8
2  foo          5    foo          5


# inner join and left join 
df1.merge(df2, how='inner', on='a')
df1.merge(df2, how='left', on='a') # or cross join 

# join with different col_name
new_df = pd.merge(df_left, df_right, how='left', on=['key1','key2',...])
new_df = pd.merge(df_left, df_right, how='left', left_on='key1', right_on='key1') 

# this is joining on index 
new_df = pd.merge(df1, df2, right_index=True, left_index=True) 
```
