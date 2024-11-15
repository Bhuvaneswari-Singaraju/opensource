N,X,Y = map(int,input().split())
if Y <= N*X:
    if Y % X == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
