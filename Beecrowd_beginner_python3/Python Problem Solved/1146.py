while True:
    X = int(input())
    
    if X == 0:
        break
    output = ""
    
    for i in range(1, X+1):
        output += str(i) + " "
    print(output[:-1])
