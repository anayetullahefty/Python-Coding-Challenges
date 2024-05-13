1180 - Lowest Number and Position

# Read the size of the array
N = int(input())

# Read the elements of the array
X = list(map(int, input().split()))

# Find the smallest element and its position
min_value = min(X)
min_index = X.index(min_value)

# Print the result
print(f"Menor valor: {min_value}")
print(f"Posicao: {min_index}")
