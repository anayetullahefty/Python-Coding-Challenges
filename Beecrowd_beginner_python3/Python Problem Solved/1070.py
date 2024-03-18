#1070 - Six Odd Numbers

num = int(input())
odd = []
while True:
    if num % 2 == 1:
        print(num)
        odd.append(num)
        if len(odd)== 6:
            break
    num +=1
