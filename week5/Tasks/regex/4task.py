import re

string = "Hello WorLd, this is DiAs"

matches = re.findall(r'[A-Z]+[a-z]+', string)

print(matches)
