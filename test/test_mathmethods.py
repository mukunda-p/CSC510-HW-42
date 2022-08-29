import sys
from code.mathmethods import *

def test_sqaure():
    for i in range(1,100):
        assert square(i)==i**2

def test_cube():
    for i in range(1,100):
        assert cube(i)==i**3
        
