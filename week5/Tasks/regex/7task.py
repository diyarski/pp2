import re

snake_string = "hello_world_from_Diyar"

def snake_to_camel(snake_string):
    camel_string = re.sub(r'_([a-zA-Z])', lambda m: m.group(1).upper(), snake_string)
    return camel_string

print(snake_to_camel(snake_string))
