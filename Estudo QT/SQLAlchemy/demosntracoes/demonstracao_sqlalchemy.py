from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer



Base = declarative_base()
database_url = 'mysql+pymysql://admin:admin@localhost:3306/locadora'
class Filme(Base):
    __tablename__ = 'filme'

    id = Column(Integer, autoincrement=True, primary_key=True)
    titulo = Column(String(100), nullable=False)
    genero = Column(String(100), nullable=False)
    ano = Column(Integer, nullable=False)

    # Esta função demonstra o objeto de uma forma mais legível
    def __repr__(self):
        return f'Filme [titulo={self.titulo}, ano={self.ano}]'

def create_database():
    engine = create_engine(database_url, echo=True)
    try:
        engine.connect()
    except Exception as e:
        if '1049' in str(e):
            engine = create_engine(database_url.rsplit('/', 1)[0], echo=True)
            conn = engine.connect()
            conn.execute("CREATE DATABASE locadora")
            conn.close()
            print("Database criado com sucesso!")
        else:
            raise e

create_database()


#Configurações
# Cria uma instância do objeto Engine
# O objeto Engine é responsável por se comunicar com o banco de dados
engine = create_engine(database_url)

# Cria uma conexão com o banco de dados usando o objeto Engine
# O objeto Connection é uma interface para executar comandos SQL no banco de dados
conn = engine.connect()

# Cria uma instância da classe sessionmaker
# A classe sessionmaker é usada para criar objetos Session, que representam uma transação com o banco de dados
Session = sessionmaker(bind=engine)

# Cria uma sessão do banco de dados usando a instância da classe sessionmaker
# O objeto Session é usado para executar comandos SQL no banco de dados e manipular objetos Python que representam
# tabelas no banco de dados
session = Session()


#Criação da tabela
def create_table():
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
    print("Tabela criada com sucesso!")

create_table()

#Inserção no banco
data_insert = Filme(titulo='Jokera', ano='2018', genero='Ação')
session.add(data_insert)
session.commit()

#Remoção do banco
session.query(Filme).filter(Filme.titulo == 'Joker').delete()
session.commit()

#Atualização
#A função update precisa de parametros sendo passados como um dicionário
session.query(Filme).filter(Filme.titulo == 'Jokera').update({'titulo' : 'Joker'})

#Consutla
data = session.query(Filme).all()
print(data)

session.close()
