A, B = input().split()
A = int(A)
B = int(B)

if A >= 12:
    C = "PM"
else:
    C = "AM"

if A >= 13:
    A = A - 12

if A < 10:
    print("0", A, ":", B, C)
else:
    print(A, ":", B, C)
