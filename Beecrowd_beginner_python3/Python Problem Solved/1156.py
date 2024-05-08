#1156 - S Sequence II

result = 0
divisor = 1
power = 0

while (divisor < 40):
    dividend = 2**power
    S = divisor / dividend
    
    #print(f"{divisor}/{dividend}")

    result += S
    divisor += 2
    power += 1 
    
print(f"{result:.2f}")
