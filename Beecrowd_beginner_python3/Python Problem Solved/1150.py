#1150 - Exceeding Z

X = int(input())

while True:
    Z = int(input())
    if Z>X:
        break
count = 0
output = 0
for i in range(X,Z):
    output += i
    count +=1
    if output>Z:
        break
print(count)
