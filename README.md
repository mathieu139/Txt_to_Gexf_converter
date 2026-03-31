# Convertisseur TXT vers GEXF

Ce projet contient un script Python qui convertit un fichier texte contenant des arêtes de graphe en fichier GEXF, avec le même nom de base.

Exemple :
- entree : `mon_graphe.txt`
- sortie : `mon_graphe.gexf`

Le script principal est : `convert_txt_to_gexf.py`

## Fonctionnement

Le programme fait les actions suivantes :
1. Demande le chemin du fichier `.txt` au lancement.
2. Verifie que le chemin existe, que c'est un fichier et que l'extension est bien `.txt`.
3. Lit le fichier ligne par ligne.
4. Ignore les lignes vides, les commentaires (lignes commencant par `#`) et les lignes invalides.
5. Construit la liste des noeuds et des aretes.
6. Genere un fichier `.gexf` dans le meme dossier, avec le meme nom.

## Format attendu du fichier TXT

Chaque ligne valide doit contenir 2 valeurs separees par des espaces :

```txt
source cible
```

Exemple :

```txt
0 1
1 2
2 3
# commentaire
3 4
```

## Prerequis

- Python 3.10+

## Utilisation

Lancer le script :

```bash
python convert_txt_to_gexf.py
```

Puis saisir le chemin du fichier `.txt` quand il est demande.

Exemple de saisie :

```txt
T:\experience\facebook_combined.txt\facebook_combined.txt
```

Le script affichera ensuite un resume :
- fichier source
- fichier de sortie
- nombre de noeuds
- nombre d'aretes

## Structure du code

- `txt_to_gexf(txt_file, gexf_file)` : conversion du contenu texte vers GEXF
- `ask_txt_path()` : lecture et validation du chemin utilisateur
- `main()` : orchestration du flux complet

