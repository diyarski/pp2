import re

pattern = r'a[b]*'

string = 'abbbb'

if re.search(pattern, string):
    print("Match found!")
else:
    print("No match found.")
