# -*- coding: utf8 -*-

# cette bibliothèque contient les fonctions logiques du projet
# elle est utilisée par la partie 1 (console) et la partie 2 (FreeCAD)

from random import randint
import numpy as np
from types_projet import *
from fonctions_console import *


# genere une grille aleatoire
# @param densite de murs en pourcentage (entier entre 0 et 100)
# @return grille : une liste de liste contenant soit des 0 (mur) soit des 1 (vide)

def comptage_1(matrice) : # Fonction permettant de calculer le nombre de 0 présents dans une matrice (utilisée pour la géneration de la grille en fonction d'une densitée)
	j=0
	nb0=0
	while j<=matrice.shape[1]-1:
		
		for i in range (0,matrice.shape[0]-1):
			
			if matrice [i][j]==0:
				nb0=nb0+1
		j=j+1
		
	return nb0
	

def generer_grille(Pdensite,Pdimx,Pdimy): 

	
	nbrecasepleine=int((Pdensite/100)*Pdimx*Pdimy) #nombre de case remplis nécéssaire pour faire les murs
	nbcasespleinesCompte=0
	grille=np.ones((Pdimx,Pdimy)) #Création de notre grille vide aux bonne dimenssions 
	
	
	
	while nbcasespleinesCompte != (nbrecasepleine-1):
			
		nbcasespleinesCompte=comptage_1(grille)
				
		a=randint(0,Pdimx-1)
		b=randint(0,Pdimy-1)
		grille[a][b]=0
	
		
	
			
	return grille
	
	
def generer_PD_PA (matrice, Xdepart,Ydepart,Xstop,Ystop):
		
	matrice[Ydepart-1][Xdepart-1]=2
	matrice[Ystop-1][Xstop-1]=3
	
	
	return matrice 
	
	
def voisin(l,listes): #donne les voisins d'un point
	#Le programme test si les 4 voisins du point sont dans la matrice, et les ajoute à la liste potes_du_point si ils sont dans la matrice
	potes_du_point=[]
	if l[1]-1>=0:
		point=[]
		point.append(l[0])
		point.append(l[1]-1)
		potes_du_point.append(point)
		
	if l[1]+1<=listes[1]-1 :
		point=[]
		point.append(l[0])
		point.append(l[1]+1)
		potes_du_point.append(point)
		
	if l[0]+1<=listes[2]-1:
		point=[]
		point.append(l[0]+1)
		point.append(l[1])
		potes_du_point.append(point)
		
	if l[0]-1>=0 : 
		point=[]
		point.append(l[0]-1)
		point.append(l[1])
		potes_du_point.append(point)
		
	return potes_du_point



def matrice_des_distances(matrice,numero_case_libre,numero_case_mur,numero_case_arrivee,liste):	# fonction qui retourne la matrice des distances $
	
	coord=[]
	coord.append(liste[4]-1)
	coord.append(liste[3]-1)
	l=voisin(coord,liste) #renvoie la liste des voisins du point de départ
	dist=np.full((liste[1],liste[2]),int(numero_case_libre))
	dist[coord[1]][coord[0]]=0 #le point de depart est a la distance 0
	dist[liste[-1]-1][liste[-2]-1]=numero_case_arrivee
	
	for i in range (liste[1]): #la matrice dist prend la valeur numéro des murs si il y a un mur
		for j in range (liste[2]):
			if matrice[i][j]==0:
				dist[i][j]=numero_case_mur
	
	for k in l :

		if dist[k[1]][k[0]]==numero_case_libre:
			dist[k[1]][k[0]]=1 #met a la distance 1 les voisins du point de depart

	while len(l)!=0:
		point_a_traiter=l[0]
		l.remove(point_a_traiter)
		for c in voisin(point_a_traiter,liste):
			if dist[c[1]][c[0]]==numero_case_libre :
				dist[c[1]][c[0]]=(dist[point_a_traiter[1]][point_a_traiter[0]]+1)
				l.append(c)
	
	return(dist)
	
	


def test_si_resolvable(matrice,liste,Ncmur): #cette fonction retourne un niveau logique vrai ou faux en fonction de la resolvabilité du chemin
	
	
	test1=0
	test2=0
	coordA=[]
	coordA.append(liste[-2]-1)
	coordA.append(liste[-1]-1)
	coordB=[]
	coordB.append(liste[3]-1)
	coordB.append(liste[4]-1)
	voisin_arrivee=voisin(coordA,liste)
	voisin_depart=voisin(coordB,liste)
	for k in voisin_arrivee:
		if matrice[k[1]][k[0]]==0 :
			test1=test1+1
			
	for i in voisin_depart:
		if matrice[i[1]][i[0]]==0 :
			test2=test2+1
	
	if test1>(len(voisin_arrivee)-1) or test2>(len(voisin_depart)-1) :
		return False
	return True
		
	


