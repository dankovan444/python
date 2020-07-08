while True:
    choice = input ("enter(C,F):")
    if choice in ('c','f'):
        num1 = float(input("Enter first number: "))
        if choice == 'c':
            print ((num1*(9/5))+32)
        if choice == 'f':
            print ((num1-32)*(5/9))

#celsius = 30
# fahrenheit = celsius * (9/5) + 32
# print (fahrenheit)
#
# f = 70
# celsius = (f - 32) * 5/9
# print (celsius)





