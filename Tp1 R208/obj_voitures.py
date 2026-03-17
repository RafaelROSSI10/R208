import base64
import re


class Voitures():


    prix_litre = 1.70

    def __init__(self, marque="Ferrari", modele="SF90_spider", annee=2010, prix=None, couleur="Blanc", conso=6.0):
        # Attributs d'instance publics
        self.marque = marque
        self.annee = annee
        self.modele = modele
        self.prix = prix
        self.couleur = couleur
        self.conso = conso

        self._id_serie = "A123 B456 C789"

        self.__audio_code = base64.b64encode("0000".encode()).decode()

    def __str__(self):
        return f"Voiture : {self.marque} {self.modele} - {self.annee} - {self.couleur} - {self.conso} l/100km - {self.prix} €"

    def calcul_consommation(self, distance):
        return (self.conso * distance) / 100

    def calcul_prix(self, distance):
        litres_necessaires = self.calcul_consommation(distance)
        return litres_necessaires * Voitures.prix_litre

    def modif_prix_litre(self, nouveau_prix):
        Voitures.prix_litre = nouveau_prix

    def calcul_co2(self, distance):
        litres_necessaires = self.calcul_consommation(distance)
        return litres_necessaires * 2.3

    def affiche_prot_priv(self):
        print(f"ID Série (protégé) : {self._id_serie}")
        print(f"Audio Code (pseudo-privé chiffré) : {self.__audio_code}")

    # --- GETTERS ET SETTERS ---

    def get_id_serie(self):

        return self._id_serie

    def set_id_serie(self, num_serie):
        if re.fullmatch(r"[A-Z0-9]{4} [A-Z0-9]{4} [A-Z0-9]{4}", num_serie):
            self._id_serie = num_serie
            return True
        return False

    def get_audio_code(self):
        return base64.b64decode(self.__audio_code).decode()

    def set_audio_code(self, code):
        if re.fullmatch(r"[0-9]{4}", code):
            self.__audio_code = base64.b64encode(code.encode()).decode()
            return True
        return False