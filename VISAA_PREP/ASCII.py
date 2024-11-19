S = input()
new = ''
for i in S:
    if i.isupper():
        new += i.lower()
    elif i.islower():
        new += i.upper() 
    else:
        new += i
print(new)
