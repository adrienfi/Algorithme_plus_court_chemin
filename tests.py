# -*- coding: utf-8 -*-

# ce programme permet de faire des tests au fur et à mesure du développement, il ne fait pas partie du projet final

from random import randint
import numpy as np
"""
#from constantes import *
#from types_projet import *
#from fonctions_logique import *
#from fonctions_console import *

#p = Position(0,0)

#print(p.x)
#print(p.y)

def generer_grille(Pdensite,Pdimx,Pdimy,Xdepart,Ydepart,Xstop,Ystop): 

	
	nbrecasepleine=int((Pdensite/100)*Pdimx*Pdimy) #nombre de case remplis nécéssaire pour faire les murs
	nbcasespleinesCompte=0
	#print(nbrecasepleine) verification
	grille=np.zeros((Pdimx,Pdimy)) #Création de notre grille vide aux bonne dimenssions 
	grille[Xdepart-1][Ydepart-1]=2
	grille[Xstop-1][Ystop-1]=3
	
	
	while nbcasespleinesCompte != (nbrecasepleine-1):
			
		nbcasespleinesCompte=comptage_1(grille)
				
		a=randint(0,Pdimx-1)
		b=randint(0,Pdimy-1)
		grille[a][b]=1
		#print(nbcasespleinesCompte) vérification 
		
	
			
	return grille
	
	
	
def comptage_1(matrice) : 
	j=0
	nb1=0
	while j<=matrice.shape[1]-1:
		
		for i in range (0,matrice.shape[0]-1):
			
			if matrice [i][j]==1:
				nb1=nb1+1
		j=j+1
		
	return nb1
	
	
def test_entier(valeur): #retourn un NL 0 ou 1 en fonction du type de la variable 
	i=0
		
	try:
		
		valeur=int(valeur)
	
	except : 
		
		i=0
		
			
	if type(valeur) == int :
			
		i=1
			
	return i 
	
	
def test_longueur (Pliste) : 
	
	NivL=0
	
	if len(Pliste)==2 :
		NivL=1
	else :
		NivL=0
	return NivL
		
def aquisition_donnees_position_depart(): #reccupere les positions du point de départ 
	
	PdepartX=input("Xdepart ? :")
	PdepartY=input("Ydepart ? :")
	Pdepart=[PdepartX,PdepartY]
	
	if test_longueur(Pdepart)==1 & test_entier(Pdepart[0])==1 & test_entier(Pdepart[1])==1:
		
		Pdepart=[int(x) for x in Pdepart]
		return Pdepart
	else : 
		
		return aquisition_donnees_position()
		
def aquisition_donnees_position_stop():#reccupere les positions du point d'arrivé
	
	PstopX=input("Xstop ? :")
	PstopY=input("Ystop ? :")
	Pstop=[PstopX,PstopY]
	
	if test_longueur(Pstop)==1 & test_entier(Pstop[0])==1 & test_entier(Pstop[1])==1:
		
		Pstop=[int(x) for x in Pstop]
		return Pstop
		
	else : 
		return aquisition_donnees_position_stop()

def aquisition_donnees_position (): # verifie que le point de départ et d'arriver ne sont pas confondus et concataine les résultats des deux fonctions précédentes
		
	ps=aquisition_donnees_position_depart()
	pa=aquisition_donnees_position_stop()
	print (pa)
	print(ps)

	while pa[0]==ps[0] :
		while pa[1]==ps[1] :
		
			print ("depart et arrivee ne peuvent pas etre confondus, rentrer un nouveau point d'arrivee")
			ps=aquisition_donnees_position_stop()
		
	else :
			
		l=[ps[0],ps[1],pa[0],pa[1]]
		return l 
		
		
def aquisition_donnees():# Aquisition de l'ensemble des paramètres : Densitee/dimX/dimY/Pdepart/Parrivee 
	
	
	Pdens=input("Densitee") #Gestion des entrés biaisées sur Pdens 
	NL=test_entier(Pdens)
	
	while NL !=1  :
		
		Pdens=input("rentrer une valeur entiere")
		NL=test_entier(Pdens)
		
	Pdens=int(Pdens)
	
	while Pdens <=10 or Pdens >50 :
		
		NL=test_entier(Pdens)
		
		while NL==0 :
			
			Pdens=input("rentrer une valeur entiere")
			NL=test_entier(Pdens)
		
		else  :
			
			Pdens=input("Pdens est compris entre 10 et 50, votre Pdens? :")
			Pdens=int(Pdens)
			
			
		
		
		
			
	dimX=input("dimX :")  ##Gestion des entrés biaisées sur dimX
	
	NL=test_entier(dimX)
	
	while NL !=1  :
		
		dimX=input("rentrer une valeur entiere :")
		NL=test_entier(dimX)
		
	dimX=int(dimX)
	
	while dimX <=3 or dimX >10 :
		
		NL=test_entier(dimX)
		
		while NL==0 :
			
			dimX=input("rentrer une valeur entiere :")
			NL=test_entier(dimX)
		
		else  :
			
			dimX=input("dimX est compris entre 3 et 10; votre dimX ? :")
			dimX=int(dimX)
		
		
		
		
		
		
		
	dimY=input("dimY :")  ##Gestion des entrés biaisées sur dimY
	
	NL=test_entier(dimY)
	
	while NL !=1  :
		
		dimY=input("rentrer une valeur entiere :")
		NL=test_entier(dimY)
		
	dimY=int(dimY)
	
	while dimY <=3 or dimY >10 :
		
		NL=test_entier(dimY)
		
		while NL==0 :
			
			dimY=input("rentrer une valeur entiere :")
			NL=test_entier(dimY)
		
		else  :
			
			dimY=input("dimY est compris entre 3 et 10; votre dimX ? :")
			dimY=int(dimY)
			
			
		
		
	donnees_position=aquisition_donnees_position()   # aquisition des donnees sur les points de depart et d'arriver 
		
			
	
		
	return [Pdens,dimX,dimY,donnees_position[0],donnees_position[1],donnees_position[2],donnees_position[3]] 	
	


donnees=aquisition_donnees()
print(generer_grille(donnees[0],donnees[1],donnees[2],donnees[3],donnees[4],donnees[5],donnees[6]))

#print (aquisition_donnees())


"""
	
"""def voisin(l): #donne les voisins d'un point
	#Le programme test si les 4 voisins du point sont dans la matrice, et les ajoute à la liste potes_du_point si ils sont dans la matrice
	potes_du_point=[]
	if l[1]-1>=0:
		point=[]
		point.append(l[0])
		point.append(l[1]-1)
		potes_du_point.append(point)
	if l[1]+1<=aquisition_donnees[3]-1
		point=[]
		point.append(l[0])
		point.append(l[1]+1)
		potes_du_point.append(point)
	if l[0]+1<=aquisition_donnees[2]-1
		point=[]
		point.append(l[0]+1)
		point.append(l[1])
		potes_du_point.append(point)
	if l[0]-1>=0
		point=[]
		point.append(l[0]-1)
		point.append(l[1])
		potes_du_point.append(point)
	return potes_du_point
		
		
		
#AUTRE PROGRAMME

	coord=[]
	coord.append(donnees[3])
	coord.append(donnees[4])
	l=voisin(coord) #renvoie la liste des voisins du point de départ
	numero_case_libre=max(donnees[1],[donnees[2])**2+1 #numero du départ
	numero_case_mur=nombre_case_libre+1 #numéro des murs
	numero_case-arrivee=numero_case_mur+1
	dist=np.full((donnees[1],donnees[2]),int(numero_case_libre))
	dist=[[nombre_case_libre for k in range donnees[2]] for j in range donnees[1]] #creer une liste rempli de grand nombre #dist 
	dist[coord[1]][coord[0]]=0 #le point de depart est a la distance 0
	dist[donnees[5]]][donnees[4]]=numero_case-arrivee
	
	for i in range len(matrice): #la matrice dist prend la valeur numéro des murs si il y a un mur
		for j in range len(matrice[0]):
			if matrice[i][j]==1:
				dist[i][j]=numero_case_mur
	
	for k in l :
		dist[k[1]][k[0]]=1 #met a la distance 1 les voisins du point de depart
	while len(l)!=0:
		point_a_traiter=l.pop()
		for x in voisin(point_a_traiter):
			if dist[[x[1]][x[0]]==numero_case_libre and dist[[x[0]][x[1]]==:
				dist[[x[1]][x[0]]=dist[[point_a_traiter[1]][point_a_traiter[0]]+1
				l.append(x)
	print(dist)"""

def bite ():
	return("bire")
	
print(bite())
