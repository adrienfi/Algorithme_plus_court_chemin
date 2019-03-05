# -*- coding: utf-8 -*-

# ce script est le programme principal pour la partie 1 du projet
# il permet, via la console :
#
# 1) génération et affichage de la grille
# 2) saisie des points de départ et d'arrivée
# 3) calcul d'un chemin minimal (si existant)
# 4) affichage du résultat (pas de chemin ou chemin affiché dans la grille)

from types_projet import *
from fonctions_logique import * 
from fonctions_console import *

def trajet_le_plus_court (liste_info):
	
	matrice_distance=matrice_des_distances(grille,Ncase_libre,Ncase_mur,Ncase_arrivee,liste_info)
	

	trajet=[]
	l_coordonnees=[liste_info[-2]-1,liste_info[-1]-1]
	
	voisinage=voisin(l_coordonnees,liste_info)
	valeur_du_voisinage=[]
	for k in voisinage:
		valeur_du_voisinage.append(matrice_distance[k[1]][k[0]])
	
	distance_actuelle=min(valeur_du_voisinage)
	
		

	print("L'arrivee est à : " + str(distance_actuelle+1) + " déplaccements")
	
	coord=voisinage[valeur_du_voisinage.index(distance_actuelle)]
	trajet.append(coord)
	while distance_actuelle !=1:

		l_coordonnees=[coord[0],coord[1]]
		voisinage=voisin(l_coordonnees,liste_info)
		valeur_du_voisinage=[]
		for k in voisinage:
			valeur_du_voisinage.append(matrice_distance[k[1]][k[0]])
		
		distance_actuelle=min(valeur_du_voisinage)
		coord=voisinage[valeur_du_voisinage.index(min(valeur_du_voisinage))]
		trajet.append(coord)
	for k in trajet:
		grille[k[1]][k[0]]=4
	print(grille)
	for i in trajet:
		i[1]+=1
		i[0]+=1

	print("Les coordonnées differentes cases par lesquelles passer sont : " + str(trajet[::-1]))
	return(trajet)




	
donnees=aquisition_donnees()
grille=generer_grille(donnees[0],donnees[1],donnees[2])


print(grille)	# affiche une grille avec des 1 et des 0
print ("légende : ")
print( "       1= case libre")
print("       0= Murs")


	 
lcoord_points_D_A= aquisition_donnees_position() 

	
while  int(grille[lcoord_points_D_A[1]-1][lcoord_points_D_A[0]-1]) == 0 & int(grille[lcoord_points_D_A[3]-1][lcoord_points_D_A[2]-1]) == 0 :
	
	print (" Ne pas choisir un point sur un mur") 
	lcoord_points_D_A= aquisition_donnees_position()# La grille contient les points de départ et d'arrivé 	
	
for i in range(4):
	donnees.append(lcoord_points_D_A[i])

grille=generer_PD_PA(grille,donnees[3],donnees[4],donnees[-2],donnees[-1])

#Pour generer la matrice des distances, on a besoin de :
Ncase_libre=max(donnees[1],donnees[2])**2+1 # on choisit arbitrairement le numéro "case libre" supérieur au max des distances
Ncase_mur=(Ncase_libre)+1 #de même pour le numero "case mur"
Ncase_arrivee=Ncase_mur+1 #de même pour le numéro "case arrivée"
if test_si_resolvable(grille,donnees,Ncase_mur) == False :
	print("non résolvable sorry bro")
	
else : 
	
	print ("légende : ")
	print ("       2 =Départ")
	print("       3=Arrivée")
	print("       4=Trajet à suivre")
	trajet_le_plus_court(donnees)
	
	
