#1134 - Type of Fuel

Alcool = 0
Gasolina = 0
Diesel = 0

while True:
    fuel_type = int(input())
    if fuel_type == 4: break
    elif fuel_type == 1:
        Alcool += 1
    elif fuel_type == 2:
        Gasolina += 1
    elif fuel_type == 3:
        Diesel += 1
    else: continue
print("MUITO OBRIGADO")
print(f"Alcool: {Alcool}")
print(f"Gasolina: {Gasolina}")
print(f"Diesel: {Diesel}")

