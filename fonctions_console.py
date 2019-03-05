# -*- coding: utf-8 -*-
# compatibilité avec python 2.X pour FreeCAD
# from __future__ import print_function

# cette bibliothèque con  tient les fonctions du projet liées à la saisie/l'affichage console
# elle est utilisée par la partie 1 du projet

from types_projet import *


def test_entier(valeur): #retourne un NL 0 ou 1 en fonction du type de la variable 
	
	i=0
		
	try:
		
		valeur=int(valeur)
	
	except : 
		
		i=0
		
			
	if type(valeur) == int :
			
		i=1
			
	return i 

def test_longueur (Pliste) : # Fonction vérifiant que la longueur d'une liste est bien de 2 (utilisé pour l'aquisition des coordonnées des points de départ et de stop)
	
	NivL=0
	
	if len(Pliste)==2 :
		NivL=1
	else :
		NivL=0
	return NivL

def aquisition_donnees_position_depart(): #reccupere les coordonnées du point de départ 
	
	PdepartX=input("Xdepart ? :")
	PdepartY=input("Ydepart ? :")
	Pdepart=[PdepartX,PdepartY]
	
	if test_longueur(Pdepart)==1 & test_entier(Pdepart[0])==1 & test_entier(Pdepart[1])==1:
		
		Pdepart=[int(x) for x in Pdepart]
		return Pdepart
	else : 
		
		return aquisition_donnees_position()
		
def aquisition_donnees_position_stop():#reccupere les coordonnées du point d'arrivé
	
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
	

	while pa[0]==ps[0] :
		while pa[1]==ps[1] :
		
			print ("depart et arrivee ne peuvent pas etre confondus, rentrer un nouveau point d'arrivee")
			ps=aquisition_donnees_position_stop()
		
	else :
			
		l=[ps[0],ps[1],pa[0],pa[1]]
		return l 
		
def aquisition_donnees():# Aquisition de l'ensemble des paramètres : Densitee/dimX/dimY
	
	
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
	
	while dimX <=5 or dimX >10 :
		
		NL=test_entier(dimX)
		
		while NL==0 :
			
			dimX=input("rentrer une valeur entiere :")
			NL=test_entier(dimX)
		
		else  :
			
			dimX=input("dimX est compris entre 5 et 10; votre dimX ? :")
			dimX=int(dimX)
		
		
		
		
			
	dimY=input("dimY :")  ##Gestion des entrés biaisées sur dimY
	
	NL=test_entier(dimY)
	
	while NL !=1  :
		
		dimY=input("rentrer une valeur entiere :")
		NL=test_entier(dimY)
		
	dimY=int(dimY)
	
	while dimY <=5 or dimY >10 :
		
		NL=test_entier(dimY)
		
		while NL==0 :
			
			dimY=input("rentrer une valeur entiere :")
			NL=test_entier(dimY)
		
		else  :
			
			NL=test_entier(dimY)	
			dimY=input("dimY est compris entre 5 et 10; votre dimX ? :")
			dimY=int(dimY)
			
		
	 	
	return [Pdens,dimY,dimX]




