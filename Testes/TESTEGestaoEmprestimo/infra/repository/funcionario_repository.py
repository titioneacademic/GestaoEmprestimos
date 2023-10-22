from infra.configs.connection import DBConnectioHandler
from infra.entities.funcionario import Funcionario


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

class FuncionarioRepository:

    @staticmethod
    def select_funcionario_by_id(id_funcionario):
        with (DBConnectioHandler() as db):
            funcionario = db.session.query(Funcionario).filter(Funcionario.id == id_funcionario).first()
            return funcionario

    @staticmethod
    def select_funcionario_by_cpf(cpf_funcionario):
        with DBConnectioHandler() as db:
            funcionario = db.session.query(Funcionario).filter(Funcionario.cpf == cpf_funcionario).first()
            return funcionario

    @staticmethod
    def select_funcionario_by_uniforme_id(id_uniforme):
        with DBConnectioHandler() as db:
            funcionarios = db.session.query(Funcionario).filter(Funcionario.uniforme_id == id_uniforme).all()
            return funcionarios

    @staticmethod
    def select_all_funcionarios():
        with DBConnectioHandler() as db:
            data = db.session.query(Funcionario).all()
            return data

    @staticmethod
    def select_first_funcionario():
        with DBConnectioHandler() as db:
            data = db.session.query(Funcionario).first()
            return data

    @staticmethod
    def insert_many_funcionarios(funcionarios):
        with DBConnectioHandler() as db:
            db.session.add_all(funcionarios)
            db.session.commit()

    @staticmethod
    def insert_one_funcionario(funcionario):
        with DBConnectioHandler() as db:
            db.session.add(funcionario)
            db.session.commit()

    @staticmethod
    def update_funcionario(funcionario):
        with DBConnectioHandler() as db:
            db.session.query(Funcionario).filter(Funcionario.id == funcionario.id).update({'nome': funcionario.nome,
                                                                                           'cpf': funcionario.cpf})
            db.session.commit()

    @staticmethod
    def delete_funcionario(data):
        with DBConnectioHandler() as db:
            db.session.delete(data)
            db.session.commit()
