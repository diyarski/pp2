import re

string = "HelloWorldFromDias"

def split_at_uppercase(string):
    return re.findall(r'[A-Z][^A-Z]*', string)

print(split_at_uppercase(string))
