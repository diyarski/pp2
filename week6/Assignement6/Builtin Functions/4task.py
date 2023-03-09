import time
import math

string = input()
number, delay = map(int, string.split()) # splits the string by a space and converts to integers using map

time.sleep(delay / 1000) # convert to seconds

sqrt = math.sqrt(number)

print(f"Square root of {number} after {delay} miliseconds is {sqrt}")
