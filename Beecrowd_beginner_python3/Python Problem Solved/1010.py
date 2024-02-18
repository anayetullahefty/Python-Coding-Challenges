#Reading the code, unit and price of product 1
code_1, unit_1, price_1 = input().split(" ")

#Reading the code, unit and price of product 2
code_2, unit_2, price_2 = input().split(" ")

total_price = ( ( int(unit_1) * float(price_1) ) 
              + ( int(unit_2) * float(price_2) ) )

print('VALOR A PAGAR: R$ %0.2f' %total_price)


'''
#Reference
1. https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/
2. https://developer.rhino3d.com/guides/rhinopython/python-statements/
'''
