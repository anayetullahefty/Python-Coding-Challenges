# 1165 Prime Number

N = int(input())

for i in range(N):
    X = int(input())
    count = 0

    for i in range(1, X+1):
        if X % i == 0:
            count+=1
    if count>2:
        print(f"{X} nao eh primo")
    else:
        print(f"{X} eh primo")
