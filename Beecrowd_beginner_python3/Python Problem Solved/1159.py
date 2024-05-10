#1159 - Sum of Consecutive Even Numbers

while True:
    X = int(input())
    total = 0
    count = 0

    # Stop if X is zero
    if X == 0:
        break

    # Iterate to find the sum of five consecutive even numbers from X
    while (count<5):
        if X % 2 == 0:
            total += X
            count += 1
        X += 1
    print(total)

