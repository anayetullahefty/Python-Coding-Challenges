#1118 - Several Scores with Validation

while True:
    count = 0
    total = 0
    while count<2:
        score = float(input())
        if (score >= 0 and score <= 10):
            total += score
            count += 1
        else:
            print(f"nota invalida")
    print("media = %.2f" % (total / 2))
    option = 0
    while True:
        print("novo calculo (1-sim 2-nao)")
        option = int(input())

        if option == 1 or option==2:
            break
    if option == 2:
            break
