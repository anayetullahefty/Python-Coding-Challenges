#1072 - Interval 2

in1 = 0
out = 0

for i in range(int(input())):
    num = int(input())
    if num>=10 and num <=20:
        in1 +=1
    else:
        out +=1
print(f'''{in1} in
{out} out''')
