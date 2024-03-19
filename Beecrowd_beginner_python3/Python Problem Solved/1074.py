#1074 - Even or Odd

for i in range(int(input())):
    value = int(input())
    if value>0:
        if value % 2 == 0 :
            print("EVEN POSITIVE")
        else: print("ODD POSITIVE")
    elif value<0:
        if value % 2 == 0 :
            print("EVEN NEGATIVE")
        else: print("ODD NEGATIVE")
    elif value == 0:
        print("NULL")
