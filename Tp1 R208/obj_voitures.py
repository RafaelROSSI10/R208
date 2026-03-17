import base64
import re


class Voitures():
    """
    Classe représentant une voiture avec ses caractéristiques techniques,
    son coût d'utilisation et ses données sécurisées.
    """

    # Attribut de classe : commun et identique pour toutes les instances
    prix_litre = 1.70

    def __init__(self, marque="Ferrari", modele="SF90_spider", annee=2010, prix=None, couleur="Blanc", conso=6.0):
        """Constructeur de la classe Voitures."""
        # Attributs d'instance publics
        self.marque = marque
        self.annee = annee
        self.modele = modele
        self.prix = prix
        self.couleur = couleur
        self.conso = conso

        # Attribut protégé (1 tiret) : Convention pour dire "ne pas toucher de l'extérieur"
        self._id_serie = "A123 B456 C789"

        # Attribut pseudo-privé (2 tirets) : Masqué par Python (Name Mangling)
        # On chiffre la valeur par défaut dès la création
        self.__audio_code = base64.b64encode("0000".encode()).decode()

    def __str__(self):
        """Retourne une chaîne de caractères formatée décrivant la voiture."""
        return f"Voiture : {self.marque} {self.modele} - {self.annee} - {self.couleur} - {self.conso} l/100km - {self.prix} €"

    def calcul_consommation(self, distance):
        """Calcule le volume de carburant consommé pour une distance donnée (en km)."""
        return (self.conso * distance) / 100

    def calcul_prix(self, distance):
        """Calcule le coût en carburant pour une distance donnée (en km)."""
        litres_necessaires = self.calcul_consommation(distance)
        return litres_necessaires * Voitures.prix_litre

    def modif_prix_litre(self, nouveau_prix):
        """Modifie l'attribut de classe définissant le prix du litre de carburant."""
        Voitures.prix_litre = nouveau_prix

    def calcul_co2(self, distance):
        """Calcule la masse de CO2 (en kg) émise pour une distance donnée."""
        litres_necessaires = self.calcul_consommation(distance)
        return litres_necessaires * 2.3

    def affiche_prot_priv(self):
        """Affiche les attributs protégé et pseudo-privé (version chiffrée)."""
        print(f"ID Série (protégé) : {self._id_serie}")
        print(f"Audio Code (pseudo-privé chiffré) : {self.__audio_code}")

    # --- GETTERS ET SETTERS ---

    def get_id_serie(self):
        """Retourne le numéro de série."""
        return self._id_serie

    def set_id_serie(self, num_serie):
        """Met à jour le numéro de série si le format est valide (Ex: A123 B456 C789)."""
        if re.fullmatch(r"[A-Z0-9]{4} [A-Z0-9]{4} [A-Z0-9]{4}", num_serie):
            self._id_serie = num_serie
            return True
        return False

    def get_audio_code(self):
        """Retourne le code audio en le déchiffrant au préalable."""
        return base64.b64decode(self.__audio_code).decode()

    def set_audio_code(self, code):
        """Met à jour le code audio en le chiffrant si le format est valide (4 chiffres)."""
        if re.fullmatch(r"[0-9]{4}", code):
            self.__audio_code = base64.b64encode(code.encode()).decode()
            return True
        return False