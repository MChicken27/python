"""
szöveg = "A fekete cica átsétált az úton"
print(szöveg)
print("A szöveg hossza:", len(szöveg))

szöveg_szavanként = szöveg.split(" ")
print(szöveg_szavanként)
szöveg_azként = szöveg.split("az")

első_az = szöveg.find("az")
print ("Az 'az' karaktersorozat elsőelőfordulási helye:", első_az)

első_n = szöveg.find("n")
print ("Az 'az' karaktersorozat elsőelőfordulási helye:", első_n)

szó = "kutya"
print(szó)
print(szó.capitalize())
print(szó.lower())
print(szó.upper())
"""

thing_1 = input("type an object: \n")
thing_2 =  input("type an other object: \n")
adjective =  input("type an adjective: \n")
song_name =  input("type a song name: \n")
celebrity =  input("type a celebrity: \n")
feeling =  input("type a feeling: \n")
verb =  input("type a verb: \n")
place =  input("type a place: \n")
food =  input("type a food: \n")
person =  input("type a person: \n")

print(f"""i just got back from a pizza party with a {thing_1} can you believe we got to eat a pizza with {thing_2} on it ? It was super {adjective}
The party even had a cool song , named {song_name} made by {celebrity} , it felt so {feeling}. My favirote was when someone said he likes to {verb}, that was really stupid. 
like imagine saying that at {place} while eating {food}. I asked his name , it was {person}.
      """)


