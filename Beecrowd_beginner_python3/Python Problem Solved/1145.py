n1,n2 = list(map(int,input().split()))
cont = 1
end = (int((n2/n1))+1)
for i in range(1,end):
    r = ""
    for y in range(n1):
        r += str(cont) + " "
        cont += 1
    print(r[:-1])
