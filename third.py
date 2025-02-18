#1
my_name = "Dani"
print ("Az én nevem: " + my_name)
print (f"Az én nevem: {my_name}")
print ("")

#2
my_age = 21
print ("az én életkorom" + str(my_age))
print ("")

#3
pet_name = "Morzsi"
pet_age = 5
pet_species = "kutya"

print (f"Az én háziállatom neve {pet_name}, {pet_age} éves , és egy {pet_species}")

pet_name = "Cirmi"
peg_age = 3
pet_species = "macsek"

print (f"Az én háziállatom neve {pet_name}, {pet_age} éves , és egy {pet_species}")

#name = input("mi a neved?")
#age = input("hány éves vagy")
#print("A te neved : %s" %name)
#print ("A te neved : %s és %d éves vagy" %(name, age))

num = 5
word = "auto"
is_boy= True
is_animal = False

if num : 
    print("Ez egy szám")
if word : 
    print("Ez egy karakter")
if is_boy:
    print("ő egy fiú")
if is_animal:
    print("ő egy állat")
else:
    print("ő nem állat")

num1=12
num2=33
num3 = 68

if num1 > num2:
    print("Az első szám nagyobb mint a második")
if num1 < num2 or num2> num3:
    print("No Kecske ):")
else : 
    print("kecske")

#a1=int(input("Kérem az első számot:"))
#a2=int(input("Kérem a második számot"))

#if a1==a2:
    #print("a két szám egyenlő")
#elif a1>a2:
    #print("az első szám nagyobb mint a második")
#else:
    #print("az első szám kisebb mint a második")

score = int(input("hány pontos lett a dolgozatot ?"))

if score >= 90:
    print("5-ös lett a dolgozatód")
elif score >= 75: 
    print("4-es lett a dolgozatód")
elif score >= 60: 
    print("3-as lett a dolgozatód")
elif score >= 45: 
    print("2-as lett a dolgozatód")
else: 
    print("1-es lett a dolgozatód")