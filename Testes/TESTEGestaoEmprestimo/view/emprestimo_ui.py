# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'selecao_uniforme.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(341, 227)
        Dialog.setMinimumSize(QSize(341, 227))
        self.horizontalLayout_3 = QHBoxLayout(Dialog)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txt_cpf_emprestimo = QLineEdit(self.widget)
        self.txt_cpf_emprestimo.setObjectName(u"txt_cpf_emprestimo")

        self.horizontalLayout_2.addWidget(self.txt_cpf_emprestimo)

        self.btn_consulta_funcionario = QPushButton(self.widget)
        self.btn_consulta_funcionario.setObjectName(u"btn_consulta_funcionario")

        self.horizontalLayout_2.addWidget(self.btn_consulta_funcionario)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.txt_nome_funcionario = QLineEdit(self.widget)
        self.txt_nome_funcionario.setObjectName(u"txt_nome_funcionario")

        self.verticalLayout_2.addWidget(self.txt_nome_funcionario)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cb_uniforme = QComboBox(self.widget)
        self.cb_uniforme.addItem("")
        self.cb_uniforme.addItem("")
        self.cb_uniforme.addItem("")
        self.cb_uniforme.setObjectName(u"cb_uniforme")

        self.horizontalLayout.addWidget(self.cb_uniforme)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.btn_emprestar = QPushButton(self.widget)
        self.btn_emprestar.setObjectName(u"btn_emprestar")

        self.verticalLayout_2.addWidget(self.btn_emprestar)


        self.horizontalLayout_3.addWidget(self.widget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"CPF do funcion\u00e1rio", None))
        self.btn_consulta_funcionario.setText(QCoreApplication.translate("Dialog", u"Consultar", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Nome funcion\u00e1rio", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Selecione o tipo de uniforme", None))
        self.cb_uniforme.setItemText(0, QCoreApplication.translate("Dialog", u"Selecione", None))
        self.cb_uniforme.setItemText(1, QCoreApplication.translate("Dialog", u"Gar\u00e7om", None))
        self.cb_uniforme.setItemText(2, QCoreApplication.translate("Dialog", u"Cozinha", None))

        self.btn_emprestar.setText(QCoreApplication.translate("Dialog", u"Confirmar", None))
    # retranslateUi

