"""
print("Hello World") #f5
név = "Ádám" #string
print ("Hello " + név  + "!")

myName = input("Add meg a neved: ")
print("Hello " + myName + " !")
print(id(myName))
print(id(név))
"""

name = "Logirobi"
age = 17
weight = 67.1
smart = True
iq = 119

print(type(name))
print(type(age))
print(type(weight))
print(type(smart))

print ("Szia! " + name + "vagyok")
print("Idén vagyok" + str(age) + "éves")
print(str(weight) + "kg a súlyom")
if smart:
    print("okos vagyok")
else : 
    print("bUtA VoK...")