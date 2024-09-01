# takes in two vectors in a list
# calculate dot product and cross product
# eg: vector1 = [1,2,3] vector2 = [4,5,6]
# no libraries


def get_dot_product(a, b):
    dot = []
    for i in range(len(a)):
        dot.append(a[i] * b[i])
    return dot

def get_cross_product(a, b):
    cross = []
    if len(a) == 3:
        cross.append(a[1] * b[2] - a[2] * b[1]) # i
        cross.append(-(a[0] * b[2] - a[2] * b[0])) # j
        cross.append(a[0] * b[1] - a[1] * b[0]) # k
    return cross

a = [4, -2, 5]
b = [-1, 3, -6]
c = [7, -5, 1]

if len(a) == len(b) and len(a) > 0:
    dot_product = get_dot_product(a, b)
    print('dot product:',dot_product)

    cross_product = get_cross_product(a, c)
    print('cross product:',cross_product)

else:
    print('Given vectors differ in magnitude')

