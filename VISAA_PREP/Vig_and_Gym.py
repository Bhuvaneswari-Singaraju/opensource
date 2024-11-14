X, Y, Z = map(int, input().split())
Y = X+Y
if X<Z:
    if Y<= Z:
        print("2")
    else:
        print("1")
else:
    print("0")
