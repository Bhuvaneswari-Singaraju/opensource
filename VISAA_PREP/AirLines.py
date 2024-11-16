X, Y = map(int, input().split())
planes = X * 100
req = Y - planes

if planes >= Y:
    print(0)
else:
    rem = (req + 99)//100
    print(int(rem))
