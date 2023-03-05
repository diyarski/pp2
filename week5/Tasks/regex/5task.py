import re

string = "acsb abs abb a5b"

matches = re.findall(r'a.*?b', string)

print(matches)
