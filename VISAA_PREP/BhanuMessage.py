num = input()
if num[0] == '+' and " " in num[1:]:
    space = num.index(" ")
    country = num[1:space]
    phn = num[space+1:]
    if country.isdigit() and len(country)== 2:
        if phn.isdigit() and len(phn) == 10:
            print("Correct")
        else:
            print("Incorrect")
    else:
        print("Incorrect")
else:
    print("Incorrect")
