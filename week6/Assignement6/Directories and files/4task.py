import os
line_cnt = 0
path = input("Write the file path: ")
with open(path, "r") as file:
    for line in file:
        line_cnt +=1

print("Number of lines:", line_cnt)
