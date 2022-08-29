import sys
from code.math_methods import cube,square,factorial,exp

def test_cube():
    count=1
    while count<=100:
        assert cube(count)==count**3
        count=count+1

def test_square():
    count=1
    while count<=100:
        assert square(count)==count**2
        count=count+1
