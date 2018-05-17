#!/usr/bin/env python
import re as reg
"""
Alaaddin Alokby
Lab 5: Complex Numbers
Problems: 
Sources: 
https://docs.python.org/2/reference/datamodel.html#emulating-numeric-types
https://docs.python.org/3/tutorial/classes.html
http://mathworld.wolfram.com/ComplexDivision.html
"""

class Complex:
    """A class that performs simple operations on complex numbers"""

    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im
        

        # handle imaginary number if entered alone, and as a string
        if type(re) == str and im == 0:
            if 'i' in re:
                im_str = reg.findall(r'\d*i', re)
                im_str = im_str[0][:-1]
                self.re = 0
                self.im = float(im_str)
                

    def __str__(self):
        if self.im < 0:
            return '({} - {}i)'.format(str(self.re),str(-1*self.im))
        return '({} + {}i)'.format(str(self.re), str(self.im))
        

    def __add__(self, other):
        try:
            return Complex(self.re + other.re, self.im + other.im)
        except:
            other = Complex(other)
            return Complex(self.re + other.re, self.im + other.im)

    def __radd__(self, other):
        try:
            return Complex(self.re + other.re, self.im + other.im)
        except:
            other = Complex(other)
            return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        try:
            return Complex(self.re - other.re, self.im - other.im)
        except:
            other = Complex(other)
            return Complex(self.re - other.re, self.im - other.im)

    def __rsub__(self, other):
        try:
            return Complex(self.re - other.re, self.im - other.im)
        except:
            other = Complex(other)
            return Complex(self.re - other.re, self.im - other.im)
    # Complex multiplication - returns float
    def __mul__(self, other):
        try:
            return Complex((self.re * other.re) - (self.im * other.im), (self.re * other.im) + (self.im * other.re))
        except:
            other = Complex(other)
            return Complex((self.re * other.re) - (self.im * other.im), (self.re * other.im) + (self.im * other.re))

    __rmul__ = __mul__
    
    # Using the tilde operator - returns the conjugate
    def __invert__(self):
        return Complex(self.re, -1*self.im)
    # Using the negative operator - returns same magnitude, opposite sign
    def __neg__(self):
        return Complex(-1*self.re, -1*self.im)

    # Complex division - returns integer
    def __floordiv__(self, other):
        try:
            return Complex((self.re*other.re + self.im*other.im)/(other.re**2 + other.im**2),(self.im*other.re - self.re*other.im)/(other.re**2 + other.im**2))
        except AttributeError:
            try:
                other = Complex(other)
                return Complex((self.re*other.re + self.im*other.im)/(other.re**2 + other.im**2),(self.im*other.re - self.re*other.im)/(other.re**2 + other.im**2))
            except ZeroDivisionError:
                return 'ZeroDivisionError: division by zero -- floor'

    def __rfloordiv__(self, other):
        try:
            return Complex((other.re*self.re + other.im*self.im)/(self.re**2 + self.im**2),(other.im*self.re - other.re*self.im)/(self.re**2 + self.im**2))
        except AttributeError:
            try:
                other = Complex(other)
                return Complex((other.re*self.re + other.im*self.im)/(self.re**2 + self.im**2),(other.im*self.re - other.re*self.im)/(self.re**2 + self.im**2))
            except ZeroDivisionError:
                return 'ZeroDivisionError: division by zero -- floorr'

    # Complex division - returns float
    def __truediv__(self, other):
        try:
            return Complex((self.re*other.re + self.im*other.im)/(other.re**2 + other.im**2),(self.im*other.re - self.re*other.im)/(other.re**2 + other.im**2))
        except AttributeError:
            try:
                other = Complex(other)
                return Complex((self.re*other.re + self.im*other.im)/(other.re**2 + other.im**2),(self.im*other.re - self.re*other.im)/(other.re**2 + other.im**2))
            except ZeroDivisionError:
                return 'ZeroDivisionError: division by zero -- true'

    def __rtruediv__(self, other):
        try:
            return Complex((other.re*self.re + other.im*self.im)/(self.re**2 + self.im**2),(other.im*self.re - other.re*self.im)/(self.re**2 + self.im**2))
        except AttributeError:
            try:
                other = Complex(other)
                return Complex((other.re*self.re + other.im*self.im)/(self.re**2 + self.im**2),(other.im*self.re - other.re*self.im)/(self.re**2 + self.im**2))
            except ZeroDivisionError:
                return 'ZeroDivisionError: division by zero -- truer'

# Solve for the square root of a complex number
# Sign Function
# https://en.wikipedia.org/wiki/Complex_number#Square_root
# https://en.wikipedia.org/wiki/Sign_function
def signum(a):
    if a > 0:
        return 1
    if a < 0:
        return -1
    return 0

# This is not a class function
def sqrt(a):
    if type(a) == Complex:
        # get the real and imaginary components of the complex number
        re = a.re
        im = a.im
        # Calculate gamma
        gamma = ((re + (re**2 + im**2)**0.5)/2)*0.5
        delta = signum(im)*((-re + (re**2 + im**2)**0.5)/2)**0.5
        return Complex((gamma + delta)**2)
    return a**0.5
    

if __name__ == '__main__':
    c = Complex(17, -5)
    r = Complex(20, 10)
    print(-r)
    print(c)
    print(c/r)
    print((17 - 5j) / (20 + 10j))
    print('#############################')
    print(4j/(17-5j))
    print('4i'/c)
    print(sqrt(Complex(1.23, 3.45)))
    print(sqrt(4))