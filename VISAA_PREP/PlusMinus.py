def plusMinus(arr):
    count1 = 0
    count2 = 0
    count3 = 0
    for i in arr:
        if i == 0:
            count1 += 1
        elif i < 0:
            count2 += 1
        else:
            count3 += 1
    lt = len(arr)
    res1 = count1/lt
    res2 = count2/lt
    res3 = count3/lt
    print(f"{res3:.6f}")
    print(f"{res2:.6f}")
    print(f"{res1:.6f}")
