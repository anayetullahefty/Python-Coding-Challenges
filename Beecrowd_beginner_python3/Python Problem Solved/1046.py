#1046		Game Time
a,b = map(int,input().split())

if a<b:
    time = b-a
    print(f"O JOGO DUROU {time} HORA(S)")
else:
    time = (24-a)+b
    print(f"O JOGO DUROU {time} HORA(S)")
