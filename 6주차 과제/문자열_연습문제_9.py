A, B = input().split()

A = A + A + A

if B in A:
    print(A + B)
else:
    print(A + B + B)
