N = int(input())
arr = list(map(int, input().split()))
peri = -1
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            if arr[i]+arr[j] > arr[k] and arr[i]+arr[k] > arr[j] and arr[j]+arr[k]>arr[i]:
                perimeter = arr[i] + arr[j]+arr[k]
                peri = max(perimeter, peri)
print( peri)
