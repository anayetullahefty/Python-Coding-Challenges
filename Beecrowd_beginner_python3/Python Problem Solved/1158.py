#1158 - Sum of Consecutive Odd Numbers III

N = int(input())

for i in range(N):
    X, Y = map(int,input().split())
    total = 0
    count =0

    while (count<Y):
        if X % 2 != 0:
            total += X
            count +=1
        X +=1
    print(total)
