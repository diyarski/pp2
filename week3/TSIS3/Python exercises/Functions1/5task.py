def permute(string, answer):
    if (len(string) == 0):
        print(answer, end=" ")
 
    for i in range(len(string)):
        a = string[i]
        left_substring = string[0:i]
        right_substring = string[i + 1:]
        rest = left_substring + right_substring
        permute(rest, answer + a)

answer = ""
 
string = input()

permute(string, answer)
