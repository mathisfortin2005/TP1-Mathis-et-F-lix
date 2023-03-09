"""
TP1
Noms : Mathis Fortin et Félix Chamberland
Groupe : 00002
Travail réalisé dans le cadre du cours "420 SD2-HY Programmation orientée objet" donné par M. Pier Luc Ducharme
Dernière modification : 2023-03-09
Version 1
"""

import csv


# Arbre binaire de recherche
class Noeud:

    def __init__(self, equipe):
        self._equipe = equipe
        self._gauche = None
        self._droite = None

    @property
    def gauche(self):
        return self._gauche

    @gauche.setter
    def gauche(self, valeur):
        self._gauche = valeur

    @property
    def droite(self):
        return self._droite

    @droite.setter
    def droite(self, valeur):
        self._droite = valeur

    #La méthode insertion permet de créer l'arbre
    def insertion(self, equipe):
        if equipe.total_points() < self._equipe.total_points():
            if self._gauche is None:
                self.__gauche = Noeud(equipe)
            else:
                self.__gauche.insertion(equipe)
        else:
            if self._droite is None:
                self._droite = Noeud(equipe)
            else:
                self._droite.insertion(equipe)

    #La méthode afficher_arbre permet d'afficher l'arbre
    def afficher_arbre(self):
        if self._gauche:
            self._gauche.afficher_arbre()
        self._equipe.afficher(),
        if self._droite:
            self._droite.afficher_arbre()


class EquipeLNH:

    def __init__(self, nom, data):
        self.__nom = nom
        self.__data = data

    @property
    def equipe(self):
        return self.__equipe

    @equipe.setter
    def equipe(self, valeur):
        self.__equipe = valeur

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, valeur):
        self.__nom = valeur

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, valeur):
        self.__data = valeur

    #La méthode total_points retourne le nombre de points
    def total_points(self):
        points = int(self.data['V'])*2 + int(self.data['DP'])
        #Permet d'aller chercher les données à partir d'une liste et de faire le calcul
        return points

    #La méthode moyenne_but_par_match retourne le nombre de but par match moyen
    def moyenne_but_par_match(self):
        moyennes_buts = int(self.data['BP'])/int(self.data['MJ'])
        return moyennes_buts

    def afficher(self):
        print(self.nom + '\t\t\tPts: ' + str(self.total_points()) + '\tBP/MJ: ' + str(self.moyenne_but_par_match()))


class DataUtils:

    @staticmethod
    def load_data(filename):
        liste_equipes = []
        with open(filename, 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            lignes = 0
            for ligne in reader:
                if lignes == 0:
                    print("Ignorer l'entete")
                    lignes += 1
                else:
                    equipe = EquipeLNH(ligne[0], {'MJ': ligne[2], 'V': ligne[3], 'DP': ligne[6], 'BP': ligne[12]})
                    liste_equipes.append(equipe)
                    lignes += 1
            return liste_equipes

    #La méthode moyenne_haut_bas prend en entrée la liste d'équipe et retourne 2 tuples, bas et haut,
    #Le tuple bas contient les équipes qui sont sous la moyenne de but par match
    #Le tuple haut contient les équipes qui sont sur ou égales à la moyenne de but par match
    @staticmethod
    def moyenne_haut_bas(liste_equipes):
        moyenne_but_equipe = 0 #Initialisation de la variable moyenne_but_equipe
        listebas = [] #Création de la liste listebas
        listehaut = [] #Création de la liste listehaut
        for i in range(len(liste_equipes)):
            moyenne_but_equipe += liste_equipes[i].moyenne_but_par_match()
        moyenne_but_tt_equipe = moyenne_but_equipe / len(liste_equipes)
        for j in range(len(liste_equipes)):
            if moyenne_but_tt_equipe < liste_equipes[j].moyenne_but_par_match():
                listebas.append(liste_equipes[j])
            else:
                listehaut.append(liste_equipes[j])
        bas = tuple(listebas)
        haut = tuple(listehaut)
        return bas, haut


# Code pour tester
racine = None
liste_equipes = DataUtils.load_data('./data/nhl.csv')
for equipe in liste_equipes:
    if racine is None:
        racine = Noeud(equipe)
    else:
        racine.insertion(equipe)

racine.afficher_arbre()

bas, haut = DataUtils.moyenne_haut_bas(liste_equipes)

print('En dessous de la moyenne BP/MJ')
for equipe in bas:
    equipe.afficher()
print('Au dessus de la moyenne BP/MJ')
for equipe in haut:
    equipe.afficher()
