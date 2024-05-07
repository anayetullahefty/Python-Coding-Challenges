#1154 - Ages

age = []

while True:
    N = int(input())
    
    if N <0:
        break
    else:
        age.append(N)
avg = sum(age)/len(age)
print(f"{avg:.2f}")
