import math
from code.math_methods import *

def test_cube():
    assert cube(-2)==(-2)**3
    assert cube(0)==0**3
    assert cube(2)==2**3

def test_square():
    assert square(-2)==(-2)**2
    assert square(0)==0**2
    assert square(2)==2**2

def test_factorial():
    assert factorial(0)==math.factorial(0)
    assert factorial(2)==math.factorial(2)
    assert factorial(100)==math.factorial(100)

def test_exp():
    assert exp(1,2)==math.pow(1,2)
    assert exp(2,3)==math.pow(2,3)
    assert exp(100,3)==math.pow(100,3)