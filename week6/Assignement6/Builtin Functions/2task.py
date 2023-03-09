def count(string):
    upper_count = sum(1 for letter in string if letter.isupper())
    lower_count = sum(1 for letter in string if letter.islower())
    return upper_count, lower_count

str = input("Write a string: ")

uc, lc = count(str)
print("Number of uppercase letters", uc)
print("Number of lowercase letters", lc)
