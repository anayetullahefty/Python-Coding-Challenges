#11153 - Simple Factorial

N = int(input())

result = 1

for i in range(N):
    result *= (N-i)
print(result)
