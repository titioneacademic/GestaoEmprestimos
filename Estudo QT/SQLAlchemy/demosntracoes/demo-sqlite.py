# Importa as bibliotecas necessárias do SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

# Cria uma classe base para as definições das tabelas
Base = declarative_base()

# Define a URL do banco de dados como SQLite
database_url = 'sqlite:///locadora.db'  # URL do SQLite


# Define a classe Filme que representa a tabela 'filme' no banco de dados
class Filme(Base):
    __tablename__ = 'filme'

    # Define as colunas da tabela com seus tipos de dados
    id = Column(Integer, autoincrement=True, primary_key=True)
    titulo = Column(String(100), nullable=False)
    genero = Column(String(100), nullable=False)
    ano = Column(Integer, nullable=False)

    # Função de representação para exibir os objetos de filme de forma legível
    def __repr__(self):
        return f'Filme [titulo={self.titulo}, ano={self.ano}]'


# Função para criar a tabela no banco de dados SQLite
def create_table():
    # Cria uma instância da engine para se comunicar com o banco de dados SQLite
    engine = create_engine(database_url, echo=True)

    # Cria a tabela no banco de dados com base nas definições da classe Filme
    Base.metadata.create_all(engine)
    print("Tabela criada com sucesso!")


# Chama a função para criar a tabela
create_table()

# Cria uma instância da classe sessionmaker para gerenciar sessões com o banco de dados
engine = create_engine(database_url)
Session = sessionmaker(bind=engine)

# Cria uma sessão do banco de dados
session = Session()

# Inserção de dados na tabela
data_insert = Filme(titulo='Joker', ano=2018, genero='Ação')
session.add(data_insert)
session.commit()


# Atualização de dados na tabela
session.query(Filme).filter(Filme.titulo == 'Jokera').update({'titulo': 'Joker'})

# Consulta todos os dados da tabela
data = session.query(Filme).all()
print(data)

# Remoção de dados da tabela
session.query(Filme).filter(Filme.titulo == 'Joker').delete()
session.commit()

# Fecha a sessão
session.close()
