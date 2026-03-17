class Voitures():
    def __init__(self, marque="Ferrari", modele="SF90_spider", annee=2010):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    # Étape 3 : Redéfinition de la méthode magique __str__ pour un affichage propre
    def __str__(self):
        return f"Valeurs des attributs de l'instance : {self.marque} {self.modele} {self.annee}"

print("--- Étapes 1 à 4 : Création de base et test de __str__ ---")
car = Voitures("Renault", "Clio", 2018)
caisse = car.modele
print(f"J'ai une {car.marque} {caisse} de {car.annee} !")
car.annee = 2020
print(f"J'ai une {car.marque} {caisse} de {car.annee} !")
print(car)


print("\n--- Étape 5 : 2ème instance ---")
voiture2 = Voitures("Peugeot", "208", 2021)
print(voiture2)


print("\n--- Étape 7 : 3ème instance ---")
ma_voiture = Voitures("Bugatti", "Veyron")
print(ma_voiture)


print("\n--- Étape 9 : 4ème instance ---")
voiture4 = Voitures()
print(voiture4)


print("\n--- Étape 10 : 5ème instance ---")
voiture5 = Voitures("F40")
print(voiture5)


print("\n--- Étape 11 : 6ème instance ---")
voiture6 = Voitures(modele="296_GTS")
print(voiture6)


print("\n--- Étapes 12 à 14 : Introspection ---")
# Étape 12
print("Type (étape 12) :", type(voiture6))
# Étape 13
print("Vars (étape 13) :", vars(voiture6))
# Étape 14
print("Dir  (étape 14) :", dir(voiture6))
zzz