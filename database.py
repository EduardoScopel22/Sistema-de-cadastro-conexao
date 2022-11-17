import sqlite3

class Data_base:

    def __init__(self, name = 'system.db') -> None:
        self.name = name

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    def create_table_company(Self):

        cursor = Self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Alunos(
            
            NOME TEXT,
            DATANASC TEXT,
            SEXO TEXT,
            RGALUNO TEXT,
            CPFALUNO TEXT,
            ALERGIA TEXT,
            CELULAR TEXT,
            ENDERECO TEXT,
            EMAIL TEXT,
            NOMEPAI TEXT,
            CPFPAI TEXT,
            NOMEMAE TEXT,
            CPFMAE TEXT,
            MATRICULA TEXT,
            NOMERESPONSAVEL TEXT,
            CPFRESPONSAVEL TEXT,
            PAGAMENTO TEXT,

            PRIMARY KEY(NOME)
            );

        



        
        
        """)

    def  register_company(self, fullDataSet):

        campos_tabela = ('NOME','MATRICULA','DATANASC','SEXO','RGALUNO','CPFALUNO','ALERGIA','CELULAR','ENDERECO','EMAIL','NOMEPAI','CPFPAI','NOMEMAE','CPFMAE','NOMERESPONSAVEL','CPFRESPONSAVEL','PAGAMENTO')

        qtnd = ("?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?")
        cursor = self.connection.cursor()

        try:
            cursor.execute(f"""INSERT INTO Alunos{campos_tabela}
            VALUES({qtnd})""", fullDataSet)
            self.connection.commit()
            return("OK")

        except:
                return "Erro"

    def select_all_companiess(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Alunos ORDER BY NOME")
            empresas = cursor.fetchall()
            return empresas
        except:
            pass

    def delete_comapanie(self, id):

        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Alunos WHERE NOME = '{id}' ")

            self.connection.commit()

            return "Cadastro de Aluno excluida com sucesso!"

        except:
            return "Erro ao Excluir registro!"

    def update_company(self, fullDataSet):

        cursor = self.connection.cursor()
        cursor.execute(f""" UPDATE Alunos set

            NOME = '{fullDataSet[0]}',
            DATANASC = '{fullDataSet[1]}',
            SEXO = '{fullDataSet[2]}',
            RGALUNO = '{fullDataSet[3]}',
            CPFALUNO = '{fullDataSet[4]}',
            ALERGIA = '{fullDataSet[5]}',
            CELULAR = '{fullDataSet[6]}',
            ENDERECO = '{fullDataSet[7]}',
            EMAIL = '{fullDataSet[8]}',
            NOMEPAI = '{fullDataSet[9]}',
            CPFPAI = '{fullDataSet[10]}',
            NOMEMAE = '{fullDataSet[11]}',
            CPFMAE = '{fullDataSet[12]}',
            MATRICULA = '{fullDataSet[13]}',
            NOMERESPONSAVEL = '{fullDataSet[14]}',
            CPFRESPONSAVEL = '{fullDataSet[15]}',
            PAGAMENTO = '{fullDataSet[16]}'
        
            WHERE NOME = '{fullDataSet[0]}'""")

        self.connection.commit()



    def atualizar_company(self):

        cursor2 = self.connection.cursor()
       

        self.connection.commit()


     