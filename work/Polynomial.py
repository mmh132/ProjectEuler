from math import pi, cos, sin, log2, ceil

def fft(coeffs, inv):
    size = len(coeffs)

    if size == 1:
        return [coeffs[0]]
    
    angle = -2*pi/size*(-1 if inv else 1)

    w,wn = complex(1,0), complex(cos(angle), sin(angle))

    even, odd = [],[]
    for i in range(size):
        if i & 1:
            odd.append(coeffs.pop(0))
        else:
            even.append(coeffs.pop(0))

    fftEven, fftOdd = fft(even, inv), fft(odd, inv)

    new = [0]*size

    for i in range(size//2):
        new[i] = fftEven[i] + w*fftOdd[i]
        new[i + size//2] = fftEven[i] - w*fftOdd[i]
        if inv:
            new[i] /= 2
            new[i + size//2] /= 2
        w *= wn
    return new


def product(polya, polyb):
    size, rsize = 1, len(polya) + len(polyb)
    while size < rsize:
        size *= 2

    while len(polya) < size:
        polya.append(0)
    
    while len(polyb) < size: 
        polyb.append(0)
    
    fftA = fft(polya, False)
    fftB = fft(polyb, False)

    for i in range(size):
        fftA[i] *= fftB[i]
    
    rv = fft(fftA, True)

    return [round(i.real) for i in rv][:rsize - 1 - size]
