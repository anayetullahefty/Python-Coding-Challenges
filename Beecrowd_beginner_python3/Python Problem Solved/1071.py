#1071 - Sum of Consecutive Odd Numbers I

start = int(input())
stop = int(input())
sum= 0

for i in range(start-1, stop, -1):
    if i % 2 != 0 :
        sum += i
print(sum)
