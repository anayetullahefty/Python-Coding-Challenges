#1116 - Dividing X by Y

for i in range(int(input())):
    X,Y= map(int,input().split())
    
    if Y==0: print("divisao impossivel")
    
    else:
        ans = (X/Y)
        print(f"{ans:.1f}")
