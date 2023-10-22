# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_uniforme.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import view.resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(706, 590)
        MainWindow.setAnimated(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"image: url(:/icon/uniform.png);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.frame)

        self.tab_principal = QTabWidget(self.centralwidget)
        self.tab_principal.setObjectName(u"tab_principal")
        self.tab_inicio = QWidget()
        self.tab_inicio.setObjectName(u"tab_inicio")
        self.horizontalLayout = QHBoxLayout(self.tab_inicio)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.tab_inicio)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_5.addWidget(self.label_5)

        self.btn_receber = QPushButton(self.widget)
        self.btn_receber.setObjectName(u"btn_receber")

        self.verticalLayout_5.addWidget(self.btn_receber)

        self.btn_emprestar = QPushButton(self.widget)
        self.btn_emprestar.setObjectName(u"btn_emprestar")

        self.verticalLayout_5.addWidget(self.btn_emprestar)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.tb_emprestimos_ativos = QTableWidget(self.widget)
        if (self.tb_emprestimos_ativos.columnCount() < 3):
            self.tb_emprestimos_ativos.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_emprestimos_ativos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_emprestimos_ativos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_emprestimos_ativos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tb_emprestimos_ativos.setObjectName(u"tb_emprestimos_ativos")
        self.tb_emprestimos_ativos.verticalHeader().setHighlightSections(False)

        self.verticalLayout_5.addWidget(self.tb_emprestimos_ativos)


        self.horizontalLayout.addWidget(self.widget)

        self.tab_principal.addTab(self.tab_inicio, "")
        self.tab_relatorio = QWidget()
        self.tab_relatorio.setObjectName(u"tab_relatorio")
        self.verticalLayout_4 = QVBoxLayout(self.tab_relatorio)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.tab_relatorio)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_data_inicial = QLabel(self.tab_relatorio)
        self.lbl_data_inicial.setObjectName(u"lbl_data_inicial")

        self.horizontalLayout_5.addWidget(self.lbl_data_inicial)

        self.txt_data_inicial = QLineEdit(self.tab_relatorio)
        self.txt_data_inicial.setObjectName(u"txt_data_inicial")

        self.horizontalLayout_5.addWidget(self.txt_data_inicial)

        self.lbl_data_final = QLabel(self.tab_relatorio)
        self.lbl_data_final.setObjectName(u"lbl_data_final")

        self.horizontalLayout_5.addWidget(self.lbl_data_final)

        self.txt_data_final = QLineEdit(self.tab_relatorio)
        self.txt_data_final.setObjectName(u"txt_data_final")

        self.horizontalLayout_5.addWidget(self.txt_data_final)

        self.btn_consultar_periodo = QPushButton(self.tab_relatorio)
        self.btn_consultar_periodo.setObjectName(u"btn_consultar_periodo")

        self.horizontalLayout_5.addWidget(self.btn_consultar_periodo)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.tb_relatorio = QTableWidget(self.tab_relatorio)
        if (self.tb_relatorio.columnCount() < 4):
            self.tb_relatorio.setColumnCount(4)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_relatorio.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_relatorio.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_relatorio.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_relatorio.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        self.tb_relatorio.setObjectName(u"tb_relatorio")

        self.verticalLayout_4.addWidget(self.tb_relatorio)

        self.tab_principal.addTab(self.tab_relatorio, "")
        self.tab_configuracoes = QWidget()
        self.tab_configuracoes.setObjectName(u"tab_configuracoes")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_configuracoes)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.coluna_funcionario = QWidget(self.tab_configuracoes)
        self.coluna_funcionario.setObjectName(u"coluna_funcionario")
        self.verticalLayout_2 = QVBoxLayout(self.coluna_funcionario)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.coluna_funcionario)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.lbl_nome = QLabel(self.coluna_funcionario)
        self.lbl_nome.setObjectName(u"lbl_nome")

        self.verticalLayout_2.addWidget(self.lbl_nome)

        self.txt_nome = QLineEdit(self.coluna_funcionario)
        self.txt_nome.setObjectName(u"txt_nome")

        self.verticalLayout_2.addWidget(self.txt_nome)

        self.lbl_cpf = QLabel(self.coluna_funcionario)
        self.lbl_cpf.setObjectName(u"lbl_cpf")

        self.verticalLayout_2.addWidget(self.lbl_cpf)

        self.txt_cpf = QLineEdit(self.coluna_funcionario)
        self.txt_cpf.setObjectName(u"txt_cpf")

        self.verticalLayout_2.addWidget(self.txt_cpf)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_editar_funcionario = QPushButton(self.coluna_funcionario)
        self.btn_editar_funcionario.setObjectName(u"btn_editar_funcionario")

        self.horizontalLayout_3.addWidget(self.btn_editar_funcionario)

        self.btn_remover_funcionario = QPushButton(self.coluna_funcionario)
        self.btn_remover_funcionario.setObjectName(u"btn_remover_funcionario")

        self.horizontalLayout_3.addWidget(self.btn_remover_funcionario)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.btn_adicionar_funcionario = QPushButton(self.coluna_funcionario)
        self.btn_adicionar_funcionario.setObjectName(u"btn_adicionar_funcionario")

        self.verticalLayout_2.addWidget(self.btn_adicionar_funcionario)

        self.tb_funcionario = QTableWidget(self.coluna_funcionario)
        if (self.tb_funcionario.columnCount() < 2):
            self.tb_funcionario.setColumnCount(2)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_funcionario.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_funcionario.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        self.tb_funcionario.setObjectName(u"tb_funcionario")
        self.tb_funcionario.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.tb_funcionario)


        self.horizontalLayout_2.addWidget(self.coluna_funcionario)

        self.coluna_uniforme = QWidget(self.tab_configuracoes)
        self.coluna_uniforme.setObjectName(u"coluna_uniforme")
        self.verticalLayout_3 = QVBoxLayout(self.coluna_uniforme)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.coluna_uniforme)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.lbl_nome_uniforme = QLabel(self.coluna_uniforme)
        self.lbl_nome_uniforme.setObjectName(u"lbl_nome_uniforme")

        self.verticalLayout_3.addWidget(self.lbl_nome_uniforme)

        self.txt_nome_uniforme = QLineEdit(self.coluna_uniforme)
        self.txt_nome_uniforme.setObjectName(u"txt_nome_uniforme")

        self.verticalLayout_3.addWidget(self.txt_nome_uniforme)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_editar_uniforme = QPushButton(self.coluna_uniforme)
        self.btn_editar_uniforme.setObjectName(u"btn_editar_uniforme")

        self.horizontalLayout_4.addWidget(self.btn_editar_uniforme)

        self.btn_remover_uniforme = QPushButton(self.coluna_uniforme)
        self.btn_remover_uniforme.setObjectName(u"btn_remover_uniforme")

        self.horizontalLayout_4.addWidget(self.btn_remover_uniforme)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.btn_adicionar_uniforme = QPushButton(self.coluna_uniforme)
        self.btn_adicionar_uniforme.setObjectName(u"btn_adicionar_uniforme")

        self.verticalLayout_3.addWidget(self.btn_adicionar_uniforme)

        self.tb_uniformes = QTableWidget(self.coluna_uniforme)
        if (self.tb_uniformes.columnCount() < 1):
            self.tb_uniformes.setColumnCount(1)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_uniformes.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        self.tb_uniformes.setObjectName(u"tb_uniformes")
        self.tb_uniformes.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.tb_uniformes)


        self.horizontalLayout_2.addWidget(self.coluna_uniforme)

        self.tab_principal.addTab(self.tab_configuracoes, "")

        self.verticalLayout.addWidget(self.tab_principal)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tab_principal.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Controle de uniformes", None))
#if QT_CONFIG(tooltip)
        self.tab_principal.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Emprestar ou receber uniforme</span></p></body></html>", None))
        self.btn_receber.setText(QCoreApplication.translate("MainWindow", u"Receber", None))
        self.btn_emprestar.setText(QCoreApplication.translate("MainWindow", u"Emprestar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Empr\u00e9stimos ativos</span></p></body></html>", None))
        ___qtablewidgetitem = self.tb_emprestimos_ativos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Funcion\u00e1rio", None));
        ___qtablewidgetitem1 = self.tb_emprestimos_ativos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Data do empr\u00e9stimo", None));
        ___qtablewidgetitem2 = self.tb_emprestimos_ativos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Uniforme", None));
        self.tab_principal.setTabText(self.tab_principal.indexOf(self.tab_inicio), QCoreApplication.translate("MainWindow", u"In\u00edcio", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Relat\u00f3rio por per\u00edodo</span></p></body></html>", None))
        self.lbl_data_inicial.setText(QCoreApplication.translate("MainWindow", u"Data inicial", None))
        self.lbl_data_final.setText(QCoreApplication.translate("MainWindow", u"Data Final", None))
        self.btn_consultar_periodo.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        ___qtablewidgetitem3 = self.tb_relatorio.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Funcion\u00e1rio", None));
        ___qtablewidgetitem4 = self.tb_relatorio.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Data do empr\u00e9stimo", None));
        ___qtablewidgetitem5 = self.tb_relatorio.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Data da devolu\u00e7\u00e3o", None));
        ___qtablewidgetitem6 = self.tb_relatorio.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Uniforme emprestado", None));
        self.tab_principal.setTabText(self.tab_principal.indexOf(self.tab_relatorio), QCoreApplication.translate("MainWindow", u"Relat\u00f3rio", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Funcion\u00e1rios</span></p></body></html>", None))
        self.lbl_nome.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.lbl_cpf.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.btn_editar_funcionario.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_remover_funcionario.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        self.btn_adicionar_funcionario.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        ___qtablewidgetitem7 = self.tb_funcionario.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem8 = self.tb_funcionario.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Uniformes</span></p></body></html>", None))
        self.lbl_nome_uniforme.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.btn_editar_uniforme.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_remover_uniforme.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        self.btn_adicionar_uniforme.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        ___qtablewidgetitem9 = self.tb_uniformes.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        self.tab_principal.setTabText(self.tab_principal.indexOf(self.tab_configuracoes), QCoreApplication.translate("MainWindow", u"Gest\u00e3o", None))
    # retranslateUi

