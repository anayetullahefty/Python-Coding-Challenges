#1048 Salary Increase

CurrentSalary = float(input())

if CurrentSalary<=400:
    percentage = 15
elif CurrentSalary<=800:
    percentage = 12
elif CurrentSalary<=1200:
    percentage = 10
elif CurrentSalary<=2000:
    percentage = 7
else :
    percentage = 4

earn = CurrentSalary * percentage/100
NewSalary = CurrentSalary + earn

print(f'''Novo salario: {NewSalary:.2f}
Reajuste ganho: {earn:.2f}
Em percentual: {percentage} %''')
