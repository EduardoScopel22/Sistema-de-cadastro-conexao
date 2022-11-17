# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'conexaoesportiva.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1281, 505)
        MainWindow.setMaximumSize(QSize(16777215, 16666666))
        MainWindow.setStyleSheet(u"background-color: rgb(16, 33, 103);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"\n"
" border:none;\n"
"\n"
"}\n"
"QLabel{\n"
" color: rgb(255, 255, 255);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.left_container = QFrame(self.centralwidget)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMaximumSize(QSize(9, 16777215))
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(11, -1, 0, -1)
        self.frame = QFrame(self.left_container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
" background-color: #EB1C24;\n"
"}\n"
"\n"
"QToolBox{\n"
" text-align: left;\n"
" background-color: rgb(228, 254, 255);\n"
"}\n"
"\n"
"QToolBox::tab{\n"
" border-radius: 5px;\n"
"\n"
" background-color: rgb(194, 232, 255);\n"
" text-align: left;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QPushButton:hover{\n"
" background-color: #EB1C24;\n"
"border-top-left-radius: 15px;\n"
"}\n"
"\n"
"QPushButton{\n"
" color: rgb(255, 255, 255);\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 74, 334))
        self.page.setCursor(QCursor(Qt.PointingHandCursor))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(11)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_cadastrar = QPushButton(self.page)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_cadastrar)

        self.btn_sobre = QPushButton(self.page)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 30))
        self.btn_sobre.setFont(font)
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 176, 226))
        self.verticalLayout_13 = QVBoxLayout(self.page_2)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, -1, 0, -1)
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_13.addWidget(self.label_4)

        self.toolBox.addItem(self.page_2, u"Page 2")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left_container)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 11, 11)
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_toggle = QPushButton(self.top_frame)
        self.btn_toggle.setObjectName(u"btn_toggle")
        self.btn_toggle.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/menu2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_toggle, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.main_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setMaximumSize(QSize(16777215, 16666666))
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_6 = QVBoxLayout(self.pg_home)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.logo = QLabel(self.pg_home)
        self.logo.setObjectName(u"logo")

        self.verticalLayout_6.addWidget(self.logo)

        self.Pages.addWidget(self.pg_home)
        self.pg_cadastrar = QWidget()
        self.pg_cadastrar.setObjectName(u"pg_cadastrar")
        self.verticalLayout_7 = QVBoxLayout(self.pg_cadastrar)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tabWidget = QTabWidget(self.pg_cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_10 = QVBoxLayout(self.tab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QLineEdit{\n"
" Background-color: rgb(255, 255, 255);\n"
" font: 10pt \"MS Shel Dig 2\";\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"\n"
" background-color: rgb(231, 231, 231);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_cadastro = QLabel(self.frame_4)
        self.lbl_cadastro.setObjectName(u"lbl_cadastro")
        self.lbl_cadastro.setMaximumSize(QSize(16777215, 150))
        self.lbl_cadastro.setStyleSheet(u"color: rgb(0, 99, 148);\n"
"background-color: rgb(249, 249, 249);")

        self.gridLayout.addWidget(self.lbl_cadastro, 0, 0, 1, 5)

        self.txt_datanasc = QLineEdit(self.frame_4)
        self.txt_datanasc.setObjectName(u"txt_datanasc")

        self.gridLayout.addWidget(self.txt_datanasc, 1, 1, 1, 2)

        self.txt_cpf = QLineEdit(self.frame_4)
        self.txt_cpf.setObjectName(u"txt_cpf")

        self.gridLayout.addWidget(self.txt_cpf, 2, 1, 1, 2)

        self.txt_celular = QLineEdit(self.frame_4)
        self.txt_celular.setObjectName(u"txt_celular")

        self.gridLayout.addWidget(self.txt_celular, 3, 0, 1, 1)

        self.txt_nome = QLineEdit(self.frame_4)
        self.txt_nome.setObjectName(u"txt_nome")

        self.gridLayout.addWidget(self.txt_nome, 1, 0, 1, 1)

        self.txt_sexo = QLineEdit(self.frame_4)
        self.txt_sexo.setObjectName(u"txt_sexo")

        self.gridLayout.addWidget(self.txt_sexo, 1, 4, 1, 1)

        self.txt_rg = QLineEdit(self.frame_4)
        self.txt_rg.setObjectName(u"txt_rg")

        self.gridLayout.addWidget(self.txt_rg, 2, 0, 1, 1)

        self.txt_pagamento = QLineEdit(self.frame_4)
        self.txt_pagamento.setObjectName(u"txt_pagamento")

        self.gridLayout.addWidget(self.txt_pagamento, 6, 4, 1, 1)

        self.txt_alergia = QLineEdit(self.frame_4)
        self.txt_alergia.setObjectName(u"txt_alergia")

        self.gridLayout.addWidget(self.txt_alergia, 2, 4, 1, 1)

        self.txt_email = QLineEdit(self.frame_4)
        self.txt_email.setObjectName(u"txt_email")

        self.gridLayout.addWidget(self.txt_email, 3, 4, 1, 2)

        self.txt_pai = QLineEdit(self.frame_4)
        self.txt_pai.setObjectName(u"txt_pai")

        self.gridLayout.addWidget(self.txt_pai, 4, 0, 1, 1)

        self.txt_nomemae = QLineEdit(self.frame_4)
        self.txt_nomemae.setObjectName(u"txt_nomemae")

        self.gridLayout.addWidget(self.txt_nomemae, 5, 0, 1, 1)

        self.txt_responsavel = QLineEdit(self.frame_4)
        self.txt_responsavel.setObjectName(u"txt_responsavel")

        self.gridLayout.addWidget(self.txt_responsavel, 6, 0, 1, 1)

        self.txt_matricula = QLineEdit(self.frame_4)
        self.txt_matricula.setObjectName(u"txt_matricula")

        self.gridLayout.addWidget(self.txt_matricula, 5, 4, 1, 1)

        self.txt_endereco = QLineEdit(self.frame_4)
        self.txt_endereco.setObjectName(u"txt_endereco")

        self.gridLayout.addWidget(self.txt_endereco, 3, 1, 1, 2)

        self.txt_cpfpai = QLineEdit(self.frame_4)
        self.txt_cpfpai.setObjectName(u"txt_cpfpai")

        self.gridLayout.addWidget(self.txt_cpfpai, 4, 1, 1, 2)

        self.txt_cpfmae = QLineEdit(self.frame_4)
        self.txt_cpfmae.setObjectName(u"txt_cpfmae")

        self.gridLayout.addWidget(self.txt_cpfmae, 5, 1, 1, 2)

        self.txt_cpfresponsavel = QLineEdit(self.frame_4)
        self.txt_cpfresponsavel.setObjectName(u"txt_cpfresponsavel")

        self.gridLayout.addWidget(self.txt_cpfresponsavel, 6, 2, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_4)

        self.pushButton_5 = QPushButton(self.tab)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(161, 30))
        font1 = QFont()
        font1.setPointSize(12)
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"QPushButton:hover{\n"
" background-color:rgb(0,170,255);\n"
" border-radius:15px;\n"
" color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
" border-radius: 15px;\n"
" background-color: rgb(243, 243, 243);\n"
"}")

        self.verticalLayout_10.addWidget(self.pushButton_5, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_9 = QVBoxLayout(self.tab_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(16777215, 300))
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_9.addWidget(self.label_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tb_company = QTableWidget(self.tab_2)
        if (self.tb_company.columnCount() < 17):
            self.tb_company.setColumnCount(17)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        self.tb_company.setObjectName(u"tb_company")
        self.tb_company.setMinimumSize(QSize(0, 0))
        self.tb_company.setMaximumSize(QSize(16777215, 16777215))
        self.tb_company.setStyleSheet(u"QHeaderView::section{\n"
" background-color: rgb(148, 148, 148);\n"
" color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shel Dig 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
" background-color: rgb(252, 252, 252);\n"
"}")

        self.horizontalLayout_5.addWidget(self.tb_company)

        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setStyleSheet(u"QPushButton{\n"
" background-color: rgb(255, 255, 255);\n"
" color: rgb(0, 24, 74);\n"
"font: 11pt \"MS Shel Dig 2\";\n"
" border-radius:15px;\n"
"}\n"
"\n"
"QFrame{\n"
" background-color: rgb(230, 230, 230);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.btn_excel = QPushButton(self.frame_3)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(120, 30))
        self.btn_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel.setStyleSheet(u"QPushButton:hover{\n"
" background-color: rgb(255, 255, 255);\n"
" color: rgb(49, 147, 0);\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_excel)

        self.btn_alterar = QPushButton(self.frame_3)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(120, 30))
        self.btn_alterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar.setStyleSheet(u"QPushButton:hover{\n"
" background-color: rgb(255, 255, 255);\n"
" color: rgb(255, 170, 0);\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_3)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(120, 30))
        self.btn_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir.setStyleSheet(u"QPushButton:hover{\n"
" background-color: rgb(255, 255, 255);\n"
" color: rgb(199, 66, 0);\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_excluir)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.btn_atualizar = QPushButton(self.frame_3)
        self.btn_atualizar.setObjectName(u"btn_atualizar")
        self.btn_atualizar.setMinimumSize(QSize(120, 30))
        self.btn_atualizar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_atualizar.setStyleSheet(u"\n"
"QPushButton:hover{\n"
" background-color: rgb(255, 255, 255);\n"
" color: rgb(0, 34, 255);\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_atualizar)


        self.horizontalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_7.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_cadastrar)
        self.pg_contatos = QWidget()
        self.pg_contatos.setObjectName(u"pg_contatos")
        self.verticalLayout_12 = QVBoxLayout(self.pg_contatos)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")

        self.verticalLayout_12.addLayout(self.horizontalLayout_6)

        self.Pages.addWidget(self.pg_contatos)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_11 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_6 = QLabel(self.pg_sobre)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 200))

        self.verticalLayout_11.addWidget(self.label_6)

        self.label = QLabel(self.pg_sobre)
        self.label.setObjectName(u"label")

        self.verticalLayout_11.addWidget(self.label)

        self.Pages.addWidget(self.pg_sobre)

        self.verticalLayout_5.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Conexao Esportiva</span></p></body></html>", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Usu\u00e1rio</span>: Admin</p><p align=\"center\"><span style=\" font-weight:600;\">Sistema</span>: Conex\u00e3o Esportiva</p><p align=\"center\"><span style=\" font-weight:600;\">Status</span>: Ativo</p><p><br/></p><p><br/></p><p><br/></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.btn_toggle.setText("")
        self.logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/conexao esportiva.png\"/></p></body></html>", None))
        self.lbl_cadastro.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">CADASTRO</span></p></body></html>", None))
        self.txt_datanasc.setText("")
        self.txt_datanasc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Matricula:", None))
        self.txt_cpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"RG do Aluno", None))
        self.txt_celular.setText("")
        self.txt_celular.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Alergia:", None))
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.txt_sexo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nascimento:", None))
        self.txt_rg.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sexo:", None))
        self.txt_pagamento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pagamento:", None))
        self.txt_alergia.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF do Aluno:", None))
        self.txt_email.setText("")
        self.txt_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o:", None))
        self.txt_pai.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.txt_nomemae.setText("")
        self.txt_nomemae.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF do Pai:", None))
        self.txt_responsavel.setText("")
        self.txt_responsavel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do Respons\u00e1vel:", None))
        self.txt_matricula.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF da M\u00e3e:", None))
        self.txt_endereco.setText("")
        self.txt_endereco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Celular:", None))
        self.txt_cpfpai.setText("")
        self.txt_cpfpai.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do Pai:", None))
        self.txt_cpfmae.setText("")
        self.txt_cpfmae.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome da M\u00e3e:", None))
        self.txt_cpfresponsavel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF do Respons\u00e1vel:", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">ALUNOS</span></p></body></html>", None))
        ___qtablewidgetitem = self.tb_company.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem1 = self.tb_company.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Matricula", None));
        ___qtablewidgetitem2 = self.tb_company.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Data Nascimento", None));
        ___qtablewidgetitem3 = self.tb_company.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Sexo", None));
        ___qtablewidgetitem4 = self.tb_company.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"RG do Aluno", None));
        ___qtablewidgetitem5 = self.tb_company.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"CPF do Aluno", None));
        ___qtablewidgetitem6 = self.tb_company.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Alegia", None));
        ___qtablewidgetitem7 = self.tb_company.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Celular", None));
        ___qtablewidgetitem8 = self.tb_company.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None));
        ___qtablewidgetitem9 = self.tb_company.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem10 = self.tb_company.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Nome do Pai", None));
        ___qtablewidgetitem11 = self.tb_company.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"CPF do Pai", None));
        ___qtablewidgetitem12 = self.tb_company.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Nome da M\u00e3e", None));
        ___qtablewidgetitem13 = self.tb_company.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"CPF da M\u00e3e", None));
        ___qtablewidgetitem14 = self.tb_company.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Nome do Respons\u00e1vel", None));
        ___qtablewidgetitem15 = self.tb_company.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"CPF do Respons\u00e1vel", None));
        ___qtablewidgetitem16 = self.tb_company.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Pagamento", None));
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_atualizar.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Alunos", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">SOBRE</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Sistema para cadastro de alunos e armazenamento de informa\u00e7\u00f5es pessoais.</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Cetec 2022</span></p></body></html>", None))
    # retranslateUi

