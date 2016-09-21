A = 270
B = 192


def GCD(A,B):
    while (A, B) != 0:
        print A / B
        r = A % B
        A = B
        B = r
print A
