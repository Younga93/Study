'''
Written by Younga
September 22, 2020

Demonstrate how to write a simple program
 and make available to other program
'''

PI = 3.1415926

def add(x, y):
    return x + y

def diff(x, y):
    return x - y

def area_of_circle(r):
    return PI * r ** 2

def area_of_rectangle(w, length):
    return w * length

radius = 10

print(f'A circle of radius {radius} will have area {area_of_circle(radius)}')
