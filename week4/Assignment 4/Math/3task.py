import math

def area(num_of_sides, len_of_sides):
    Area = ((len_of_sides ** 2) * num_of_sides) / (4 * math.tan (math.pi / num_of_sides))
    return Area

print(round(area(4, 25)))
