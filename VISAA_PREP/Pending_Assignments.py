X, Y, Z = map(int, input().split())
new = X*Y
day_min = Z*1440
if new<= day_min:
    print("YES")
else:
    print("NO")
