from math import sqrt, floor
def approx(n):
    sf = floor((sqrt(n) - floor(sqrt(n))) * 10**12)
    sf = sf - floor(sf) + 1
    
    
    