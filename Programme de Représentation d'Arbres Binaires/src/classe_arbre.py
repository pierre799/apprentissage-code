class Arbre:
    def __init__(self, racine, parent=None, estSag=None, x=410, y=30):
        self.racine = racine
        self.Sag = None 
        self.Sad = None
        self.etiquette = ""
        self.parent = parent
        
        if parent is not None:  # Si le noeud a un parent
            niv = self.Profondeur() - 1
            w = 410 / (2 ** (niv + 1))
            if estSag:  # Enfant gauche
                self.x = int(parent.getX() - w)
            else:  # Enfant droit]
                self.x = int(parent.getX() + w)
            self.y = parent.getY() + 100
        else:  # Si le noeud est la racine
            self.x = x
            self.y = y
        
    def Profondeur(self):
        if self.parent is None:
            return 0
        else:
            return 1 + self.parent.Profondeur()


    def getRacineUltime(self):
        if self.parent is None:
            return self
        else:
            return self.parent.getRacineUltime()

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getEtiquette(self):
        return self.etiquette

    def setEtiquette(self, etiquette):
        self.etiquette = etiquette

    def getParent(self):
        return self.parent

    def getSag(self):
        return self.Sag

    def getSad(self):
        return self.Sad

    def getRacine(self):
        return self.racine

    def setRacine(self, racine):
        self.racine = racine

    # CALCULS ---------------------------------------------------------------

    def Taille(self, arbre):
        if arbre is None:
            return 0
        return 1+ self.Taille(arbre.Sag) + self.Taille(arbre.Sad)

    def Hauteur(self, arbre):
        if arbre is None or arbre.getRacine() is None:
            return {}
        dico = {}
        pile = [(arbre, 0)] 
        while pile:
            sa, hauteur = pile.pop()
            if sa and sa.getRacine() is not None:
                dico[sa.getRacine()] = hauteur
                if sa.Sad:
                    pile.append((sa.Sad, hauteur + 1))
                if sa.Sag:
                    pile.append((sa.Sag, hauteur + 1))
        
        return dico

    def LstFeuilles(self, arbre):
        lst = []
        if arbre is None:
            return lst

        if arbre.Sag is None and arbre.Sad is None:
            lst.append(str(arbre.racine))
        else:
            if arbre.Sag:
                lst.extend(self.LstFeuilles(arbre.Sag))
            if arbre.Sad:
                lst.extend(self.LstFeuilles(arbre.Sad))
        return lst

    def LC(self, dico_hauteur):
        longeur_tot = 0
        for noeud, hauteur in dico_hauteur.items():
            longeur_tot += hauteur 
        return longeur_tot

    def LCE(self, dico_hauteur, lste_feuille):
        longeur_tot = 0
        for noeud in lste_feuille:
            if noeud in dico_hauteur:
                longeur_tot += dico_hauteur[noeud]
        return longeur_tot

    def LCI(self, dico_hauteur, lst_noeuds_internes):
        longueur = 0
        for noeud in lst_noeuds_internes:
            if noeud in dico_hauteur:
                longueur += dico_hauteur[noeud]
        return longueur

    def PM(self, lcb, arbre):
        taille = self.Taille(arbre)
        if taille != 0:
            return round(lcb / taille, 2)
        else:
            return 0

    def PME(self, lce, lste_feuille):
        if len(lste_feuille) != 0:
            return lce / len(lste_feuille)
        else:
            return 0

    def PMI(self, lci, lst_feuilles, arbre):
        if (self.Taille(arbre) - len(lst_feuilles)) == 0:
            return 0
        profondeur = lci / (self.Taille(arbre) - len(lst_feuilles))
        return round(profondeur, 2)


    def LstNoeudsInternes(self, arbre, lst_feuilles):
        liste = []
        if arbre is None:
            return liste

        if arbre.Sag or arbre.Sad:
            if arbre.racine not in lst_feuilles:
                liste.append(str(arbre.racine))
        
        if arbre.Sag:
            liste.extend(self.LstNoeudsInternes(arbre.Sag, lst_feuilles))
        if arbre.Sad:
            liste.extend(self.LstNoeudsInternes(arbre.Sad, lst_feuilles))
        
        return liste
        
    def HauteurArbre(self, dico_hauteur, lste_feuille):
        return dico_hauteur[max(dico_hauteur)]
        
    def RepresentationArbre(self, prefixe=""):
        result = ""
        if self.racine:
            result += f"{prefixe}■ {self.racine}\n"
        if self.Sag:
            result += self.Sag.RepresentationArbre(prefixe + "-")
        if self.Sad:
            result += self.Sad.RepresentationArbre(prefixe + "-")
        return result

    def __repr__(self):
        return f"[{self.racine}]({self.Sag},{self.Sad})"

if __name__ == "__main__":

    a = Arbre('A')
    a.Sag = Arbre('B') 
    a.Sag.Sag = Arbre('C') 
    a.Sag.Sag.Sag = Arbre('D')
    a.Sag.Sag.Sad = Arbre('E') 
    a.Sad = Arbre('F')
    a.Sad.Sag = Arbre('G')
    a.Sad.Sad = Arbre('H')
    a.Sad.Sad.Sad = Arbre('I')

    print(a.RepresentationArbre())