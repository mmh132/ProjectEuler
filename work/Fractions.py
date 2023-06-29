from math import gcd

class fraction:
    def __init__(self, n, d) -> None:
        self.n = n
        self.d = d
    
    def __str__(self) -> str:
        out = str()
        out += str(self.n)
        out += "/"
        out += str(self.d)
        return out
    
    def __add__(self, oFrac):
        newN = self.n*oFrac.d + oFrac.n*self.d
        newD = self.d*oFrac.d
        g = gcd(newN, newD)
        return fraction(newN//g, newD//g)
    
    def __sub__(self, oFrac):
        newN = self.n*oFrac.d - oFrac.n*self.d
        newD = self.d*oFrac.d
        g = gcd(newN, newD)
        return fraction(newN//g, newD//g)
    
    def __mul__(self, oFrac):
        if oFrac.n == 0 or self.n == 0: return fraction(0,1)
        newN = self.n*oFrac.n
        newD = self.d*oFrac.d
        g = gcd(newN, newD)
        return fraction(newN//g, newD//g)
    
    def __truediv__(self, oFrac):
        temp = int()
        temp = self.n
        self.n = self.d
        self.d = temp
        return self*oFrac

    def __pow__(self, e):
        if e == 0:
            return fraction(1,1)
        elif e<0:
            temp = int()
            temp = self.n
            self.n = self.d
            self.d = temp
            return self**abs(e)
        else:
            self.n = self.n ** e
            self.d = self.d ** e
            g = gcd(self.n, self.d)
            return fraction(self.n//g, self.d//g)
        
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

    def __neg__(self):
        self.n = -1*self.n
        return self
    
