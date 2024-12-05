from math import log2

N = 2401

def teste(N):
    n = N.bit_length() # limite superior para b
    y = int(log2(N))
    for b in range(2, n+1):
        x = y/b
        u1 = int(2**x)
        u2 = u1 + 1

        if u1**b == N:
            return u1, 'a**b'
        elif u2**b == N:
            return u2, 'a**b'
        
print(teste(N))