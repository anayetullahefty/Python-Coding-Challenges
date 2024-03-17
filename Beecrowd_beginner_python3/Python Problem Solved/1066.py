#1066 - Even, Odd, Positive and Negative

even = odd = positive = negative = 0

for i in range(5):
    value = float(input())
    if value % 2 == 0:
        even += 1
    else:
        odd += 1
    if value >0:
         positive+=1
    elif value<0:
        negative+=1

print(f'''{even} valor(es) par(es)
{odd} valor(es) impar(es)
{positive} valor(es) positivo(s)
{negative} valor(es) negativo(s)''')


