A = 270
B = 192


def gcd(a, b):
    while (a != 0) and (b != 0):
        r = a % b
        a = b
        b = r
    return a


print (gcd(A, B))
