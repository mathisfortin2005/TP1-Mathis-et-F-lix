import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from abc import ABC, abstractmethod


class Polygone(ABC):

    _liste_vecteurs = []
    def __init__(self,*args):
        self._liste_vecteurs = _liste_vecteurs + vecteur4

    @property
    def liste_vecteurs(self):
        return self._liste_vecteurs

    @liste_vecteurs.setter
    def liste_vecteurs(self, nouvelle_liste):
        self._liste_vecteurs = nouvelle_liste

    # doit retourner l'aire du polygone
    @abstractmethod
    def aire(self):
        pass

    # doit retourner le périmètre du polygone
    def perimetre(self):
        # Ajouter l'implémentation de la méthode perimetre(self)
        longueur_initiale = 0
        for i in range(1, Polygone.nb_cotes(self)):
            a = Polygone.liste_vecteurs[i]
            longueur = Vecteur.longueur(a)
            longueur_initiale = int(longueur) + longueur_initiale

        """
        perimetre = 0
        nombre_cotes = self.nb_cotes()
        if nombre_cotes < 3:
            ValueError("Les données entrées ne correspondent pas à un polygone car il n'y a pas au moins 3 côtés")
        elif nombre_cotes == 3:
            pass
        elif nombre_cotes == 4:
            pass
        else:
            pass
        return perimetre
        """

    #La méthode nb_cotes retourne le nombre de côtés du polygone
    def nb_cotes(self):
        # Ajouter l'implémentation de la méthode nb_cotes(self)
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

class Triangle(Polygone)

    super.__init__(self)

class Point:

    def __init__(self, x, y):
        self._x = x
        self._y = y

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


pointA = Point(2, 2)
pointB = Point(4, 2)
pointC = Point(4, 4)
pointD = Point(4, 2)
vecteur1 = Vecteur(pointA, pointB)
vecteur2 = Vecteur(pointB, pointC)
vecteur3 = Vecteur(pointC, pointD)
vecteur4 = Vecteur(pointD, pointA)

print(vecteur1.longueur())