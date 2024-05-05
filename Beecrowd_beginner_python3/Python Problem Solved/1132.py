# 1132 - Multiples of 13
X = int(input())
Y = int(input())

# Initialize sum
result = 0

# Ensure X is smaller than Y
if X > Y:
    X, Y = Y, X

for num in range(X, Y + 1):
    # Check if the number is not divisible by 13
    if num % 13 != 0:
        result += num

print(result)
