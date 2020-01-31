### global regular expression print

find
- `grep 'str_name' * > grep_output.txt` - find a str in files
 - + `-r` for recursive => `grep -r 'str_name' *`
 - + `-l` for filename => `grep -l 'str_name' *`
 - + `-i` for case insensitive => `grep -i 'str_name' *`

replace
- `grep -r 'str_name' * | xargs -0 sed -i '' 's/str_name/str_name_new/g'` - find and replace MacOS
 
