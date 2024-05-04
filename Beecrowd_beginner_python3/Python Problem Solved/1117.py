#1117 - Score Validation

count = 0
total = 0

while count<2:
     score = float(input())

     if 1<= score <= 10:
          total += score
          count += 1
     else:
          print(f"nota invalida")
          
result =total/2
print(f"media = {result:.2f}")
