import re

pattern = r'a[bb]{2,3}'

string = 'abbb'

if re.search(pattern, string):
    print("Match found!")
else:
    print("No match found.")
