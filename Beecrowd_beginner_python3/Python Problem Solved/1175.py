#1175 - Array change I

a = []

for i in range(20):    
    N = int(input())
    a.append(N)

count = 0
for j in a[::-1]:
    print(f"N[{count}] = {j}")
    count += 1
