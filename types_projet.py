# -*- coding: utf8 -*-

# cette bibliothèque contient les types personnalisés utilisés dans le programme

from collections import namedtuple

# le programme manipule la grille sous la forme d'une liste de listes, de taille [TAILLE][TAILLE], contenant soit des 0 (mur) soit des 1 (vide)
# c'est un type de base, il n'y a donc pas de type particulier défini ici

# le type Position défini ci-dessous est utilisé pour stocker une position dans la grille, donc 2 coordonnées x,y
# on peut créer une position en utilisant c = Position(0,2)
# on peut lire/écrire une coordonnée en utilisant c.x ou c.y
Position = namedtuple("Position",["x","y"])
