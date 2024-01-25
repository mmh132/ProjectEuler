from math import sin, cos, pi

#dft on vector a
def fft(a):
    #find floor(log_2(len(a))), i.e. the length of the return vector
    l = 1
    lg2 = 0
    while l < len(a):
        l <<= 1
        lg2 += 1
    
    #pad a with zeroes so its length 2**something
    while len(a) < l:
        a.append(0)
    
    #fft recursive tree looks like bit reversal, so compute bit reversals
    rev = [0]*(l)
    for i in range(1, l):
        rev[i] = (rev[i >> 1] >> 1) + ((i&1) << (lg2 - 1))
        
    #precompute roots of unity. since we never use roots of unity with i > l/2 so we reorder
    #reordering [k .. 2*k - 1] to upper roots order 2*k
    roots = [0]*l
    for i in range(l >> 1):
        w = 2*pi*i/l
        roots[i + (l >> 1)] = complex(cos(w), sin(w))
    for i in range((l >> 1) - 1, 0, -1):
        roots[i] = roots[2 * i]

    #do the bit reversal
    out = [a[rev[i]] for i in range(l)]
    
    #bitshifting magic b/c of the structure of the fft recursion tree
    for k in range(lg2):
        for i in range(0, l, 1 << (k + 1)):
            for j in range(1 << k):
                z = roots[j + (1 << k)]*out[i + j + (1 << k)]
                out[i + j + (1 << k)] = out[i + j] - z
                out[i + j] = out[i + j] + z
        
    return out

