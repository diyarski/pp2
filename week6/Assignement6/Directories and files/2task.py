import os

path = "C:/Users/dtbku/Documents/uni"

# Check if path exists
if os.path.exists(path):
    directory, filename = os.path.split(path)
    print("Directory: ", directory)
    print("Filename: ", filename)
else:
    print("Path does not exists")
