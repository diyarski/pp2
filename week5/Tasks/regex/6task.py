import re
txt = "Hello, World. My name is Dias"
def replace(txt):
    pattern = r'[ ,.]'
    new_txt = re.sub(pattern, ':', txt)
    return new_txt
print(replace(txt))
