#Mixing data types
#Can't print string + int at same time
#Solved by typecasting - Turned int age into string with str()

name = "Jack"
age = 33
month = 9

print(name)
print(month)

print(name + " " + str(age))

print(str(age) + " " + name + " " + str(month))
