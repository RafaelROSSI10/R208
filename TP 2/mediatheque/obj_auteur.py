from .obj_couleur import Couleur


class Auteur(Couleur):
    nombre_total_auteurs = 0

    def __init__(self, nom, prenom, pays=None, date_naissance=None):
        Auteur.nombre_total_auteurs += 1
        self.id = Auteur.nombre_total_auteurs

        self.nom = nom.upper()
        self.prenom = prenom.capitalize()
        # Correction issue du QCM
        self.pays = pays if pays else "Inconnu"
        self.date_naissance = date_naissance if date_naissance else "Inconnue"

    def __str__(self):
        return f"{self.id}\t{Auteur.MAGENTA}{self.prenom} {self.nom} (né(e) le {self.date_naissance} en {self.pays}){Auteur.NO_COLOR}"


if __name__ == "__main__":
    print("Création de 3 instances de Auteur et affichage...")
    follett = Auteur("FOLLETT", "Ken", "Pays de Galles", "05/06/1949")
    verne = Auteur("VERNE", "Jules", "France", "08/02/1828")
    bridou = Auteur("BRIDOU", "Justin", None, None)
    print(follett)
    print(verne)
    print(bridou)