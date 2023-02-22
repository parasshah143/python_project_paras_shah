def area_of_the_circle(radius):
    area = radius * radius * 3.14
    return area


def triangle_area(a, b, c):
    s = (a + b + c) / 2
    tri = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return tri


def trapezium(base_1, base_2, height):
    tra = ((base_1 + base_2) / 2) * height
    return tra


def square_area(s):
    area_square = s * s
    return area_square


def Sphere(r):
    sph = 4.0 / 3.0 * 3.14 * r ** 3
    return sph


def Cylinder(r, h):
    cyl = 2 * 3.14 * pow(r, 2) * h
    return cyl


def volumeHexagonal(a, b, h):
    return a * b * h


def Volume_of_cone(r, h):
    return (3.14 * r * r * h) / 3
