import re

string = "sample_string_of_lowercase_letters"

matches = re.findall(r'[a-z]+_[a-z]+', string)

print(matches)
