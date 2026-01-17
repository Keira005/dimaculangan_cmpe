strFullName = "Keira Justine Dimaculangan"
newValue = strFullName.upper()
print(newValue)

newValue = strFullName.count("a")
print(newValue)

newValue = strFullName.split(" ")
print(newValue)
newValue = strFullName.split("a")
print(newValue)
newValue = strFullName.split("bby")
print(newValue)

newValue = strFullName.replace("Kei", "Cute")
print(newValue)

# join
FirstName = "Keira Justine"
LastName = "Dimaculangan"
FullName = "_".join([FirstName, LastName])
print(strFullName)

newValue = strFullName.isnumeric()
print(newValue)

 #substring
newValue = strFullName[2:9]
print(newValue)
newValue = strFullName[2:9:2]
print(newValue)
#return the lowest index available
print(strFullName.index("H"))
print(strFullName.index("H", 2,9))