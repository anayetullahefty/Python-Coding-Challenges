#1164 - Perfect Number

N = int(input())

for i in range(N):
    X = int(input())
    divisors_sum = 0

    for i in range(1, X):
        if X % i == 0:
            divisors_sum += i
    if divisors_sum == X:
        print(f"{X} eh perfeito")
    else:
        print(f"{X} nao eh perfeito")
