"""
i = 1
while i <= 10:
    print(i, end = " ")
    i += 1
print ("ciklus után")

list = []
bemenet = "deafult"
while bemenet != "":
    bemenet = input("add meg a lista következő elemét")
    if bemenet != "":
        list.append(bemenet)
print (list)

for i in range(10):
    print (i, end = "")
print()

list = ["Anna", "Béáta", "cECIL", "Dénes", "Elemér" , "Ferenc"]
for item in list:
    print (item, end = "")
print()
"""
list = [1,-99,3,6,39,32,54,43,56,99,-11,-12] 

összeg = 0
for item in list:
    összeg += item
print ("a lista elemeinek összege:")


for item in range(10):
    print(item)
összeg = 0
for item in list: 
    if item > 0:
        összeg += item
    