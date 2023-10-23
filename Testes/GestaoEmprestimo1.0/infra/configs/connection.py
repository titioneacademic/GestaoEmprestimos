from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from infra.configs.base import Base

#A classe DBConnectioHandler é definida para gerenciar as conexões e operações no banco de dados SQLite.
class DBConnectioHandler:

    def __init__(self):
        # Define a string de conexão SQLite
        self.__connection_string = 'sqlite:///emprestimo.db'
        self.__engine = self.__create_database_engine()
        # Chama o método para criar a tabela no SQLite
        self.create_table()
        self.session = None


    # Aqui é criado um método para que a engine possa ser aessada e comandos RAW (SQL Puro) possam ser criadas manualmente
    def get_engine(self):
        return self.__engine

    # Cria a engine do banco de dados
    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    # Criação da tabela no banco de dados SQLite
    def create_table(self):
        engine = create_engine(self.__connection_string, echo=True)
        Base.metadata.create_all(engine, checkfirst=True)
        print("Tabela criada com sucesso!")


    # Funções mágicas que definem abertura e fechamento
    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        print('Gerando conexão')
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechando conexão')
        self.session.close()
