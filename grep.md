### grep
- ` grep 'str_name' *` - find a str in files
- ` grep -r 'str_name' *` - find a str in directory and display the line containing the str
- ` grep -lr 'str_name' *` - find a str in directory and display the filename 
- `grep -r 'str_name' * | xargs -0 sed -i '' 's/str_name/str_name_new/g'` - find and replace MacOS
 
