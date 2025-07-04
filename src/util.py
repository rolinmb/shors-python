from math import gcd

def continued_fraction(x, max_den=32):
    from fractions import Fraction
    return Fraction(x).limit_denominator(max_den).denominator

def is_nontrivial_factor(a, r, N):
    if r % 2 != 0:
        return None
    x = pow(a, r // 2, N)
    f1 = gcd(x - 1, N)
    f2 = gcd(x + 1, N)
    if 1 < f1 < N:
        return f1
    if 1 < f2 < N:
        return f2
    return None

if __name__ == "__main__":
    pass