TOC
- [Dict](https://github.com/krystinli/code_snippet_collection/blob/master/Python_Functions/Data_Types.md#dict)
- [List](https://github.com/krystinli/code_snippet_collection/blob/master/Python_Functions/Data_Types.md#list)

## Dict
```py
# delete a key,value pair 
del dict[key]
dict.pop(key) >>> return value of the key 

# add/upsert new value
dict[new_key] = new_value
dict.update({old_key:new_value})

list(dict.keys()) >>> return all keys in the dict 
list(dict.values())

# dict(zip(key_list, values_list)):
col_name = ['name', 'age']
name_list = ['Krystin', 5]

dict_1 = dict(zip(col_name, name_list))

# creating dict from sequence
mapping = {}
for key,value in zip(key_list,value_list):
  mapping[key]=value

# dict is essentially a collection of 2-tuples (key-value pair)
mapping = dict(zip(range(5), reversed(range(5)))) >>> {0:4, 1:3, 2:2, 3:1, 4:0}

# default values
if key in some_dict:
  value = some_dict[key]
else:
  value = default_value 
  
# get attribute by default returns None if the key is invalid 
# for this use case, you can do:
value = some_dict.get(key, default_value)

# default dict
```

## List
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
lst.sort(reverse=True)
sorted(lst) # return a new sorted lst from the old lst

# enumerate - compute a dict mapping the values of a sequence to their locations in the sequence 
mapping = {}
for i, value in enumerate(sequence):
  mapping[value] = i
  
# zipping - zip 2 sequences (lst, tups, etc) and create a list of tuples 
zipped = zip(seq1, seq2)
list(zipped) >>> list of tuples 

name_lst = [("vera", "wang"), ("celin", "dion")]
first_name, last_name = zip(*name_lst) # unzip the sequence like converting a list of rows to cols
>>> first_name = ("vera", "celin)

# iterate over multiple sequences with enumerate and zip
for i, (a, b) in enumerate(zip(seq1, seq2)):
  print("Index {0}: sync to values {1}, {2}".format(i, a, b))

# reversed
list(reverse(seq)) # reserve is a generator so it doesn't create the sequence until materialized (with list or for loop)

# copy
list_copy = lst.copy() 
list_copy = lst[:] # or copy by slicing
```

### bisect
The built-in bisect module implements binary search and insertion into a sorted list.
```py
import bisect

bisect.bisect(lst, item) >>> location # find the location where an item should be inserted 
bisect.insort(lst, item) >>> new lst # insert the item into lst to make a new lst (without checking if current lst is sorted)
```

### string
Strings are arrays of bytes representing unicode characters. Python does not have a character data type, a single character is simply **a string with a length of 1**. Some `str.()` methods:
```python
str.strip() # method removes any whitespace from the beginning or the end
str.lower() # method returns the string in lower case
str.upper()

a = "Hello, World!"
a.replace("H", "J") # method replaces a string with another string

# The split() method splits the string into substrings if it finds instances of the separator:
a.split(",") # returns ['Hello', ' World!']
```


