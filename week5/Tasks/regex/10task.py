import re

camel_string = "HelloWWorldFromDias"

def camel_to_snake(camel_string):
    s1 = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_string)
    snake_string = s1.lower()
    return snake_string

print(camel_to_snake(camel_string))
