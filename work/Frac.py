from math import gcd

class fraction:
    def __init__(self, n, d):
        self.n = n
        self.d = d
    
    def __str__(self):
        return "%s/%s" % (self.n, self.d)
    
    def reduce(self):
        if self.n < 0 and self.d < 0: 
            self.n = abs(self.n)
            self.d = abs(self.d)
        if self.n == 0:
            return fraction(0,1)
        g = gcd(self.n, self.d)
        self.n //= g
        self.d //= g
        return self
    
    def abs(self):
        newFrac = fraction(abs(self.n), abs(self.d))
        return newFrac
    
    def __add__(self, oFrac):
        if type(oFrac) == int:
            oFrac = fraction(oFrac, 1)
        self.n = self.n * oFrac.d + oFrac.n * self.d
        self.d *= oFrac.d
        self.reduce()
        return self
    
    def __sub__(self, oFrac):
        if type(oFrac) == int:
            oFrac = fraction(oFrac, 1)
        self.n = self.n * oFrac.d - oFrac.n * self.d
        self.d *= oFrac.d
        self.reduce()
        return self
    
    def __mul__(self, oFrac):
        if type(oFrac) == int:
            oFrac = fraction(oFrac, 1)
        self.n *= oFrac.n
        self.d *= oFrac.d
        self.reduce()
        return self
    
    def __truediv__(self, oFrac):
        if type(oFrac) == int:
            oFrac = fraction(oFrac, 1)
        self.n *= oFrac.d
        self.d *= oFrac.n
        self.reduce()
        return self

    def __pow__(self, e):
        if e > 0:
            self.n = self.n ** e
            self.d = self.d ** e
            self.reduce()
            return self
        elif e < 0:
            self.n, self.d = self.d, self.n
            return self ** abs(e)
        else: 
            self.n = 1
            self.d = 1
            return self
        
    def __eq__(self, oFrac):
        return self.n == oFrac.n and self.d == oFrac.d
    
    def __lt__(self, oFrac):
        return self.n*oFrac.d < oFrac.n*self.d
    
    def __gt__(self, oFrac):
        return self.n*oFrac.d > oFrac.n*self.d
    
    def __le__(self, oFrac):
        return self == oFrac or self < oFrac

    def __ge__(self, oFrac):
        return self == oFrac or self > oFrac
    
    def __ne__(self, oFrac):
        return not self == oFrac

    def __neg__(self):
        self.n = -1*self.n
        return self
    

print(fraction(1655, 1090000000) < fraction(123, 10000032))