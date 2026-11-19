

#a = "mamma"
#a += " mia"
#print(a)

#print(18 % 5)


# a1=[2,4,3]
# a2=[5,6,4]

# x1 = 0
# x2 = 0
# y1 = 0
# y2 = 0
# c1 = 1
# c2 = 1

# for y1 in range(len(a1), 0, -1):
#     x1 += a1[y1-1] * (10**(len(a1)-c1))
#     c1 += 1

# for y2 in range(len(a2), 0, -1):
#     x2 += a2[y2-1] * (10**(len(a2)-c2))
#     c2 += 1

# x3 = str(x1 + x2)

# y3 = 0
# l3 = []

# for y3 in range(len(x3), 0, -1):
#     l3.append(int(x3[y3 - 1]))

# print(l3)

# Pi = 3.14159

# def volume_cylinder(radius, height):
#     return Pi*(radius**2)*height

# def volume_hemisphere(radius):
#     return (2*Pi*(radius**3))/3

# def volume_test_tube_internal(radius, height, thickness):
#     radius = radius - thickness
#     return (volume_cylinder(radius, height)) + (volume_hemisphere(radius))

# print(volume_test_tube_internal(2,1,1))

# from math import sin as suck

# macock = 69

# print(suck(macock))



def my_func(lst, y):
        z = 0
        for x in lst:
                if x < y:
                         z = z + x
        return z


def my_func_test(lst, y):
        z = 0
        for x in lst:
                if x < y:
                         z += x
        return z

lst = [1,2,3,4,5,6,7]
y = 5

print(my_func(lst,y))
print(my_func_test(lst,y))