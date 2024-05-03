m,n = map(int,input().split())

while True:
    if (m<=0) or (n<=0):
        break

    else:
        M = min(m,n)
        N = max(m,n)
        result = []
        for i in range(M, N+1):
            result.append(i)
        Output = ' '.join(map(str,result))
        print(f"{Output} Sum={sum(result)}")
    
    m,n = map(int,input().split())
