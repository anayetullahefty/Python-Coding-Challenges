#1179 - Array Fill IV

# Initialize arrays for even and odd numbers
par = []
impar = []

# Read 15 numbers
for _ in range(15):
    num = int(input())
    if num % 2 == 0:
        # Add even numbers to the 'par' array
        par.append(num)
        # If 'par' array is full, print its contents and reset it
        if len(par) == 5:
            for i, n in enumerate(par):
                print(f"par[{i}] = {n}")
            par = []
    else:
        # Add odd numbers to the 'impar' array
        impar.append(num)
        # If 'impar' array is full, print its contents and reset it
        if len(impar) == 5:
            for i, n in enumerate(impar):
                print(f"impar[{i}] = {n}")
            impar = []

# Print any remaining numbers in the 'impar' array
for i, n in enumerate(impar):
    print(f"impar[{i}] = {n}")

# Print any remaining numbers in the 'par' array
for i, n in enumerate(par):
    print(f"par[{i}] = {n}")
