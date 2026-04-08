import pandas as pd

df = pd.read_csv("stock_legumes.csv")

def afficher_stock(df):
    df ["valeur_stock"] = df["quantite"]* df["prix_kilo"]
    print (df)
    total= df["valeur_stock"].sum()
    print(f'Valeur totale du stock: {total}€')
    df_stock_bas= df[df["quantite"]<=85]
    if len(df_stock_bas)>0:
        print ("⚠️ Stock bas, faire réappro !")
        print(df_stock_bas[["produit", "quantite"]])
    else:
        print('Stock suffisant partout ✅')
    return df
def ajouter_produit(df):
    nom = input("Nom du nouveau produit: ")
    qtt = int(input("Quantité: "))
    prixklg = float(input("Prix au kilo: "))
    fournisseur = input("Fournisseur: ")
    nouvelle_ligne = {
        "produit": nom,
        "quantite": qtt,
        "prix_kilo": prixklg,
        "fournisseur": fournisseur
    }
    df = pd.concat([df, pd.DataFrame([nouvelle_ligne])], ignore_index=True)
    print("Produit ajouté !")
    return (df)
def modifier_produit(df):
    nom = input("Quel produit veux tu modifier? ")
    if nom in df["produit"].values:
        qtt = int(input("Quelle est la nouvelle quantite? "))
        df.loc[df["produit"] == nom, "quantite"] = qtt
        print("La modification a été réalisée.")
    else:
        print("Produit introuvable !")
    return (df)
def supprimer_produit(df):
    nom = input("Quel est le produit à supprimer? ")
    if nom in df["produit"].values:
        df = df[df["produit"] != nom]
        print("Le produit a été supprimé.")
    else:
        print("Je ne peux pas supprimer ce qui n'existe pas.")
    return (df)
while True:
    print("=== GESTIONNAIRE DE STOCK ===")
    print("1. Afficher le stock")
    print("2. Ajouter un produit")
    print("3. Modifier une quantité")
    print("4. Supprimer un produit")
    print("5. Générer un rapport")
    print("6. Quitter")

    choix = input("Ton choix : ")
    if choix == "1":
        df = afficher_stock(df)

    elif choix == "2":
        df= ajouter_produit(df)

    elif choix == "3":
        df= modifier_produit(df)

    elif choix == "4":
        df = supprimer_produit(df)

    elif choix == "5":
        df.to_csv("stock_legumes.csv", index=False)
        print("Le stock a bien été sauvegardé !")

    elif choix == "6":
        print("AU REVOIR")
        break

    else:
        print("Choix invalide, tape un nombre entre 1 et 6.")



