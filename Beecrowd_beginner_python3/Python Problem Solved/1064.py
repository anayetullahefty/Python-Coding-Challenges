#1064 - Positives and Averagecount = 0
avg = 0

for i in range(6):
    value = float(input())
    if value >0:
        count += 1
        avg += value
print(f'''{count} valores positivos
{(avg/count):.1f}''')
