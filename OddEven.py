from math import remainder


number = int(input("Enter the number: "))
remainder = number % 2
if(remainder == 0):
    print(number,"is an even number")
else:
    print(number,"is an odd number")