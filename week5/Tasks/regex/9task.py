import re

string = "HelloWorldFromDias"

def insert_spaces(string):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', string)

print(insert_spaces(string))
