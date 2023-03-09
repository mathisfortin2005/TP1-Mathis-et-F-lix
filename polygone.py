"""
TP1
Noms : Mathis Fortin et Félix Chamberland
Groupe : 00002
Travail réalisé dans le cadre du cours "420 SD2-HY Programmation orientée objet" donné par M. Pier Luc Ducharme
Dernière modification : 2023-03-09
Version 1
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from abc import ABC, abstractmethod
import math as m


class Polygone(ABC):

    _liste_vecteurs = []

    @property
    def liste_vecteurs(self):
        return self._liste_vecteurs

    @liste_vecteurs.setter
    def liste_vecteurs(self, nouvelle_liste):
        self._liste_vecteurs = nouvelle_liste

    #À COMPLÉTER doit retourner l'aire du polygone
    @abstractmethod
    def aire(self):
        pass

    #La méthode perimetre retourne le périmètre du polygone
    def perimetre(self):
        perimetre = 0
        for i in range(len(self.liste_vecteurs)):
            longueur_cote = self.liste_vecteurs[i].longueur #Utilisation de la méthode longueur
            perimetre += longueur_cote
        return perimetre

    #La méthode nb_cotes retourne le nombre de côtés du polygone
    def nb_cotes(self):
        nombre_cotes = len(self._liste_vecteurs)
        return nombre_cotes

    def afficher_forme(self):
        points = []
        for vecteur in self._liste_vecteurs:
            points.append((vecteur.point_depart.x, vecteur.point_depart.y))
        print("Affichage de " + str(points))
        polygon = Polygon(points)
        fig = plt.figure()
        ax = fig.gca()
        ax.add_patch(polygon)
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        plt.show()


#Création de la classe Triangle qui implémente la classe abstraite Polygone
class Triangle(Polygone):
    #Constructeur de la classe Triangle
    def __init__(self, vecteur1, vecteur2, vecteur3):
        self._vecteur1 = vecteur1
        self._vecteur2 = vecteur2
        self._vecteur3 = vecteur3

    #Méthode pour le calcul de l'aire d'un triangle
    def aire(self):
        hauteur = m.sqrt(self._vecteur2.longueur() * 2 - (self._vecteur1.longueur / 2) * 2)
        aire = (self._vecteur1 * hauteur) / 2
        return aire


#Création de la classe HexagoneRegulier qui implémente la classe abstraite Polygone
class HexagoneRegulier(Polygone):

    #Constructeur de la classe HexagoneRegulier
    def __init__(self, vecteur1, vecteur2, vecteur3, vecteur4, vecteur5, vecteur6):
        self._vecteur1 = vecteur1
        self._vecteur2 = vecteur2
        self._vecteur3 = vecteur3
        self._vecteur4 = vecteur4
        self._vecteur5 = vecteur5
        self._vecteur6 = vecteur6

    #Méthode de calcul de l'aire d'un hexagone régulier
    def aire(self):
        aire = 3 * m.sqrt(3) / 2 * (self._vecteur1) ** 2
        return aire


class Point:

    def __init__(self, x, y):
        self._x = x
        self._y = y

        #Validation de valeur par les points
        if self._x < 10 or 10 < self._x or self._y < 10 or 10 < self._y:
            raise ValueError("La valeur de x ou y doit être entre -10 et 10")

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, valeur):
        self._x = valeur

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, valeur):
        self._y = valeur


class Vecteur:

    def __init__(self, point_depart, point_arrivee):
        self._point_depart = point_depart
        self._point_arrivee = point_arrivee

    @property
    def point_depart(self):
        return self._point_depart

    @point_depart.setter
    def point_depart(self, valeur):
        self._point_depart = valeur

    @property
    def point_arrivee(self):
        return self._point_arrivee

    @point_arrivee.setter
    def point_arrivee(self, valeur):
        self._point_arrivee = valeur

    #La méthode longueur retourne la longueur du polygone
    def longueur(self):
        point1 = self._point_depart #Le point1 représente le point de départ du vecteur
        point2 = self._point_arrivee #Le point2 représente le point d'arrivé du vecteur
        # Pour aller chercher les y
        y1 = point1.y
        y2 = point2.y
        # Pour aller chercher les x
        x1 = point1.x
        x2 = point2.x
        l = ((y2-y1)**2+(x2-x1)**2)**(1/2) #Pour calculer la longueur
        return l

#Valeurs pour faire des tests
pointA = Point(2, 2)
pointB = Point(3, 1)
pointC = Point(4, 2)
pointD = Point(4, 4)
pointE = Point(3, 5)
pointF = Point(2, 4)
vecteur1 = Vecteur(pointA, pointB)
vecteur2 = Vecteur(pointB, pointC)
vecteur3 = Vecteur(pointC, pointD)
vecteur4 = Vecteur(pointD, pointE)
vecteur5 = Vecteur(pointE, pointF)
vecteur6 = Vecteur(pointF, pointA)
vecteur7 = Vecteur(pointA, pointC)
vecteur8 = Vecteur(pointD, pointA)
vecteur1.longueur()
triangle1 = Triangle(vecteur3, vecteur7, vecteur8)#À compléter pour tests
hexagone1 = HexagoneRegulier(vecteur1, vecteur2, vecteur3, vecteur4, vecteur5, vecteur6)#À compléter pour tests