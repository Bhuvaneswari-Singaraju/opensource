T = int(input())
for i in range(1,T+1):
    X, N = map(int, input().split())
    eachPt = X/10
    score = eachPt * N
    print(int(score))
    
