N = input()
op = ""
count = 1
for i in range(1,len(N)):
    if N[i] == N[i-1]:
        count = count + 1
    else:
        op += N[i-1] + str(count)
        count = 1
op += N[-1] + str(count)
print(op)
