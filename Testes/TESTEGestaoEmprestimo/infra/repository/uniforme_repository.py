from datetime import datetime
from sqlalchemy.orm import joinedload

from infra.configs.connection import DBConnectioHandler
from infra.entities.funcionario import Funcionario
from infra.entities.uniforme import Uniforme
from infra.entities.emprestimo import Emprestimo


# Os métodos  que vamos criar não precisam acessar ou modificar qualquer estado da instância específica de
# Repository sendo assim vamos adicionar os decorators de métodos estáticos

# Os métodos estáticos são métodos
# Sem acesso ao estado do objeto: Se o método não precisa acessar ou modificar o estado do objeto
# (representado pelos atributos do objeto), ele pode ser estático.

# Funcionalidade pertence à classe, não ao objeto: Em alguns casos, a funcionalidade faz mais sentido como algo
# que pertence à classe no total, em vez de a uma instância específica.

# Temos ganho de Desempenho: A invocação de um método estático pode ser ligeiramente mais rápida do que a invocação
# de um método de instância, porque não há necessidade de criar um vinculador para o objeto.

# Claridade e legibilidade: Usar um método estático pode comunicar intenções claras ao leitor de que esse método
# não depende ou modifica o estado da instância.

class UniformeRepository:

    @staticmethod
    def select_uniforme_by_id(id_uniforme):
        with (DBConnectioHandler() as db):
            uniforme = db.session.query(Uniforme).filter(Uniforme.id == id_uniforme).first()
            return uniforme

    @staticmethod
    def select_uniforme_by_name(name_uniforme):
        with DBConnectioHandler() as db:
            uniforme = db.session.query(Uniforme).filter(Uniforme.nome == name_uniforme).first()
            return uniforme

    @staticmethod
    def select_all_uniformes():
        with DBConnectioHandler() as db:
            data = db.session.query(Uniforme).all()
            return data

    @staticmethod
    def select_first_uniforme():
        with DBConnectioHandler() as db:
            data = db.session.query(Uniforme).first()
            return data

    @staticmethod
    def insert_many_uniformes(uniformes):
        with DBConnectioHandler() as db:
            db.session.add_all(uniformes)
            db.session.commit()

    @staticmethod
    def insert_one_uniforme(uniforme):
        with DBConnectioHandler() as db:
            db.session.add(uniforme)
            db.session.commit()

    @staticmethod
    def update_uniforme(uniforme):
        with DBConnectioHandler() as db:
            db.session.query(Uniforme).filter(Uniforme.id == uniforme.id).update({'nome': uniforme.nome})
            db.session.commit()

