
print("Learning python lists")

fruitList = ["apple", "banana", "cherry", "strawberry"]
print(fruitList)

for fruit in fruitList:
    print("####")
    print(fruit)

numberlist = [100, 200, 300, 400, 1000]
print (numberlist)
total = 0
for number in numberlist:
    print (number)
    total = total + number

print (total)

sum = 0
average=0
count = 0
newlist = [500,555,577,588,22,599,600]
for number in newlist:
    sum = sum + number
    if (count == 0):
       min = number
    elif (number < min):
       min = number
    count = count + 1

average = sum / len(newlist)
print (average)
print (min)

