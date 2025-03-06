import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class DialogueNoeud(object):
    def setupUi(self, Dialog):
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 260)
        Dialog.setFixedSize(QtCore.QSize(350, 260))
        self.bg_frame = QtWidgets.QFrame(Dialog)
        self.bg_frame.setGeometry(QtCore.QRect(0, -1, 350, 261))
        self.bg_frame.setStyleSheet("background-color: #495466;")
        self.bg_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bg_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bg_frame.setObjectName("bg_frame")
        self.label_titre = QtWidgets.QLabel(self.bg_frame)
        self.label_titre.setGeometry(QtCore.QRect(0, 0, 350, 31))
        self.label_titre.setMaximumSize(QtCore.QSize(16777215, 160))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_titre.setFont(font)
        self.label_titre.setStyleSheet("color: #DCE4F2;")
        self.label_titre.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titre.setObjectName("label_titre")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.bg_frame)
        self.buttonBox.setGeometry(QtCore.QRect(0, 230, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.buttonBox.setFont(font)
        self.buttonBox.setStyleSheet("QPushButton{\n"
"border: none;\n"
"padding: 5px 5px;\n"
"width: 40px;\n"
"background: #39414E;\n"
"color: #DCE4F2;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background: #DCE4F2;\n"
"color: #39414E;\n"
"}")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.bg_frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 30, 351, 201))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.formLayoutWidget.setFont(font)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setContentsMargins(5, 0, 10, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_racine = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_racine.setFont(font)
        self.label_racine.setStyleSheet("color: #DCE4F2;")
        self.label_racine.setObjectName("label_racine")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_racine)
        self.entry_cle = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        self.entry_cle.setFont(font)
        self.entry_cle.setStyleSheet("border: none;\n"
"padding: 2px 5px;\n"
"background: #39414E;\n"
"color: #DCE4F2;\n"
"")
        self.entry_cle.setText("")
        self.entry_cle.setObjectName("entry_cle")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.entry_cle)
        self.label_couleur = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_couleur.setFont(font)
        self.label_couleur.setStyleSheet("color: #DCE4F2;")
        self.label_couleur.setObjectName("label_couleur")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_couleur)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_colorpicker = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        self.btn_colorpicker.setFont(font)
        self.btn_colorpicker.setStyleSheet("QPushButton{\n"
"border: none;\n"
"padding: 5px 5px;\n"
"color: #242931;\n"
"background-color: #52ABFF;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"text-decoration: underline;\n"
"}")
        self.btn_colorpicker.setObjectName("btn_colorpicker")
        self.gridLayout.addWidget(self.btn_colorpicker, 0, 0, 1, 1)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.gridLayout)
        self.label_etiquette = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_etiquette.setFont(font)
        self.label_etiquette.setStyleSheet("color: #DCE4F2;")
        self.label_etiquette.setObjectName("label_etiquette")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_etiquette)
        self.entry_etiquette = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        self.entry_etiquette.setFont(font)
        self.entry_etiquette.setStyleSheet("QPlainTextEdit {\n"
"border: none;\n"
"padding: 2px 5px;\n"
"background: #39414E;\n"
"color: #DCE4F2;\n"
"}")
        self.entry_etiquette.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.entry_etiquette.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.entry_etiquette.setPlainText("")
        self.entry_etiquette.setObjectName("entry_etiquette")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.entry_etiquette)
        self.label_SAG = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_SAG.setFont(font)
        self.label_SAG.setStyleSheet("color: #DCE4F2;")
        self.label_SAG.setObjectName("label_SAG")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_SAG)
        self.check_sag = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        self.check_sag.setFont(font)
        self.check_sag.setToolTip("")
        self.check_sag.setStyleSheet("QCheckBox {\n"
"    color: #DCE4F2;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    background: #39414E;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background: #52abff;\n"
"}\n"
"")
        self.check_sag.setText("")
        self.check_sag.setTristate(False)
        self.check_sag.setObjectName("check_sag")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.check_sag)
        self.label_SAD = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_SAD.setFont(font)
        self.label_SAD.setStyleSheet("color: #DCE4F2;")
        self.label_SAD.setObjectName("label_SAD")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_SAD)
        self.check_sad = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        self.check_sad.setFont(font)
        self.check_sad.setStyleSheet("QCheckBox {\n"
"    color: #DCE4F2;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    background: #39414E;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background: #52abff;\n"
"}\n"
"")
        self.check_sad.setText("")
        self.check_sad.setObjectName("check_sad")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.check_sad)
        self.label_parent_res = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_parent_res.setFont(font)
        self.label_parent_res.setToolTip("")
        self.label_parent_res.setStyleSheet("border: none;\n"
"padding: 2px 5px;\n"
"background: #39414E;\n"
"color: #9196a1;\n"
"")
        self.label_parent_res.setText("")
        self.label_parent_res.setObjectName("label_parent_res")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_parent_res)
        self.label_parent = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_parent.setFont(font)
        self.label_parent.setStyleSheet("color: #DCE4F2;")
        self.label_parent.setObjectName("label_parent")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_parent)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.btn_colorpicker.clicked.connect(self.ouvrir_colorpicker)

    def ouvrir_colorpicker(self):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            self.btn_colorpicker.setStyleSheet(f"QPushButton {{ border: none; padding: 5px 5px; color: #242931; background-color: {color.name()}; }} QPushButton:hover {{ text-decoration: underline; }}")
            self.btn_colorpicker.setText(color.name())

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Créer un arbre"))
        self.label_titre.setText(_translate("Dialog", "Informations"))
        self.label_racine.setToolTip(_translate("Dialog", "Nom du noeud racine de l\'arbre ou sous-arbre"))
        self.label_racine.setText(_translate("Dialog", "Racine"))
        self.entry_cle.setToolTip(_translate("Dialog", "Changer la clé du noeud"))
        self.label_couleur.setToolTip(_translate("Dialog", "Couleur de ce noeud"))
        self.label_couleur.setText(_translate("Dialog", "Couleur"))
        self.btn_colorpicker.setText(_translate("Dialog", "#52abff"))
        self.label_etiquette.setToolTip(_translate("Dialog", "Description ou note associée à ce noeud"))
        self.label_etiquette.setText(_translate("Dialog", "Étiquette"))
        self.label_SAG.setToolTip(_translate("Dialog", "Le sous-arbre gauche (SAG) attaché à ce noeud"))
        self.label_SAG.setText(_translate("Dialog", "S.A.G."))
        self.label_SAD.setToolTip(_translate("Dialog", "Le sous-arbre droit (SAG) attaché à ce noeud"))
        self.label_SAD.setText(_translate("Dialog", "S.A.D."))
        self.label_parent.setToolTip(_translate("Dialog", "noeud parent ce noeud"))
        self.label_parent.setText(_translate("Dialog", "Parent"))
