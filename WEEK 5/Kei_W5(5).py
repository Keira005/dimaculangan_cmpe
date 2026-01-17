isPresent = False
isExist = True
isAvailable = "True"
isValid = 5
isOkay = 10
isNumeric = False
myChar = "5"
isNumeric = myChar.isnumeric()
strIsNumeric = str(myChar.isnumeric())
print([isNumeric])
print([strIsNumeric])


a = 5
b = 10
isEqual = (a == b)
print(isEqual)
isGTE = (a >= b)
print(isGTE)
isLTE = (a <= b)
print(isLTE)

isIn = (5 in [5, 10, 15, 10, 25, 30])
print(isIn)
isIn = (0 in [0, 1, 2, 3, 4, 5])
print(isIn)
isIn = ("hello" in  "hello world im here")
print(isIn)

isIS = ("hello" is "hello")
print(isIS)
isIS = ("hello" is "hi hello bye")
print(isIS)

IsIn = ((5 in [25, 45, 23, 12, 5, 27]) and (5 in [25, 45, 23, 12, 27]))
print(IsIn)
IsIn = ((5 in [25, 45, 23, 12, 5, 27]) or (5 in [25, 45, 23, 12, 27]))
print(IsIn)

isGroupPassed = False
passingGrade = 85
markGrade = 75
jennyGrade = 95
arthurGrade = 86
isMarkPassed = markGrade >= passingGrade
print(isMarkPassed)
isJennyPassed = jennyGrade >= passingGrade
print(isJennyPassed)
isArthurPassed = arthurGrade >= passingGrade
print(isArthurPassed)
isGroupPassed = isMarkPassed and isJennyPassed and isArthurPassed
print(isGroupPassed)
isGroupPassed = isMarkPassed or isJennyPassed or isArthurPassed
print(isGroupPassed)


isGroupPassed = False
passingGrade = 85
markGrade = 75
jennyGrade = 95
arthurGrade = 86
isMarkPassed = markGrade >= passingGrade
print(isMarkPassed)
isJennyPassed = jennyGrade >= passingGrade
print(isJennyPassed)
isArthurPassed = arthurGrade >= passingGrade
print(isArthurPassed)
isGroupPassed = isMarkPassed and isJennyPassed and isArthurPassed
print(isGroupPassed)
isGroupPassed = isMarkPassed or isJennyPassed or isArthurPassed
print(isGroupPassed)


intA = 555
intB = 5
intC = 4

isDivisible = False #initial value
remainder = intA % intB #modulus or the percent sign returns the remainder
print(remainder)
if remainder == 0:
    isDivisible = True
print(isDivisible)

isDivisible = False #initial value <--------------------------------------
remainder = intA % intC
print(remainder)
if remainder == 0:
    isDivisible = True
print(isDivisible)