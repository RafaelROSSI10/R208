from obj_voitures import Voitures

print("="*50)
print("1. CRÉATION DU GARAGE")
print("="*50)

captur = Voitures(marque="Renault", modele="Captur_TCE_90ch", annee=2021, couleur="Gris foncé", conso=7.2, prix=20000)
clio = Voitures(marque="Renault", modele="Clio_TCE_100ch", annee=2018, couleur="Bleu nuit", conso=5.5, prix=17000)

print(captur)
print(clio)

print("\n" + "="*50)
print("2. TESTS DE VOYAGE : COLMAR - BIARRITZ (1060 km)")
print("="*50)

distance = 1060

print("--- Consommation Carburant ---")
print(f"Captur : {captur.calcul_consommation(distance):.2f} L")
print(f"Clio   : {clio.calcul_consommation(distance):.2f} L")

print("\nBilan Carbone (CO2)")
print(f"Captur : {captur.calcul_co2(distance):.2f} kg de CO2")
print(f"Clio   : {clio.calcul_co2(distance):.2f} kg de CO2")
print("Rappel : Un voyage en TGV génère environ 3.9 kg de CO2 par passager !")

print("\n" + "="*50)
print("3. TESTS DES ATTRIBUTS DE CLASSE (Prix du litre)")
print("="*50)

print(f"Prix initial (Captur) : {captur.prix_litre} €/L")
print(f"Prix initial (Clio)   : {clio.prix_litre} €/L")
print(f"Coût trajet Clio : {clio.calcul_prix(distance):.2f} €")
print(f"Coût trajet Captur : {captur.calcul_prix(distance):.2f} €")

print("\n... L'essence augmente ! Mise à jour via captur.modif_prix_litre(1.95) ...")
captur.modif_prix_litre(1.95)

# La modification impacte TOUTES les instances
print(f"Nouveau prix (Captur) : {captur.prix_litre} €/L")
print(f"Nouveau prix (Clio)   : {clio.prix_litre} €/L")
print(f"Nouveau coût trajet Clio : {clio.calcul_prix(distance):.2f} €")
print(f"Nouveau coût trajet Captur : {captur.calcul_prix(distance):.2f} €")

print("\n" + "="*50)
print("4. TESTS D'ENCAPSULATION (Attributs Protégés et Privés)")
print("="*50)

print("--- Accès aux attributs cachés ---")
print(f"Accès direct _id_serie (déconseillé mais possible) : {captur._id_serie}")

try:
    print(captur.__audio_code)
except AttributeError:
    print("ÉCHEC NORMAL : Impossible d'accéder directement à captur.__audio_code (pseudo-privé) !")

print("\n--- Utilisation des méthodes de la classe ---")
captur.affiche_prot_priv()

print("\n" + "="*50)
print("5. TESTS DES GETTERS ET SETTERS (Contrôle et Chiffrement)")
print("="*50)

# Test de l'ID série avec Regex
print("--- Modification ID Série ---")
print("Tentative avec format invalide ('TEST') :", captur.set_id_serie("TEST"))
print("Tentative avec format valide ('Z999 Y888 X777') :", captur.set_id_serie("Z999 Y888 X777"))
print(f"Nouvel ID lu via le Getter : {captur.get_id_serie()}")

# Test du Code Audio avec Chiffrement Base64
print("\n--- Modification Code Audio ---")
print(f"Code actuel (déchiffré via Getter) : {captur.get_audio_code()}")
print("Tentative avec format invalide ('AZER') :", captur.set_audio_code("AZER"))
print("Tentative avec format valide ('9876') :", captur.set_audio_code("9876"))
print(f"Nouveau code lu (déchiffré via Getter) : {captur.get_audio_code()}")

print("\nVérification en mémoire (Code stocké chiffré) :")
captur.affiche_prot_priv()