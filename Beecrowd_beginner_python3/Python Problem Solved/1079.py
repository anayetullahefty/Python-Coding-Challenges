#beecrowd | 1079 Weighted Averages

for i in range(int(input())):
    a,b,c = map(float,input().split())
    result = ((a*2)+(b*3)+(c*5))/(2+3+5)
    print(f"{result:.1f}")

    #print('%.1f' %result)
