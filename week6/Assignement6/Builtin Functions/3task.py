def is_palindrome(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]

str = input("Write a string: ")
if is_palindrome(str):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
