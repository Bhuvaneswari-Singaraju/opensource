a, b = input().split()
if (a == 'S' and b == 'P') or (a == 'R' and b == 'S') or (a == 'P' and b == 'R'):
    print("Vignesh")
elif (b == 'S' and a == 'P') or (b == 'R' and a == 'S') or (b == 'P' and a == 'R'):
    print("Charan")
else:
    print("NULL")
