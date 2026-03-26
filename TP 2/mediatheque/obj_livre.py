from .obj_couleur import Couleur
from .obj_auteur import Auteur

class Livre(Couleur):
    nombre_total_livres = 0

    def __init__(self, titre, auteur, isbn=None, annee_publication=None):
        Livre.nombre_total_livres += 1
        self.id = Livre.nombre_total_livres
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn if isbn else "N/A"
        self.annee_publication = annee_publication if annee_publication else "Inconnue"
        self.disponible = True

    def __str__(self):
        return (f"{self.id}{Livre.NO_COLOR}.\t: {Livre.VERT}'{self.titre}' de "
                f"{self.auteur.prenom} {self.auteur.nom} {Livre.NO_COLOR}(ISBN: {self.isbn}, "
                f"publié en {self.annee_publication}){Livre.NO_COLOR} - "
                f"{'Dispo' if self.disponible else 'NON Dispo'}"
                f"{Livre.VERT if self.disponible else Livre.ROUGE}{Livre.NO_COLOR}")

if __name__ == "__main__":
    follett = Auteur("FOLLETT", "Ken", "Pays de Galles", "05/06/1949")
    livre_1 = Livre("Les Piliers de la Terre", follett, "9782130428114", "1989")
    print(livre_1)