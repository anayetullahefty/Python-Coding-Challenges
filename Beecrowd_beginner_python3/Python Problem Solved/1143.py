#1143 - Squared and Cubic

num = int(input())
count = 1

if (1<num<1000):
    for i in range(1, num+1):
        print(f"{i} {i*i} {i*i*i}")
