import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from dialogue_noeud import DialogueNoeud
from classe_arbre import Arbre

mainStyleSheet = """

QMainWindow{
    background-color: #2c3e50;
}

QToolTip {
    border: 2px solid #52ABFF;
    padding: 5px;
    opacity: 230;
    color: #DCE4F2;
}
"""


class MainWindowUI(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1089, 600)
        MainWindow.setFixedSize(QtCore.QSize(1089, 600))
        MainWindow.setWindowIcon(QtGui.QIcon('ressources/icon.png'))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 861, 601))
        self.frame_2.setStyleSheet("background-color:#242931;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(860, 0, 231, 601))
        self.frame.setStyleSheet("background-color: #495466;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 231, 551))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(5, 0, 7, 0)
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setVerticalSpacing(8)
        self.formLayout.setObjectName("formLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #DCE4F2;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.label_etiquette = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(10)
        font.setItalic(True)
        font.setWeight(75)
        self.label_etiquette.setFont(font)
        self.label_etiquette.setStyleSheet("color: #DCE4F2;")
        self.label_etiquette.setAlignment(QtCore.Qt.AlignCenter)
        self.label_etiquette.setObjectName("label_etiquette")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.label_etiquette)
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        self.label_taille = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label_taille.setFont(font)
        self.label_taille.setStyleSheet("color: #DCE4F2;")
        self.label_taille.setObjectName("label_taille")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_taille)
        self.valeur_taille = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiBold")
        font.setPointSize(10)
        self.valeur_taille.setFont(font)
        self.valeur_taille.setStyleSheet("color: #DCE4F2;")
        self.valeur_taille.setObjectName("valeur_taille")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.valeur_taille)
        self.label_hauteur = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label_hauteur.setFont(font)
        self.label_hauteur.setStyleSheet("color: #DCE4F2;")
        self.label_hauteur.setObjectName("label_hauteur")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_hauteur)
        self.valeur_hauteur = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiBold")
        font.setPointSize(10)
        self.valeur_hauteur.setFont(font)
        self.valeur_hauteur.setStyleSheet("color: #DCE4F2;")
        self.valeur_hauteur.setObjectName("valeur_hauteur")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.valeur_hauteur)
        self.label_LC = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label_LC.setFont(font)
        self.label_LC.setStyleSheet("color: #DCE4F2;")
        self.label_LC.setObjectName("label_LC")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_LC)
        self.valeur_LC = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiBold")
        font.setPointSize(10)
        self.valeur_LC.setFont(font)
        self.valeur_LC.setStyleSheet("color: #DCE4F2;")
        self.valeur_LC.setObjectName("valeur_LC")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.valeur_LC)
        self.label_LCE = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label_LCE.setFont(font)
        self.label_LCE.setStyleSheet("color: #DCE4F2;")
        self.label_LCE.setObjectName("label_LCE")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_LCE)
        self.valeur_LCE = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiBold")
        font.setPointSize(10)
        self.valeur_LCE.setFont(font)
        self.valeur_LCE.setStyleSheet("color: #DCE4F2;")
        self.valeur_LCE.setObjectName("valeur_LCE")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.valeur_LCE)
        self.label_LCI = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label_LCI.setFont(font)
        self.label_LCI.setStyleSheet("color: #DCE4F2;")
        self.label_LCI.setObjectName("label_LCI")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_LCI)
        self.valeur_LCI = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiBold")
        font.setPointSize(10)
        self.valeur_LCI.setFont(font)
        self.valeur_LCI.setStyleSheet("color: #DCE4F2;")
        self.valeur_LCI.setObjectName("valeur_LCI")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.valeur_LCI)
        self.label_PM = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label_PM.setFont(font)
        self.label_PM.setStyleSheet("color: #DCE4F2;")
        self.label_PM.setObjectName("label_PM")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_PM)
        self.valeur_PM = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiBold")
        font.setPointSize(10)
        self.valeur_PM.setFont(font)
        self.valeur_PM.setStyleSheet("color: #DCE4F2;")
        self.valeur_PM.setObjectName("valeur_PM")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.valeur_PM)
        self.label_PME = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label_PME.setFont(font)
        self.label_PME.setStyleSheet("color: #DCE4F2;")
        self.label_PME.setObjectName("label_PME")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_PME)
        self.valeur_PME = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiBold")
        font.setPointSize(10)
        self.valeur_PME.setFont(font)
        self.valeur_PME.setStyleSheet("color: #DCE4F2;")
        self.valeur_PME.setObjectName("valeur_PME")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.valeur_PME)
        self.label_PMI = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label_PMI.setFont(font)
        self.label_PMI.setStyleSheet("color: #DCE4F2;")
        self.label_PMI.setObjectName("label_PMI")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_PMI)
        self.valeur_PMI = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiBold")
        font.setPointSize(10)
        self.valeur_PMI.setFont(font)
        self.valeur_PMI.setStyleSheet("color: #DCE4F2;")
        self.valeur_PMI.setObjectName("valeur_PMI")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.valeur_PMI)
        self.label_repr = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label_repr.setFont(font)
        self.label_repr.setStyleSheet("color: #DCE4F2;")
        self.label_repr.setObjectName("label_repr")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.SpanningRole, self.label_repr)
        self.entry_repr = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        self.entry_repr.setFont(font)
        self.entry_repr.setStyleSheet("background-color: #39414E;\n"
"border:none;\n"
"color: #DCE4F2;")
        self.entry_repr.setObjectName("entry_repr")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.SpanningRole, self.entry_repr)
        self.entry_repr.setReadOnly(True)
        self.entry_repr.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.entry_repr.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        spacerItem2 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(13, QtWidgets.QFormLayout.SpanningRole, spacerItem2)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 550, 231, 52))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #---------------------------------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------------------------------

        self.boutons = []
        self.arbre = Arbre("R")
        self.label_etiquette.setToolTip(self.arbre.getEtiquette())
        self.creer_btn_arbre(self.arbre)

        self.mettre_a_jour_calculs(self.arbre)

    def creer_btn_arbre(self, arbre, sag=False, sad=False):
        """Créer un btn pour chaque noeud de l'arbre et le positionner."""
        
        #creer btn
        btn_arbre = QtWidgets.QPushButton(self.frame_2)
        btn_arbre.clicked.connect(lambda checked, arbre=arbre: self.ouvrir_dialogue(arbre, btn_arbre))
        btn_arbre.setGeometry(QtCore.QRect(40, 40, 40, 40)) 

        btn_arbre.setToolTip(f"Racine: {arbre.getRacine()}\nÉtiquette: `{arbre.getEtiquette()}`")

        #style
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        btn_arbre.setStyleSheet(
            "QPushButton { background-color: #52abff; color: #242931; padding: 4px; border: none; } "
            "QPushButton:hover { background-color: #DCE4F2; color: #39414E; }"
        )
        btn_arbre.setObjectName(f"btn_arbre_{arbre.racine}")
        btn_arbre.setText(arbre.racine) #txt du bouton = le nom du nœud

        if arbre.parent is not None:
            if sag:
                btn_arbre.move(arbre.getX(), arbre.getY())
            elif sad:  # Sous-arbre droit
                btn_arbre.move(arbre.getX(), arbre.getY())
        else:
            btn_arbre.move(arbre.getX(), arbre.getY())

        btn_arbre.show()

        self.boutons.append(btn_arbre) #stocker le bouton dans une liste (ça peut servir)

    def ouvrir_dialogue(self, arbre, bouton):
        #stopper le dialogue (4 niveaux max)
        dico_hauteur = arbre.Hauteur(arbre.getRacineUltime())
        niveau_max = max(dico_hauteur.values())  
        niveau_arbre = dico_hauteur.get(arbre.getRacine(), -1)
        if niveau_max and niveau_arbre >= 4:
            bloque = True
        else:
            bloque = False

        dialog = QtWidgets.QDialog()
        dialog.ui = DialogueNoeud()
        dialog.ui.setupUi(dialog)

        #mise en place des valeurs
        couleur_bg = bouton.styleSheet().split('background-color:')[1].split(';')[0].strip() #pour récuperer la couleur
        dialog.ui.btn_colorpicker.setText(couleur_bg)
        dialog.ui.btn_colorpicker.setStyleSheet(f"QPushButton {{ border: none; padding: 5px 5px; color: #242931; background-color: {couleur_bg}; }} QPushButton:hover {{ text-decoration: underline; }}")
        if arbre.getParent() is not None:
                dialog.ui.label_parent_res.setText(arbre.getParent().getRacine())
        else:
                dialog.ui.label_parent_res.setText("Aucun parent")
        dialog.ui.entry_cle.setText(arbre.getRacine())
        dialog.ui.entry_etiquette.setPlainText(arbre.getEtiquette())

        if bloque:
            dialog.ui.check_sag.hide()
            dialog.ui.label_SAG.hide()
            dialog.ui.check_sad.hide()
            dialog.ui.label_SAD.hide()

        if arbre.Sag:
            dialog.ui.check_sag.setChecked(True)
            dialog.ui.check_sag.setText(f"(arbre {arbre.getSag().getRacine()})")
            dialog.ui.check_sag.setEnabled(False)
        if arbre.Sad:
            dialog.ui.check_sad.setChecked(True)
            dialog.ui.check_sad.setText(f"(arbre {arbre.getSad().getRacine()})")
            dialog.ui.check_sad.setEnabled(False)

        dialog.ui.buttonBox.accepted.connect(lambda: self.mettre_a_jour_btn(bouton, dialog.ui.entry_cle.text(), dialog.ui.entry_etiquette.toPlainText(), dialog.ui.btn_colorpicker.text(), arbre, dialog.ui.check_sag.isChecked(), dialog.ui.check_sad.isChecked()))

        dialog.exec_()

    def mettre_a_jour_btn(self, bouton, racine, etiquette, couleur_bg, arbre, sag, sad):
        #mettre a jour le btn
        bouton.setText(racine)
        bouton.setStyleSheet(f"QPushButton {{ background-color: {couleur_bg}; color: #242931; padding: 4px; border: none; }}""QPushButton:hover { background-color: #DCE4F2; color: #39414E; }")

        if sag and arbre.Sag is None:
            arbre.Sag = Arbre(racine + "g", arbre, estSag=True)
            arbre.Sag.parent = arbre
            self.creer_btn_arbre(arbre.Sag, sag=True, sad=False)

        if sad and arbre.Sad is None:
            arbre.Sad = Arbre(racine + "d", arbre, estSag=False)
            arbre.Sad.parent = arbre
            self.creer_btn_arbre(arbre.Sad, sag=False, sad=True)

        #mettre a jour l'arbre
        arbre.setEtiquette(etiquette)

        if arbre.getRacineUltime().getEtiquette() == "":
                self.label_etiquette.setText("aucune étiquette")
                self.label_etiquette.setToolTip("")
        else:
                if len(arbre.getRacineUltime().getEtiquette()) < 27:
                        self.label_etiquette.setText(arbre.getRacineUltime().getEtiquette())
                        self.label_etiquette.setToolTip(arbre.getRacineUltime().getEtiquette())
                else:
                        self.label_etiquette.setText(arbre.getRacineUltime().getEtiquette()[:24]+"...")
                        self.label_etiquette.setToolTip(arbre.getRacineUltime().getEtiquette())

        arbre.setRacine(racine)
        self.label.setText(arbre.getRacineUltime().getRacine())
        bouton.setToolTip(f"Racine: {arbre.getRacine()}\nÉtiquette: `{arbre.getEtiquette()}`")

        self.mettre_a_jour_repr()
        self.mettre_a_jour_calculs(arbre)

    def mettre_a_jour_repr(self):
        self.entry_repr.setPlainText(self.arbre.RepresentationArbre())

    def mettre_a_jour_calculs(self, arbre):
        a = arbre.getRacineUltime()

        dico_hauteur = a.Hauteur(a)
        taille_arbre = a.Taille(a)
        lste_feuille = a.LstFeuilles(a)
        lste_noeuds_internes = a.LstNoeudsInternes(a, lste_feuille)
        hauteur_arbre = a.HauteurArbre(dico_hauteur, lste_feuille)
        lcb = a.LC(dico_hauteur)
        lce = a.LCE(dico_hauteur, lste_feuille)
        lci = a.LCI(dico_hauteur, lste_noeuds_internes)
        pm = a.PM(lcb, a)
        pme = a.PME(lce, lste_feuille)
        pmi = a.PMI(lci, lste_feuille, a)
        
        self.valeur_taille.setText(str(taille_arbre))
        self.valeur_hauteur.setText(str(hauteur_arbre))
        self.valeur_LC.setText(str(lcb))
        self.valeur_LCE.setText(str(lce))
        self.valeur_LCI.setText(str(lci))
        self.valeur_PM.setText(str(round(pm,2)))
        self.valeur_PME.setText(str(round(pme,2)))
        self.valeur_PMI.setText(str(round(pmi,2)))

        #---------------------------------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------------------------------

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TreeMaker"))
        self.label.setText(_translate("MainWindow", "R"))
        self.label_etiquette.setText(_translate("MainWindow", "aucune étiquette"))
        self.label_taille.setText(_translate("MainWindow", "Taille:"))
        self.valeur_taille.setText(_translate("MainWindow", "NA"))
        self.label_hauteur.setText(_translate("MainWindow", "Hauteur:"))
        self.valeur_hauteur.setText(_translate("MainWindow", "NA"))
        self.label_LC.setToolTip(_translate("MainWindow", "Longueur de cheminement"))
        self.label_LC.setText(_translate("MainWindow", "LC:"))
        self.valeur_LC.setText(_translate("MainWindow", "NA"))
        self.label_LCE.setToolTip(_translate("MainWindow", "Longueur de cheminement externe"))
        self.label_LCE.setText(_translate("MainWindow", "LCE:"))
        self.valeur_LCE.setText(_translate("MainWindow", "NA"))
        self.label_LCI.setToolTip(_translate("MainWindow", "Longueur de cheminement interne"))
        self.label_LCI.setText(_translate("MainWindow", "LCI:"))
        self.valeur_LCI.setText(_translate("MainWindow", "NA"))
        self.label_PM.setToolTip(_translate("MainWindow", "Profondeur moyenne"))
        self.label_PM.setText(_translate("MainWindow", "PM:"))
        self.valeur_PM.setText(_translate("MainWindow", "NA"))
        self.label_PME.setToolTip(_translate("MainWindow", "Profondeur moyenne Externe"))
        self.label_PME.setText(_translate("MainWindow", "PME:"))
        self.valeur_PME.setText(_translate("MainWindow", "NA"))
        self.label_PMI.setToolTip(_translate("MainWindow", "Profondeur moyenne Interne"))
        self.label_PMI.setText(_translate("MainWindow", "PMI:"))
        self.valeur_PMI.setText(_translate("MainWindow", "NA"))
        self.label_repr.setToolTip(_translate("MainWindow", "Profondeur moyenne Interne"))
        self.label_repr.setText(_translate("MainWindow", "Représentation:"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(mainStyleSheet)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    