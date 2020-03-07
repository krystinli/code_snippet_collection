### Global_Regular_Expression_Print
- `grep xxx filename` finding xxx in file
- `grep -w xxx filename` finding xxx in file and restrict to xxx only
- `grep -n xxx filename` finding xxx in file with line number
- `grep -v xxx filename` inverse finding ... return everything that doesn't match 
- `grep -i xxx filename` finding xxx in file with inverse output
- `man grep` prints mannual of grep function and `q` to quit mannual mode
- `grep -E '^.o' haiku.txt` irregular expr
- `find . -type d` in the current dir `.`, find things that're dir `-type d`
- `find . -type f` in the current dir `.`, find things that're files `-type f`

find
- `grep 'str_name' * > grep_output.txt` - find a str in files
 - + `-r` for recursive => `grep -r 'str_name' *`
 - + `-l` for filename => `grep -l 'str_name' *`
 - + `-i` for case insensitive => `grep -i 'str_name' *`

replace
- `grep -r 'str_name' * | xargs -0 sed -i '' 's/str_name/str_name_new/g'` - find and replace MacOS
 
### Escaping
- `"..."` or `'...'` - putting entire thing in a single/double quote avoid escapting whitespaces
- `grep '\[*\]' file` - find any [...] 
