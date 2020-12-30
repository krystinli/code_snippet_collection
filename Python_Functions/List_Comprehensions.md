## List Comprehensions

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

# sorting 
lst.sort() # sort a list in-place without creating a new obj 
lst.sort(key=len) # sort by length of items in lst
sorted(lst) # return a new sorted lst from the old lst

# enumerate - compute a dict mapping the values of a sequence to their locations in the sequence 
mapping = {}
for i, value in enumerate(sequence):
  mapping[value] = i
  
# zipping - zip 2 sequences (lst, tups, etc) and create a list of tuples 
zipped = zip(seq1, seq2)
list(zipped) >>> list of tuples 

for i, (a, b) in enumerate(zip(seq1, seq2)):
  print("Index {0}: sync to values {1}, {2}".format(i, a, b))


```

### bisect
The built-in bisect module implements binary search and insertion into a sorted list.
```py
import bisect

bisect.bisect(lst, item) >>> location # find the location where an item should be inserted 
bisect.insort(lst, item) >>> new lst # insert the item into lst to make a new lst (without checking if current lst is sorted)
```
