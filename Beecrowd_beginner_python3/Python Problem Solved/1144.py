#1144 - Logical Sequence

num = int(input())

if 1<num<1000:
    for i in range(1, num+1):
        print(f"{i} {i*i} {i*i*i}")
        print(f"{i} {(i*i)+1} {(i*i*i)+1}")
