N = int(input())
s = input()
t = input()
Ds = {}
Dt = {}
for i in range(N):
    if s[i] in Dt:
        if Dt[s[i]] != t[i]:
            print("false")
    else:
       Dt[s[i]] = t[i]
    if t[i] in Ds:
        if Ds[t[i]] != s[i]:
            print("false")
    else:
        Ds[t[i]] = s[i]
else:
    print("true")
        
