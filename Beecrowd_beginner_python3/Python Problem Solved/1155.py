#1155 - S Sequence

elements = 0

for i in range(1,101):
    S = 1 / i
    elements += S

print(f"{elements:.2f}")
