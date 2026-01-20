shoesA = ["Adidas", "Puma", "Nike", "Converse", "Vans"]
print(shoesA)
print(shoesA[2])
print(shoesA.index("Gon"))
isThere = "Gon" in shoesA
print(isThere)
shoesA.append("New Balance")
print(shoesA)
shoesA.insert(3, "Chrolo")
print(shoesA)
print(len(shoesA))
print(shoesA.count("Nike"))
shoesA.remove("Converse")
print(shoesA)
print(shoesA.index("Kurapika"))
shoesA[1] = "Hisoka"
print(shoesA)


#LIST #MUTABLE #CRUD - CREATE(append/insert) READ(view)
#UPDATE(assigned) and DELETE(remove/clear)
chocolatesA = ["Twix", "Toblerone", "Kitkat", "Bounty", "Dairy Milk"]
chocolatesB = ["Snickers", "Bueno", "Mars", "Ferrero", "Kisses"]
chocolatesC = ["Meiji", "Salcov", "Auro", "Choco Choco", "Super sticks"]


Chocolates_list = [chocolatesA, chocolatesB, chocolatesC]
print(Chocolates_list) #list of a list
print(Chocolates_list[2])
print(Chocolates_list[2][1])


Chocolates_Plus = chocolatesA + chocolatesB + chocolatesC
print(Chocolates_Plus)


chocolatesA.extend(chocolatesB)
chocolatesA.extend(chocolatesC)
print(chocolatesA)


#SET #MUTABLE #CRUD - CREATE(append/insert) READ(view)
#UPDATE(assigned) and DELETE(remove/clear)


chocolatesA = {"Twix", "Toblerone", "Kitkat", "Bounty", "Dairy Milk"}
chocolatesB = {"Snickers", "Bueno", "Mars", "Ferrero", "Kisses"}
print(chocolatesA)
chocolatesA.add("Meiji")
print(chocolatesA)


ChocolatesUnion = chocolatesA.union(chocolatesB)
print(ChocolatesUnion)
ChocolatesIntersection = chocolatesA.intersection(chocolatesB)
print(ChocolatesIntersection)
ChocolatesDifference = chocolatesA.difference(chocolatesB)
print(ChocolatesDifference)
ChocolatesDifference = chocolatesB.difference(chocolatesA)
print(ChocolatesDifference)


chocolatesA = {"Twix", "Toblerone", "Kitkat", "Bounty", "Dairy Milk"}
chocolatesB = {"Snickers", "Bueno", "Mars", "Ferrero", "Kisses"}
ChocolatesOfSet = [chocolatesA, chocolatesB]
print(ChocolatesOfSet)


#TUPLE #IMMUTABLE
chocolatesA = ("Twix", "Toblerone", "Kitkat", "Bounty", "Dairy Milk")
print(chocolatesA)
print(chocolatesA.index("Kitkat"))
print(chocolatesA.count("Toblerone"))
print(chocolatesA[2])
chocolatesB = ("Snickers", "Bueno", "Mars", "Ferrero")
CHOCOLATES = (chocolatesA, chocolatesB)
print(CHOCOLATES)
mytuple = (
   (1, 2, 3 , "A"),
   (4, 5, 6 , "B"),
   (7, 8, 9 , "C"),
   (0, "*", "#" , "D"),
)
print(mytuple[3][2])


#KEY  : VALUE
myInfo = {
 "Name": "Keira Dimaculangan",
 "Age": 18,
 "Citizenship": "Filipino",
 "Address": "Las Pinas"
}
print(myInfo)
print(myInfo["Name"])
print(myInfo["Address"])
print(myInfo["Age"])
print(myInfo.get("Name"))
myInfo["Name"] = "Keira"
print(myInfo)
print(myInfo["Name"])
myInfo.update({"Section" : 4})
print(myInfo)


#nested dictionary
#{"Name" : { "FirstName" : "Keira", "Mae" : "Dimaculangan" }, "Age" : 18, "Hobbies" : ["Anime", "Singing", "Mobile Legends", "Make up", "Reading"] }
myInfo = {
 "Name": {
   "FirstName": "Keira Mae",
   "LastName": "Dimaculangan"
 },
 "Age": 18,
 "Hobbies": [
   "Anime",
   "Singing",
   "Mobile Legends"
   "Make up",
   "Reading"]}
print(myInfo)
print(myInfo["Name"]["LastName"])
print(myInfo["Name"])
print(myInfo["Name"]["FirstName"] + " " +  myInfo["Name"]["LastName"])
print(myInfo["Hobbies"][1])


simpleATMMachineDatabase = [{ "Name": {
           "FirstName": "Keira Mae",
           "LastName": "Mae"},
           "AccountNumber":98483 ,
           "PIN" : "Kei103",
           "ControlNumber": 1435,
           "Balance": 774.77 }, {
"Name": {"FirstName": "Keisha Mae",
       "LastName": "Dimaculangan"},
       "AccountNumber": 837483,
       "PIN": "Giyu676",
       "ControlNumber": 78,
       "Balance": 27827461824.99
   },
   {
       "Name": {
       "FirstName": "Alyana",
           "LastName": "Dimaculangan"
       },
       "AccountNumber": 87493,
       "PIN": "Yana9798",
       "ControlNumber": 29,
       "Balance": 824878
   }
]


myName = input("Please Enter your Name")
myAccountNumer = input("Please Enter your Account Number")
PIN = input("Please Enter your PIN Number")
#code to get specific record (next meeting)
print(f'This is your Balance : {simpleATMMachineDatabase[1]["Balance"]}')


CHOCOLATESa = ["Twix", "Twix", "Kitkat", "Toblerone", "Hersheys"]
CHOCOLATESa.append("Bueno")
print(CHOCOLATESa)
CHOCOLATESa.insert(2, "Meiji")
print(CHOCOLATESa)
print(CHOCOLATESa.index("Hersheys"))
CHOCOLATESa[4] = "Toblerone"
print(CHOCOLATESa)
print(len(CHOCOLATESa))
print(CHOCOLATESa.count("Twix"))


CHOCOLATESa.remove("Twix")
print(CHOCOLATESa)


print(CHOCOLATESa[4])


CHOCOLATESa.clear()
print(CHOCOLATESa)




CHOCOLATESA = ["Twix", "Kitkat", "Toblerone", "Hersheys", "Meiji"]
CHOCOLATESB = ["Kisses", "Dairy Milk", "Mars", "Auro", "Choco Choco"]
CHOCOLATESC = ["Snickers", "Supersticks", "Choco Mucho", "Cloud 9", "Hello"]
CHOCOLATESABC = [CHOCOLATESA, CHOCOLATESB, CHOCOLATESC] #list of list
print(CHOCOLATESABC)
print(CHOCOLATESABC[2][3])


CHOCOLATESABCAdd = CHOCOLATESA + CHOCOLATESB +  CHOCOLATESC #single list
print(CHOCOLATESABCAdd)
CHOCOLATESA.extend(CHOCOLATESB)
CHOCOLATESA.extend(CHOCOLATESC)
print(CHOCOLATESA)


#LIST OF A different data types and list
myInfoList = ["Keira Mae", 18, True, ["Anime", "Singing", "Reading"]]
print(myInfoList[0])
print(myInfoList[1])
print(myInfoList[2])
print(myInfoList[3])
print(myInfoList[3][1])


#TUPLE ( ) parenthesis
CHOCOLATES_A = ("Twix", "Kitkat", "Toblerone", "Hersheys", "Meiji")
print(CHOCOLATES_A[3])
print(CHOCOLATES_A.count("Hersheys"))
CHOCOLATES_B = ("Kisses", "Dairy Milk", "Mars", "Auro", "Choco Choco")
CHOCOLATESC = ("Snickers", "Supersticks", "Choco Mucho", "Cloud 9", "Hello")
CHOCOLATESABC = (CHOCOLATES_A, CHOCOLATES_B, CHOCOLATESC)
print(CHOCOLATESABC[2][4])


#SET { } CURLY BRACE
ChocolatessA = {"Twix", "Kitkat", "Toblerone", "Hersheys", "Meiji"}
ChocolatessB = {"Kisses", "Dairy Milk", "Mars", "Auro", "Choco Choco"}
print(ChocolatessA)
ChocolatessUnion = ChocolatessA.union(ChocolatessB)
print(ChocolatesUnion)
ChocolatessUnionB = ChocolatessA | ChocolatessB
print(ChocolatessUnionB)


CHOCOLATESSIntersection = ChocolatessA.intersection(ChocolatessB)
print(CHOCOLATESSIntersection)
CHOCOLATESSIntersectionB = ChocolatessA & ChocolatessB
print(CHOCOLATESSIntersectionB)


CHOCOLATESSDifference = ChocolatessA.difference(ChocolatessB)
print(CHOCOLATESSDifference)
CHOCOLATESSDifferenceB = ChocolatessA - ChocolatessB
print(CHOCOLATESSDifferenceB)


ChocolatessA = {"Twix", "Kitkat", "Toblerone", "Hersheys", "Meiji"}
ChocolatessB = {"Twix", "Dairy Milk", "Mars", "Auro", "Choco Choco"}
CHOCOLATESSABlistOfSet = [ChocolatessA, ChocolatessB]
print(CHOCOLATESSABlistOfSet)


#TUPLE #IMMUTABLE
CHOCOLATESA = ("Twix", "Twix", "Kitkat", "Toblerone", "Hersheys")
print(CHOCOLATESA)
print(CHOCOLATESA.index("Toblerone"))
print(CHOCOLATESA.count("Twix"))
print(CHOCOLATESA[4])
CHOCOLATESB = ("Netero", "Kite", "Biscuit", "Hisoka")
CHOCOLATES = (CHOCOLATESA, CHOCOLATESB)
print(CHOCOLATES)


mytuple = (
   (0, 1, 2 , "A"),
   (3, 4, 5 , "B"),
   (6, 7, 8 , "C"),
   (9, "*", "#" , "D"),
)
print(mytuple[2][3])


#KEY  : VALUE
myInfo = {
 "Name": "Keira Dimaculangan",
 "Age": 18,
 "Citizenship": "Filipino",
 "Address": "Las Pinas"
}
print(myInfo)
print(myInfo["Name"])
print(myInfo["Address"])
print(myInfo["Age"])
print(myInfo.get("Name"))
myInfo["Name"] = ""
print(myInfo)
print(myInfo["Name"])
myInfo.update({"Section" : 4})
print(myInfo)


#nested dictionary
#{"Name" : { "FirstName" : "Keira", "Dimaculangan" : "Zarsuelo" }, "Age" : 18, "Hobbies" : ["Anime", "Make up", "Singing", "Mobile Legends", "Cooking"] }
myInfo = {
 "Name": {
   "FirstName": "Keira",
   "LastName": "Dimaculangan"
 },
 "Age": 18,
 "Hobbies": [
   "Anime",
   "Make up",
   "Singing",
   "Mobile Legends",
   "Cooking"
 ]
}


print(myInfo)
print(myInfo["Name"]["LastName"])
print(myInfo["Name"])
print(myInfo["Name"]["FirstName"] + " " +  myInfo["Name"]["LastName"])
print(myInfo["Hobbies"][1])


simpleATMMachineDatabase = [
   {
       "Name": {
           "FirstName": "Kate",
           "LastName": "Gadiano"
       },
       "AccountNumber": 95667,
       "PIN" : 837835,
       "ControlNumber": 98,
       "Balance": 245456
   },
   {
       "Name": {
           "FirstName": "Sophia",
           "LastName": "Armillo"
       },
       "AccountNumber": 21645139,
       "PIN": 545545,
       "ControlNumber": 28,
       "Balance": 1548515484.2154
   },
   {
       "Name": {
           "FirstName": "Asherra",
           "LastName": "Calong"
       },
       "AccountNumber": 1545454,
       "PIN": 444745,
       "ControlNumber": 26,
       "Balance": 554555


   }
]
myName = input("Please Enter your Name")
myAccountNumer = input("Please Enter your Account Number")
PIN = input("Please Enter your PIN Number")
#code to get specific record (next meeting)
print(f'This is your Balance : {simpleATMMachineDatabase[1]["Balance"]}')


ChocolatessA.append("Ash")
print(ChocolatessA)
ChocolatessA.insert(2, "Sophia")
print(ChocolatessA)
print(ChocolatessA.index("Ash"))
ChocolatessA[1] = "Sophia"
print(ChocolatessA)
print(len(ChocolatessA))
print(ChocolatessA.count("Ash"))
ChocolatessA.remove("Sophia")
print(ChocolatessA)
print(ChocolatessA[0])
ChocolatessA.clear()
print(ChocolatessA)


#LIST [ ] solid bracket or square bracket
#CRUD - CREATE(append,insert)  READ(view)  UPDATE(assign value by index)  DELETE(pop, remove, clear)
ChocolatesA = ["Toblerone", "Toblerone", "Dairy Milk", "Kisses", "Hershey"]
ChocolatesB = ["Kisses", "Kitkat", "Take It", "Dairy Milk", "Kitkat"]
ChocolatesC = ["Kitkat", "Hershey", "Toblerone", "Kitkat", "Take It"]
ChocolateABC = [ChocolatesA, ChocolatesB, ChocolatesC] #list of list
print(ChocolateABC)
print(ChocolateABC[2][3])
ChocolateABCAdd = ChocolatesA + ChocolatesB + ChocolatesC #single list
print(ChocolateABCAdd)
ChocolatesA.extend(ChocolatesB)
ChocolatesA.extend(ChocolatesC)
print(ChocolatesA)  #single list


#LIST OF A different data types and list
myInfoList = ["Keira", 18, True, ["Anime", "Cooking", "Mobile Legends"]]
print(myInfoList[0])
print(myInfoList[1])
print(myInfoList[2])
print(myInfoList[3])
print(myInfoList[3][1])


#TUPLE ( ) parenthesis
subjectsA = ("math", "math", "science", "filipino", "mapeh")
print(subjectsA[3])


print(subjectsA.count("math"))
subjectsB = ("filipino", "esp", "mtb", "science", "english")
subjectsC = ("english", "mapeh", "math", "english", "mtb")
SUBJECTSABC = (subjectsA, subjectsB, subjectsC)
print(SUBJECTSABC[2][4])


#SET { } CURLY BRACE
subjectsa = {"math", "science", "filipino", "mapeh"}
subjectsb = {"mapeh", "math", "mtb", "english"}


SUBJECTSUnion = subjectsa.union(subjectsb)
print(SUBJECTSUnion)
SUBJECTSUnionB=subjectsa | subjectsb
print(SUBJECTSUnionB)


SUBJECTSIntersection = subjectsa.intersection(subjectsb)
print(SUBJECTSIntersection)
SUBJECTSIntersectionB = subjectsa & subjectsa
print(SUBJECTSIntersectionB)


SUBJECTSDifference = subjectsa.difference(subjectsb)
print(SUBJECTSDifference)
SUBJECTSDifferenceB = subjectsa - subjectsb
print(SUBJECTSDifferenceB)


#SUBSET
SubjectsA = {"math", "science", "filipino", "mapeh"}
SubjectsB = {"mapeh", "math", "english", "esp"}
SubjectsC = {"science", "mtb"}
ColorsD = {"science", "white"}
print(SubjectsC.issubset(SubjectsA))
print(ColorsD.issubset(SubjectsA))


#DICTIONARY - dict - CURLY BRACES, KEY-VALUE PAIR
#myInfo = {"Name" : "Keira Dimaculangan", "Age" : 18, "Citizenship": "Filipino"}
myInfo = {
 "Name": "Keira Dimaculangan",
 "Age": 18,
 "Citizenship": "Filipino"
}
print(myInfo)
print(myInfo["Name"])
print(myInfo.get("Name"))
print(myInfo["Age"])
print(myInfo.get("Age"))
print(myInfo["Citizenship"])
print(myInfo.get("Citizenship"))


myInfo.update({"Address": "Laguna"})
print(myInfo)
myInfo.update({"Age": 18}) #update
print(myInfo)
myInfo["Age"] = 18 #assigned value
print(myInfo)


print(myInfo.values())
print(myInfo.keys())


for i in myInfo.keys():
   print(myInfo[i])


#myInfo = {"Name" : "Keira Dimaculangan", "Age" : 25, "Citizenship": "Filipino"}
myInfo = {
 "Name": {
     "FirstName" : "Keira",
     "LastName" : "Dimaculangan"
 },
 "Age": 18,
 "Citizenship": "Filipino",
 "Hobbies" : [
     "Mobile Legends", "Watching Anime", "Cooking"
 ]
}
print(myInfo)
print(myInfo["Name"]["FirstName"])
print(myInfo["Name"]["LastName"])


shoesA = ["Adidas", "Puma", "Nike", "Converse", "Vans"]
print(shoesA)
print(shoesA[2])
print(shoesA.index("Gon"))
isThere = "Gon" in shoesA
print(isThere)
shoesA.append("New Balance")
print(shoesA)
shoesA.insert(3, "Chrolo")
print(shoesA)
print(len(shoesA))
print(shoesA.count("Nike"))
shoesA.remove("Converse")
print(shoesA)
print(shoesA.index("Kurapika"))
shoesA[1] = "Hisoka"
print(shoesA)


#LIST #MUTABLE #CRUD - CREATE(append/insert) READ(view)
#UPDATE(assigned) and DELETE(remove/clear)
chocolatesA = ["Twix", "Toblerone", "Kitkat", "Bounty", "Dairy Milk"]
chocolatesB = ["Snickers", "Bueno", "Mars", "Ferrero", "Kisses"]
chocolatesC = ["Meiji", "Salcov", "Auro", "Choco Choco", "Super sticks"]


Chocolates_list = [chocolatesA, chocolatesB, chocolatesC]
print(Chocolates_list) #list of a list
print(Chocolates_list[2])
print(Chocolates_list[2][1])


Chocolates_Plus = chocolatesA + chocolatesB + chocolatesC
print(Chocolates_Plus)


chocolatesA.extend(chocolatesB)
chocolatesA.extend(chocolatesC)
print(chocolatesA)


#SET #MUTABLE #CRUD - CREATE(append/insert) READ(view)
#UPDATE(assigned) and DELETE(remove/clear)


chocolatesA = {"Twix", "Toblerone", "Kitkat", "Bounty", "Dairy Milk"}
chocolatesB = {"Snickers", "Bueno", "Mars", "Ferrero", "Kisses"}
print(chocolatesA)
chocolatesA.add("Meiji")
print(chocolatesA)


ChocolatesUnion = chocolatesA.union(chocolatesB)
print(ChocolatesUnion)
ChocolatesIntersection = chocolatesA.intersection(chocolatesB)
print(ChocolatesIntersection)
ChocolatesDifference = chocolatesA.difference(chocolatesB)
print(ChocolatesDifference)
ChocolatesDifference = chocolatesB.difference(chocolatesA)
print(ChocolatesDifference)


chocolatesA = {"Twix", "Toblerone", "Kitkat", "Bounty", "Dairy Milk"}
chocolatesB = {"Snickers", "Bueno", "Mars", "Ferrero", "Kisses"}
ChocolatesOfSet = [chocolatesA, chocolatesB]
print(ChocolatesOfSet)


#TUPLE #IMMUTABLE
chocolatesA = ("Twix", "Toblerone", "Kitkat", "Bounty", "Dairy Milk")
print(chocolatesA)
print(chocolatesA.index("Kitkat"))
print(chocolatesA.count("Toblerone"))
print(chocolatesA[2])
chocolatesB = ("Snickers", "Bueno", "Mars", "Ferrero")
CHOCOLATES = (chocolatesA, chocolatesB)
print(CHOCOLATES)
mytuple = (
   (1, 2, 3 , "A"),
   (4, 5, 6 , "B"),
   (7, 8, 9 , "C"),
   (0, "*", "#" , "D"),
)
print(mytuple[3][2])


#KEY  : VALUE
myInfo = {
 "Name": "Keira Dimaculangan",
 "Age": 18,
 "Citizenship": "Filipino",
 "Address": "Las Pinas"
}
print(myInfo)
print(myInfo["Name"])
print(myInfo["Address"])
print(myInfo["Age"])
print(myInfo.get("Name"))
myInfo["Name"] = "Keira"
print(myInfo)
print(myInfo["Name"])
myInfo.update({"Section" : 4})
print(myInfo)


#nested dictionary
#{"Name" : { "FirstName" : "Keira", "Mae" : "Dimaculangan" }, "Age" : 18, "Hobbies" : ["Anime", "Singing", "Mobile Legends", "Make up", "Reading"] }
myInfo = {
 "Name": {
   "FirstName": "Keira Mae",
   "LastName": "Dimaculangan"
 },
 "Age": 18,
 "Hobbies": [
   "Anime",
   "Singing",
   "Mobile Legends"
   "Make up",
   "Reading"]}
print(myInfo)
print(myInfo["Name"]["LastName"])
print(myInfo["Name"])
print(myInfo["Name"]["FirstName"] + " " +  myInfo["Name"]["LastName"])
print(myInfo["Hobbies"][1])


simpleATMMachineDatabase = [{ "Name": {
           "FirstName": "Keira Mae",
           "LastName": "Mae"},
           "AccountNumber":98483 ,
           "PIN" : "Kei103",
           "ControlNumber": 1435,
           "Balance": 774.77 }, {
"Name": {"FirstName": "Keisha Mae",
       "LastName": "Dimaculangan"},
       "AccountNumber": 837483,
       "PIN": "Giyu676",
       "ControlNumber": 78,
       "Balance": 27827461824.99
   },
   {
       "Name": {
       "FirstName": "Alyana",
           "LastName": "Dimaculangan"
       },
       "AccountNumber": 87493,
       "PIN": "Yana9798",
       "ControlNumber": 29,
       "Balance": 824878
   }
]


myName = input("Please Enter your Name")
myAccountNumer = input("Please Enter your Account Number")
PIN = input("Please Enter your PIN Number")
#code to get specific record (next meeting)
print(f'This is your Balance : {simpleATMMachineDatabase[1]["Balance"]}')


CHOCOLATESa = ["Twix", "Twix", "Kitkat", "Toblerone", "Hersheys"]
CHOCOLATESa.append("Bueno")
print(CHOCOLATESa)
CHOCOLATESa.insert(2, "Meiji")
print(CHOCOLATESa)
print(CHOCOLATESa.index("Hersheys"))
CHOCOLATESa[4] = "Toblerone"
print(CHOCOLATESa)
print(len(CHOCOLATESa))
print(CHOCOLATESa.count("Twix"))


CHOCOLATESa.remove("Twix")
print(CHOCOLATESa)


print(CHOCOLATESa[4])


CHOCOLATESa.clear()
print(CHOCOLATESa)




CHOCOLATESA = ["Twix", "Kitkat", "Toblerone", "Hersheys", "Meiji"]
CHOCOLATESB = ["Kisses", "Dairy Milk", "Mars", "Auro", "Choco Choco"]
CHOCOLATESC = ["Snickers", "Supersticks", "Choco Mucho", "Cloud 9", "Hello"]
CHOCOLATESABC = [CHOCOLATESA, CHOCOLATESB, CHOCOLATESC] #list of list
print(CHOCOLATESABC)
print(CHOCOLATESABC[2][3])


CHOCOLATESABCAdd = CHOCOLATESA + CHOCOLATESB +  CHOCOLATESC #single list
print(CHOCOLATESABCAdd)
CHOCOLATESA.extend(CHOCOLATESB)
CHOCOLATESA.extend(CHOCOLATESC)
print(CHOCOLATESA)


#LIST OF A different data types and list
myInfoList = ["Keira Mae", 18, True, ["Anime", "Singing", "Reading"]]
print(myInfoList[0])
print(myInfoList[1])
print(myInfoList[2])
print(myInfoList[3])
print(myInfoList[3][1])


#TUPLE ( ) parenthesis
CHOCOLATES_A = ("Twix", "Kitkat", "Toblerone", "Hersheys", "Meiji")
print(CHOCOLATES_A[3])
print(CHOCOLATES_A.count("Hersheys"))
CHOCOLATES_B = ("Kisses", "Dairy Milk", "Mars", "Auro", "Choco Choco")
CHOCOLATESC = ("Snickers", "Supersticks", "Choco Mucho", "Cloud 9", "Hello")
CHOCOLATESABC = (CHOCOLATES_A, CHOCOLATES_B, CHOCOLATESC)
print(CHOCOLATESABC[2][4])


#SET { } CURLY BRACE
ChocolatessA = {"Twix", "Kitkat", "Toblerone", "Hersheys", "Meiji"}
ChocolatessB = {"Kisses", "Dairy Milk", "Mars", "Auro", "Choco Choco"}
print(ChocolatessA)
ChocolatessUnion = ChocolatessA.union(ChocolatessB)
print(ChocolatesUnion)
ChocolatessUnionB = ChocolatessA | ChocolatessB
print(ChocolatessUnionB)


CHOCOLATESSIntersection = ChocolatessA.intersection(ChocolatessB)
print(CHOCOLATESSIntersection)
CHOCOLATESSIntersectionB = ChocolatessA & ChocolatessB
print(CHOCOLATESSIntersectionB)


CHOCOLATESSDifference = ChocolatessA.difference(ChocolatessB)
print(CHOCOLATESSDifference)
CHOCOLATESSDifferenceB = ChocolatessA - ChocolatessB
print(CHOCOLATESSDifferenceB)


ChocolatessA = {"Twix", "Kitkat", "Toblerone", "Hersheys", "Meiji"}
ChocolatessB = {"Twix", "Dairy Milk", "Mars", "Auro", "Choco Choco"}
CHOCOLATESSABlistOfSet = [ChocolatessA, ChocolatessB]
print(CHOCOLATESSABlistOfSet)


#TUPLE #IMMUTABLE
CHOCOLATESA = ("Twix", "Twix", "Kitkat", "Toblerone", "Hersheys")
print(CHOCOLATESA)
print(CHOCOLATESA.index("Toblerone"))
print(CHOCOLATESA.count("Twix"))
print(CHOCOLATESA[4])
CHOCOLATESB = ("Netero", "Kite", "Biscuit", "Hisoka")
CHOCOLATES = (CHOCOLATESA, CHOCOLATESB)
print(CHOCOLATES)


mytuple = (
   (0, 1, 2 , "A"),
   (3, 4, 5 , "B"),
   (6, 7, 8 , "C"),
   (9, "*", "#" , "D"),
)
print(mytuple[2][3])


#KEY  : VALUE
myInfo = {
 "Name": "Keira Dimaculangan",
 "Age": 18,
 "Citizenship": "Filipino",
 "Address": "Las Pinas"
}
print(myInfo)
print(myInfo["Name"])
print(myInfo["Address"])
print(myInfo["Age"])
print(myInfo.get("Name"))
myInfo["Name"] = ""
print(myInfo)
print(myInfo["Name"])
myInfo.update({"Section" : 4})
print(myInfo)


#nested dictionary
#{"Name" : { "FirstName" : "Keira", "Dimaculangan" : "Zarsuelo" }, "Age" : 18, "Hobbies" : ["Anime", "Make up", "Singing", "Mobile Legends", "Cooking"] }
myInfo = {
 "Name": {
   "FirstName": "Keira",
   "LastName": "Dimaculangan"
 },
 "Age": 18,
 "Hobbies": [
   "Anime",
   "Make up",
   "Singing",
   "Mobile Legends",
   "Cooking"
 ]
}


print(myInfo)
print(myInfo["Name"]["LastName"])
print(myInfo["Name"])
print(myInfo["Name"]["FirstName"] + " " +  myInfo["Name"]["LastName"])
print(myInfo["Hobbies"][1])


simpleATMMachineDatabase = [
   {
       "Name": {
           "FirstName": "Kate",
           "LastName": "Gadiano"
       },
       "AccountNumber": 95667,
       "PIN" : 837835,
       "ControlNumber": 98,
       "Balance": 245456
   },
   {
       "Name": {
           "FirstName": "Sophia",
           "LastName": "Armillo"
       },
       "AccountNumber": 21645139,
       "PIN": 545545,
       "ControlNumber": 28,
       "Balance": 1548515484.2154
   },
   {
       "Name": {
           "FirstName": "Asherra",
           "LastName": "Calong"
       },
       "AccountNumber": 1545454,
       "PIN": 444745,
       "ControlNumber": 26,
       "Balance": 554555


   }
]
myName = input("Please Enter your Name")
myAccountNumer = input("Please Enter your Account Number")
PIN = input("Please Enter your PIN Number")
#code to get specific record (next meeting)
print(f'This is your Balance : {simpleATMMachineDatabase[1]["Balance"]}')


ChocolatessA.append("Ash")
print(ChocolatessA)
ChocolatessA.insert(2, "Sophia")
print(ChocolatessA)
print(ChocolatessA.index("Ash"))
ChocolatessA[1] = "Sophia"
print(ChocolatessA)
print(len(ChocolatessA))
print(ChocolatessA.count("Ash"))
ChocolatessA.remove("Sophia")
print(ChocolatessA)
print(ChocolatessA[0])
ChocolatessA.clear()
print(ChocolatessA)


#LIST [ ] solid bracket or square bracket
#CRUD - CREATE(append,insert)  READ(view)  UPDATE(assign value by index)  DELETE(pop, remove, clear)
ChocolatesA = ["Toblerone", "Toblerone", "Dairy Milk", "Kisses", "Hershey"]
ChocolatesB = ["Kisses", "Kitkat", "Take It", "Dairy Milk", "Kitkat"]
ChocolatesC = ["Kitkat", "Hershey", "Toblerone", "Kitkat", "Take It"]
ChocolateABC = [ChocolatesA, ChocolatesB, ChocolatesC] #list of list
print(ChocolateABC)
print(ChocolateABC[2][3])
ChocolateABCAdd = ChocolatesA + ChocolatesB + ChocolatesC #single list
print(ChocolateABCAdd)
ChocolatesA.extend(ChocolatesB)
ChocolatesA.extend(ChocolatesC)
print(ChocolatesA)  #single list


#LIST OF A different data types and list
myInfoList = ["Keira", 18, True, ["Anime", "Cooking", "Mobile Legends"]]
print(myInfoList[0])
print(myInfoList[1])
print(myInfoList[2])
print(myInfoList[3])
print(myInfoList[3][1])


#TUPLE ( ) parenthesis
subjectsA = ("math", "math", "science", "filipino", "mapeh")
print(subjectsA[3])


print(subjectsA.count("math"))
subjectsB = ("filipino", "esp", "mtb", "science", "english")
subjectsC = ("english", "mapeh", "math", "english", "mtb")
SUBJECTSABC = (subjectsA, subjectsB, subjectsC)
print(SUBJECTSABC[2][4])


#SET { } CURLY BRACE
subjectsa = {"math", "science", "filipino", "mapeh"}
subjectsb = {"mapeh", "math", "mtb", "english"}


SUBJECTSUnion = subjectsa.union(subjectsb)
print(SUBJECTSUnion)
SUBJECTSUnionB=subjectsa | subjectsb
print(SUBJECTSUnionB)


SUBJECTSIntersection = subjectsa.intersection(subjectsb)
print(SUBJECTSIntersection)
SUBJECTSIntersectionB = subjectsa & subjectsa
print(SUBJECTSIntersectionB)


SUBJECTSDifference = subjectsa.difference(subjectsb)
print(SUBJECTSDifference)
SUBJECTSDifferenceB = subjectsa - subjectsb
print(SUBJECTSDifferenceB)


#SUBSET
SubjectsA = {"math", "science", "filipino", "mapeh"}
SubjectsB = {"mapeh", "math", "english", "esp"}
SubjectsC = {"science", "mtb"}
ColorsD = {"science", "white"}
print(SubjectsC.issubset(SubjectsA))
print(ColorsD.issubset(SubjectsA))


#DICTIONARY - dict - CURLY BRACES, KEY-VALUE PAIR
#myInfo = {"Name" : "Keira Dimaculangan", "Age" : 18, "Citizenship": "Filipino"}
myInfo = {
 "Name": "Keira Dimaculangan",
 "Age": 18,
 "Citizenship": "Filipino"
}
print(myInfo)
print(myInfo["Name"])
print(myInfo.get("Name"))
print(myInfo["Age"])
print(myInfo.get("Age"))
print(myInfo["Citizenship"])
print(myInfo.get("Citizenship"))


myInfo.update({"Address": "Laguna"})
print(myInfo)
myInfo.update({"Age": 18}) #update
print(myInfo)
myInfo["Age"] = 18 #assigned value
print(myInfo)


print(myInfo.values())
print(myInfo.keys())


for i in myInfo.keys():
   print(myInfo[i])


#myInfo = {"Name" : "Keira Dimaculangan", "Age" : 25, "Citizenship": "Filipino"}
myInfo = {
 "Name": {
     "FirstName" : "Keira",
     "LastName" : "Dimaculangan"
 },
 "Age": 18,
 "Citizenship": "Filipino",
 "Hobbies" : [
     "Mobile Legends", "Watching Anime", "Cooking"
 ]
}
print(myInfo)
print(myInfo["Name"]["FirstName"])
print(myInfo["Name"]["LastName"])
print(myInfo["Name"]["FirstName"] + " " + myInfo["Name"]["LastName"])
print(myInfo["Age"])
print(myInfo["Hobbies"][2])


myInfo["Name"]["FirstName"] = "Denise"
print(myInfo["Name"]["FirstName"])


simpleATMMachineDatabase = [
   {
       "Name": {
           "FirstName": "Sophia",
           "LastName": "Armillo"
       },
       "AccountNumber": 467637,
       "PIN" : 7483,
       "ControlNumber": 21,
       "Balance": 87438
   },
   {
       "Name": {
           "FirstName": "Keira",
           "LastName": "Dimaculangan"
       },
       "AccountNumber": 4723,
       "PIN": 47823,
       "ControlNumber": 24,
       "Balance": 9999999999999999999999.99
   },
   {
       "Name": {
           "FirstName": "Samme",
           "LastName": "Roselle"
       },
       "AccountNumber": 8473,
       "PIN": 837582,
       "ControlNumber": 54,
       "Balance": 55451
   }
]


myName = input("Please enter your name")
print(myName)
myAccountNumber = input("Please enter your Account number")
print(myAccountNumber)
myPinNumber = input("Please enter your PIN number")
print(myPinNumber)


print(f'Your remaining balance is {simpleATMMachineDatabase[2]["Balance"]}')






myListOfDictionary = [
   {"subject" : "math"},
   {"subject" : "mapeh"},
   {"subject" : "english"}
]
print(myListOfDictionary[2])
print(myListOfDictionary[2]["subject"])
