from datetime import datetime

from obj_membre import Membre
def menu_ajouter_membre(self):
    while True:
        nom = input("--> Entrez le nom du membre ? : ").strip()
        if nom != "": break
        print("*** Erreur : Valeur saisie incorrecte...")

    while True:
        prenom = input("--> Son prénom ? : ").strip()
        if prenom != "": break
        print("*** Erreur : Valeur saisie incorrecte...")

    while True:
        date_str = input("--> Et sa date de naissance (JJ/MM/AAAA) ? : ").strip()
        try:
            datetime.datetime.strptime(date_str, "%d/%m/%Y")
            break
        except ValueError:
            print("*** Erreur : Valeur saisie incorrecte...")

    nouveau_membre = Membre(nom, prenom, date_str)
    self.biblio.membres.append(nouveau_membre)
    print(
        f"Le membre '{nouveau_membre.prenom} {nouveau_membre.nom} (né(e) le {nouveau_membre.date_naissance})' a bien été créé(e)...")
    input("\nAppuyer sur Entrée pour continuer...")


def menu_supprimer_membre(self):
    self.biblio.lister_membres()  # Affiche la liste
    try:
        id_choix = int(input("--> Choisissez le ou la membre à radier (numéro) : "))
        membre_trouve = next((m for m in self.biblio.membres if m.id == id_choix), None)

        if membre_trouve:
            if len(membre_trouve.livres_empruntes) > 0:
                print(
                    f"Le membre '{membre_trouve.prenom} {membre_trouve.nom}' ne peut pas être radié car il a des emprunts en cours...")
            else:
                print(
                    f"Le membre '{membre_trouve.prenom} {membre_trouve.nom}' peut être radié des membres de la bibliothèque...")
                confirm = input("Veuillez confirmer sa suppression (OUI) ? : ")
                if confirm == "OUI":
                    self.biblio.membres.remove(membre_trouve)
                    print(f"Le membre '{membre_trouve.prenom} {membre_trouve.nom}' a été radié...")
                else:
                    print("Suppression annulée...")
        else:
            print("Erreur : Membre introuvable.")
    except ValueError:
        print("Erreur de saisie.")
    input("\nAppuyer sur Entrée pour continuer...")


def menu_supprimer_livre(self):
    self.biblio.lister_livres()  # Affiche la liste
    try:
        id_choix = int(input("--> Choisissez le livre à supprimer (numéro) : "))
        livre_trouve = next((l for l in self.biblio.livres if l.id == id_choix), None)

        if livre_trouve:
            if not livre_trouve.disponible:
                print(f"Le livre '{livre_trouve.titre}' ne peut pas être supprimé car il est emprunté...")
            else:
                print(f"Le livre '{livre_trouve.titre}' peut être supprimé de la bibliothèque...")
                confirm = input("Veuillez confirmer sa suppression (OUI) ? : ")
                if confirm == "OUI":
                    self.biblio.livres.remove(livre_trouve)
                    print(f"Le livre '{livre_trouve.titre}' a été supprimé...")
                else:
                    print("Suppression annulée...")
        else:
            print("Erreur : Livre introuvable.")
    except ValueError:
        print("Erreur de saisie.")
    input("\nAppuyer sur Entrée pour continuer...")


class Ihm:
    pass
