a,b,c,d = map(int,input().split())

start = (a*60)+b # convart in minute
end = (c*60)+d # convart in minute

diff = end - start
if diff<=0:
    diff = diff + 24*60

hour = int(diff/60)
minute = diff % 60

print(f"O JOGO DUROU {hour} HORA(S) E {minute} MINUTO(S)")
