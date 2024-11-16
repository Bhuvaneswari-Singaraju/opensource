try:
    N = int(input())
    arr = list(map(int, input().split()))
    if len(arr)!=N:
        exit()

    k = int(input())
    op = "false"
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == k:
                op = "true"
                break
        if op == "true":
            break
    print(op)
except ValueError:
    print("true")
