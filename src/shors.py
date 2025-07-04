from util import *
from qubit import np

def shor(N):
    from random import randint

    if N % 2 == 0:
        return 2
    a = randint(2, N - 1)
    if gcd(a, N) > 1:
        return gcd(a, N)

    # Find period r of f(x) = a^x mod N
    Q = 2 ** 5  # Use power of 2 for QFT
    xs = np.arange(Q)
    fxs = np.array([pow(a, int(x), N) for x in xs])

    # Simulate the output of QFT (use classical FFT here)
    f_transform = np.fft.fft(fxs)
    measured = np.argmax(np.abs(f_transform))
    frac = measured / Q
    r = continued_fraction(frac)

    factor = is_nontrivial_factor(a, r, N)
    if factor:
        return factor
    return None