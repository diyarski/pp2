import os

path = "C:/Users/dtbku/Documents/uni"

print("Directories: ")
for item in os.listdir(path):
    if os.path.isdir(os.path.join(path, item)):
        print(item)

print("\nFiles:")
for item in os.listdir(path):
    if os.path.isfile(os.path.join(path, item)):
        print(item)

print("\nAll Directories and Files: ")
for item in os.listdir(path):
    print(item)
