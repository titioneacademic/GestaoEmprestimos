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

class EmprestimoRepository:

    @staticmethod
    def insert_emprestimos(funcionario, uniforme):
        with DBConnectioHandler() as db:
            datetime_insert = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            emp = Emprestimo()
            emp.funcionario_id = funcionario.id
            emp.uniforme_id = uniforme.id
            emp.data_emprestimo = datetime.strptime(datetime_insert, '%d/%m/%Y %H:%M:%S')
            try:
                db.session.add(emp)
                db.session.commit()
            except Exception as e:
                print(e)

    @staticmethod
    def finalizes_emprestimo(funcionario, uniforme):
        with (DBConnectioHandler() as db):
            date = datetime.now()
            try:
                db.session.query(Emprestimo
                                 ).filter(Emprestimo.uniforme_id == uniforme.id,
                                          Emprestimo.funcionario_id == funcionario.id).update({'data_devolucao': date})
                db.session.commit()
            except Exception as e:
                print(e)

    @staticmethod
    def select_all_emprestimos():
        with DBConnectioHandler() as db:
            emprestimos = db.session.query(Emprestimo).options(joinedload(Emprestimo.funcionario)
                                                               , joinedload(Emprestimo.uniforme)).all()
            return emprestimos

    @staticmethod
    def select_emprestimos_in_period(start_date, end_date):
        with DBConnectioHandler() as db:
            emprestimos = (
                db.session.query(Emprestimo, Funcionario, Uniforme)
                .join(Funcionario, Funcionario.id == Emprestimo.funcionario_id)
                .join(Uniforme, Uniforme.id == Emprestimo.uniforme_id)
                .filter(
                    Emprestimo.data_emprestimo.between(start_date, end_date)
                )
                .options(
                    joinedload(Emprestimo.funcionario),  # Usa a relação aqui
                    joinedload(Emprestimo.uniforme)  # E aqui
                )
                .all()
            )
            return emprestimos

    @staticmethod
    def select_emprestimos_ativos():
        with DBConnectioHandler() as db:
            emprestimos = (db.session.query(Emprestimo, Funcionario, Uniforme)
                           .join(Funcionario, Funcionario.id == Emprestimo.funcionario_id)
                           .join(Uniforme, Uniforme.id == Emprestimo.uniforme_id)
                           .filter(Emprestimo.data_devolucao.is_(None))
                           .options(joinedload(Emprestimo.funcionario),
                                    joinedload(Emprestimo.uniforme))
                           .all())
            return emprestimos

    @staticmethod
    def delete_emprestimo(data):
        with DBConnectioHandler() as db:
            db.session.delete(data)
            db.session.commit()
