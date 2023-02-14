def palindrome(s):
    return s == s[::-1]
s = input()
answer = palindrome(s)
 
if answer:
    print("Yes")
else:
    print("No")
