import math

def degree_to_radian(degrees):
    radians = degrees*(math.pi/180)
    return radians

print(round(degree_to_radian(15), 6))
