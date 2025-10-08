print("1st exercise")
# Average temperature
weekTemp = [25, 35, 26, 21, 22, 36, 41]
avrg = sum(weekTemp)/len(weekTemp)
print("The average temperature is", avrg)

# Below or above average
for temperature in weekTemp:
    if temperature >= avrg:
        print(temperature, "is above average")
    else:
        print(temperature, "is below average")

print("\n2nd exercise")

# Student lists
coreStudents = ["Max", "Luke", "Will", "Michael", "Justin", "Jane"]
valedictorian = [83, 91, 58, 90, 100, 64]
dice = sum(valedictorian)/len(valedictorian)
print("The students' average grade is", dice)

# Percentage
passCount = 0
for grade in valedictorian:
    if grade >= 70:
        passCount = passCount + 1
    
print("Percentage of students that passed:", (passCount/len(coreStudents) * 100))

# Failed students
passed = [(name, grade) for name, grade in zip(coreStudents, valedictorian) if grade < 70]
for name, grade in passed:
    print(name,"'s grade is", grade)

print("\n3rd exercise")

# Shopping List
groList = ["maple syrup", "band-aids", "eggs", "waffles", "apple juice", "olive oil"]
ijbol = [True, False, True, False, False, False]

# Purchased items
print("Shopping list (pending):")

for i in range(len(groList)):
    if not ijbol[i]:
        inP = input(f"Have you already bought {groList[i]}? (y/n) ").strip().lower()
        if inP in ["y", "yes"]:
            ijbol[i] = True

# New list
print("\nUpdated shopping list:")
for i in range(len(groList)):
    if not ijbol[i]:
        print("-", groList[i])

print("\n4th exercise")

# Numbers
randoDice = [18, 9, 70, 53, 36, 15]
maxEn = max(randoDice)
print("The highest value is", maxEn)
minOh = min(randoDice)
print("The lowest value is", minOh)

# Ordering
randoDice.sort()
print("Numbers in order:", randoDice)

print("\n5th exercise")

# Even and odd
ctFu = [12, 7, 39, 75, 50, 26]
for num in ctFu:
    if (num % 2) == 0:
        print(num, "is an even number")
    else:
        print(num, "is an odd number")

print("\n6th exercise")

# Usernames
botPin = ["frandy", "bunsout", "cloudstrife", "lixboom", "whlrs", "bunsout"]

while True:
    pers = input("What's your username? ").strip().lower()
    if pers in botPin:
        print("That username is taken. Try again\n")
    else:
        botPin.append(pers)
        print(pers, "has been registered successfully")
        print("Username list:", botPin)