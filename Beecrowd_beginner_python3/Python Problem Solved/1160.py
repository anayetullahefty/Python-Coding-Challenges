#1160 - Population Increase
N = int(input())

for i in range(N):
    pa,pb,g1,g2 = input().split()
    PA = int(pa)
    PB = int(pb)
    G1 = float(g1)
    G2 = float(g2)
    count = 0

    while (PA<=PB):
        CPA = int(PA*(G1/100))
        CPB = int(PB*(G2/100))
        count +=1
        PA += CPA
        PB += CPB
        if count>100:
            break
    if count>100:
        print("Mais de 1 seculo.")
    else:
        print(f"{count} anos.")
