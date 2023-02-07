s = input()

print(s[0: s.find('h')] + s[s.rfind('h') + 1::])
