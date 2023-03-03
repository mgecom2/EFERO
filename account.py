 

def demander_nom():
    nom = ""
    while nom == "":
        nom = input("Quelle est votre nom ?")
    return nom
nom = demander_nom()


def demander_age():
    age =""
    while age == "":
        age = input("Quelle est votre age ?")
    return age
age = demander_age()

if int(age) < 18:
    print(nom + " " + "est mineur")
elif 
else:
    print(nom + " " + "est majeur")
