#r
strFullname = "Keira Marie"
NewValue = strFullname.upper()
print(NewValue)
NewValue = strFullname.count ("m")
print(NewValue)


#joim
strfirstname = "Keira Marie"
strmiddlename= "Mot"
strlastname= "Fukiko"
strfullname = "_".join([strfirstname, strmiddlename, strlastname])
print(strfullname)

NewValue = strFullname.isnumeric()
print(NewValue)

NewValue = strFullname[0:11]
print(NewValue)
NewValue = strFullname[0:11:2]
print(NewValue)

print(strFullname.index("e"))
print(strFullname.index("e", 0, 12))
print(strFullname.index("e", 6, 12))

#
citizenship = "Filipino"
age = 18
registered = True

if citizenship == "Filipino" and age >= 18:
    if registered:
        print("You can vote")
    else:
        print("You can not vote but you can reister now")
elif citizenship == "Filipino" and age < 18:
    if registered:
        print("You cannot. Please wait until you are eligible and then register.")
    else:
        print("You cannot vote nor register")


fruitlist = ["grapes", "durian", "cherry", "orange", "mango"]

for fruit in fruitlist:
    print("fruit list include #: " + fruit)

print("after loop")
#
myString = "ibaliknyocodesko"
for char in myString:
    print(char.upper())

print("after loop")

myGrade = float(input("Enter your grade: "))


if myGrade >= 97:
    print("Grade is greater than 1.0")
elif myGrade >= 94:
    print("Grade is greater than 1.25")
elif myGrade >= 88:
    print("Grade is greater than 1.50")
elif myGrade >= 85:
    print("Grade is greater than 1.75")
elif myGrade >= 82:
    print("Grade is greater than 2.0")
elif myGrade >= 79:
    print("Grade is greater than 2.25")
elif myGrade >= 76:
    print("Grade is greater than 2.5")
elif myGrade >= 75:
    print("Grade is greater than 3.0")
elif myGrade >= 65:
    print("Grade is greater than 5.0")
else:
    print("5.0/INC/W/D")

print("before loop")

for x in range(0, 67, 5):
    print("x value is : " + str(x))

print("after loop")

#
print("before loop")
for x in range(67):
    print("x value is : " + str(x))

print("after loop")
#
print("before loop")

for x in range(0, 67):
    print("x value is : " + str(x))

print("after loop")
