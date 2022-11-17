from turtle import width
from typing import Container
from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication, QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem)
from ui_main import Ui_MainWindow
import sys
from database import Data_base
import pandas as pd
import sqlite3
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
import re




class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Conexão Esportiva - Sistema de cadastro de alunos")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)

        


        #########################################
        #TOGGLE BUTTON
        self.btn_toggle.clicked.connect(self.leftContainer)
        ###############################################

        ##############################################
        #Páginas do Sistema
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_cadastrar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastrar))
        self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))
        ###################################################################
        self.pushButton_5.clicked.connect(self.cadastrar_empresas)
        self.btn_alterar.clicked.connect(self.update_company)
        self.btn_excel.clicked.connect(self.gerar_excel_2)
        self.btn_excluir.clicked.connect(self.deletar_empresa)
        self.btn_atualizar.clicked.connect(self.atualizar_aluno)

        self.buscar_empresa()
    def leftContainer(self):

        width = self.left_container.width()

        if width == 9:
            newWidth = 200
        else:
            newWidth = 9
        
        self.animation = QtCore.QPropertyAnimation(self.left_container, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def cadastrar_empresas(self):
        db = Data_base()
        db.connect()

        fullDataSet = (

          self.txt_nome.text(), self.txt_matricula.text(), self.txt_datanasc.text(), self.txt_sexo.text(), self.txt_rg.text(), self.txt_cpf.text(), self.txt_alergia.text(), self.txt_celular.text(), self.txt_endereco.text(), self.txt_email.text(), self.txt_pai.text(), self.txt_cpfpai.text(), self.txt_nomemae.text(), self.txt_cpfmae.text(), self.txt_responsavel.text(), self.txt_cpfresponsavel.text(), self.txt_pagamento.text()

        )

        #Cadastrar no Banco de Dados
        resp = db.register_company(fullDataSet)

        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro Realizado")
            msg.setText("Cadastro Realizado com sucesso")
            msg.exec()
            db.close_connection()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("Erro ao cadastrar, verifique se as informações foram preenchidadas corretamente!")
            msg.exec()
            db.close_connection()
            return 

    def buscar_empresa(self):

        db = Data_base()
        db.connect()
        result = db.select_all_companiess()

        self.tb_company.clearContents()
        self.tb_company.setRowCount(len(result))
        

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tb_company.setItem(row, column, QTableWidgetItem(str(data)))
        
        db.close_connection()

        self.tb_company.reset()


    def update_company(self):

        dados = []
        update_dados = []

        for row in range(self.tb_company.rowCount()):
            for column in range(self.tb_company.columnCount()):
                dados.append(self.tb_company.item(row, column).text())
            update_dados.append(dados)
            dados = []

        #ATUALIZAR DADOS NO BANCO
        db = Data_base()
        db.connect() 

        for emp in update_dados:
            db.update_company(tuple(emp))

        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de Dados")
        msg.setText("Dados atualizados com sucesso!")
        msg.exec()

        self.tb_company.reset()
        self.buscar_empresa()

    def gerar_excel(self):

        dados = []
        all_dados = []

        for row in range(self.tb_company.rowCount()):
            for column in range(self.tb_company.columnCount()):
                dados.append(self.tb_company.item(row, column).text())

            all_dados.append(dados)
            dados = []

        columns = ['NOME','DATANASC','SEXO','RGALUNO','CPFALUNO','ALERGIA','CELULAR','ENDERECO','EMAIL','NOMEPAI','CPFPAI','NOMEMAE','CPFMAE','MATRICULA','NOMERESPONSAVEL','CPFRESPONSAVEL','PAGAMENTO']

        empresas = pd.DataFrame(all_dados, columns= columns)
        empresas.to_excel("Alunos.xlsx", sheet_name='alunos', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Relatório Excel gerado com sucesso!")
        msg.exec()

    def gerar_excel_2(self):

        cnx = sqlite3.connect("system.db")

        alunos = pd.read_sql_query("""SELECT * FROM Alunos""", cnx)

        alunos.to_excel("Alunos.xlsx", sheet_name='alunos', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Relatório Excel gerado com sucesso!")
        msg.exec()


    def deletar_empresa(self):

        db = Data_base()
        db.connect()

        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluído.")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            nome = self.tb_company.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = db.delete_comapanie(nome)
            self.buscar_empresa()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Alunos")
            msg.setText(result)
            msg.exec()




        db.close_connection()

    def atualizar_aluno(self):
        db = Data_base()
        db.connect()

        db.close_connection

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de Dados")
        msg.setText("Dados atualizados com sucesso!")
        msg.exec()

        self.tb_company.reset()
        self.buscar_empresa()


if __name__ == "__main__":

    db = Data_base()
    db.connect()
    db.create_table_company()
    db.close_connection()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()