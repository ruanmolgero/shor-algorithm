import ket
from math import log2
from random import randint

# 1. Se N for par, retorne o fator 2.
# 2. Determine, de forma clássica, se N = a^b para a ≥ 1 e b ≥ 2.
#   Se for o caso, retorne o fator a (isso pode ser feito em tempo polinomial).
# 3. Escolha um número aleatório g tal que 1 < g ≤ N−1. Usando o algoritmo de Euclides,
#   determine se gcd(a, N) > 1. Se for o caso, retorne o fator gcd(g,N).
# 4. Use o algoritmo quântico de busca de ordem definido na seção 2.2 para encontrar a
#   ordem r de a mod  N.
# 5. Se r for ímpar ou, se r for par mas gr/2 ≡ −1(mod  N), volte para o passo (iii).
#   Caso contrário, compute gcd(gr/2 − 1, N) e gcd(gr/2 + 1, N). Verifique se algum desses
#   valores é um fator não trivial de N. Se for, retorne o fator. Senão, volte ao passo (iii)


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


def shor(N):
    # 1. Caso Trivial
    if N % 2 == 0:
        return 2

    # 2. Caso onde N = a^b
    n = N.bit_length()  # limite superior para b
    y = int(log2(N))
    for b in range(2, n+1):
        x = y/b
        u1 = int(2**x)
        u2 = u1 + 1

        if u1**b == N:
            return u1, 'a**b'
        elif u2**b == N:
            return u2, 'a**b'

    for _ in range(n):
        try:
            # 3. Caso onde gcd(a, N) > 1
            x = randint(2, N-1)
            g = gcd(x, N)
            if g > 1:
                return g, 'lucky'

            def quantum_order_finding(N, a):
                pass
        except:
            continue

    return N, 'prime or failed'
