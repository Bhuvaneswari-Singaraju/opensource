n = int(input())
reverse = str(abs(n))[::-1]
new = int(reverse)
if n<0:
    new = -new
if new<-pow(2, 31) or new> pow(2, 31)-1:
    print(0)
else:
    print(new)
