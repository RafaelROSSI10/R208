class Voitures():
    def __init__(self, marque = "ferrari", modele = "sf90", annee = 2010):
        self.marque = marque
        self.annee = annee
        self.modele = modele

    def __str__(self):
        return f"Valeurs des attributs de l'instance : {self.marque} {self.modele} {self.annee}"


car = Voitures("Renault", "Clio", 2018)
caisse = car.modele
print(f"J'ai une {car.marque} {caisse} de {car.annee} !")
car.annee = 2020
print(f"J'ai une {car.marque} {caisse} de {car.annee} !")
print(car)

car2 = Voitures("Peugeot", "208", 2021)
print(car2)

ma_voiture = Voitures("Bugatti", "Veyron")
print(ma_voiture)

voiture4 = Voitures()
print("Voiture 4 :", voiture4)

voiture5 = Voitures(modele="F40", annee= 1990)
print("Voiture 5 :", voiture5)

voiture6 = Voitures(modele="296_GTS", marque="Porsche")
print("Voiture 6 :", voiture6)

print("\n--- Type ---")
print(type(voiture6))


print("\n--- Vars ---")
print(vars(voiture6))

print("\n--- Dir ---")
print(dir(voiture6))





