# 1051 - Taxes
a = float(input())-2000

if a<=0:
    print("Isento")
elif a<=1000:
    tax = (a*8)/100
    print(f"R$ {tax:.2f}")
elif a<=2500:
    tax = ((1000*8)/100) + (((a-1000)*18)/100)
    print(f"R$ {tax:.2f}")
else:
    tax = ((1000*8)/100) + ((1500*18)/100)+ (((a-2500)*28)/100)
    print(f"R$ {tax:.2f}")
