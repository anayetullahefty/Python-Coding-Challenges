#1133 - Rest of a Division

num1 = int(input())
num2 = int(input())

# Ensure X is smaller than Y
if num1>num2:
    num1,num2 = num2,num1

for i in range(num1+1,num2):
    if (i % 5 == 2) or (i % 5 == 3):
        print(i)
