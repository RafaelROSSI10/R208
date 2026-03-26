from obj_couleur import Couleur
from obj_auteur import Auteur


class Livre(Couleur):
    nombre_total_livres = 0

    def __init__(self, titre, auteur, isbn=None, annee_publication=None):
        Livre.nombre_total_livres += 1
        self.id = Livre.nombre_total_livres

        self.titre = titre
        self.auteur = auteur  # L'auteur est une instance de la classe Auteur
        self.isbn = "N/A" if isbn is None else isbn
        self.annee_publication = "Inconnue" if annee_publication is None else annee_publication
        self.disponible = True  # True par défaut

    def __str__(self):
        etat = "Dispo" if self.disponible else "ND"
        return f"'{self.titre}' de {self.auteur.prenom} {self.auteur.nom} (ISBN: {self.isbn}, publié en {self.annee_publication}) - {etat}"


if __name__ == "__main__":
    follett = Auteur("FOLLETT", "Ken", "Pays de Galles", "05/06/1949")
    livre_1 = Livre("Les Piliers de la Terre", follett, "9782130428114", "1989")
    livre_2 = Livre("Une Colonne de Feu", follett, "9782221157695", "2017")
    livre_2.disponible = False  # On le rend indisponible pour tester

    print("Création de 2 instances de Livre et affichage...")
    print(livre_1)
    print(livre_2)