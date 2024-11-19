S = input()
vowels = 'aeiouAEIOU'
count = 0
count2 = 0
for i in S:
    if i in vowels:
        count += 1
    elif i.isalpha():
        count2 += 1
print(f"{count},{count2}")
