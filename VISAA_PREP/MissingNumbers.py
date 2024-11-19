def missingNumbers(arr, brr):
    arr1 = {}
    brr1 = {}
    miss = []
    for i in arr:
        if i in arr1:
            arr1[i] += 1
        else:
            arr1[i] = 1
    for i in brr:
        if i in brr1:
            brr1[i] += 1
        else:
            brr1[i] = 1
    for i in brr1:
        if i not in arr1 or brr1[i] >arr1[i]:
            miss.append(i)
    return sorted(miss)
