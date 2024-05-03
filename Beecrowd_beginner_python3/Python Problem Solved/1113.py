#1113 - Ascending and Descending

X, Y = map(int,input().split())

while True:
    if X==Y :
        break
    elif X>Y:
        print("Decrescente")
    elif Y>X:
        print("Crescente")
    X, Y = map(int,input().split())
