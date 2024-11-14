X = int(input())
off = X*(0.10)
dis = 100
if off > dis:
    X = X-off
else:
    X = X-100
print(int(X))
