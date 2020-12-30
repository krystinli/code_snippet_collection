## List_Comprehensions

```py
# updateing list
lst.append(item) # item added to end of list
lst.remove(item) # remove item from list, opposite of append
lst.insert(0, item) # insert item at specific location, computational expensive compared to append 
lst.pop(0) # remove element at specific location and returns the item being removed, oppostive of insert 
item in lst >>> True # inefficient compared to dicts as Python makes a linear scan across value in lst 

# concatenation
lst1 + lst2 # by addition, but more expensive since a new list must be created and the objs copied over 
lst1.extend(lst2) # requires both lst already defined, extending an existing list, and hence more preferrable:

data_agg = []
for chunk in lst_of_lst:
  data_agg.extend(chunk). # instead of data_agg = data_agg + chunk 
```
