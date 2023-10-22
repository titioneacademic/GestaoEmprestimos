import datetime
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtGui import QPalette, QColor, Qt

from infra.entities.funcionario import Funcionario
from infra.entities.uniforme import Uniforme
from view.emprestimo_ui import Ui_Dialog
from view.main_ui import Ui_MainWindow
from infra.repository.funcionario_repository import Repository
from infra.configs.connection import DBConnectioHandler


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Criação e estruturação da base
        repo = Repository()
        data_base = DBConnectioHandler()

        self.btn_emprestar.clicked.connect(self.adicionar_emprestimo)
        emp = repo.select_all_emprestimos()
        print(emp)

        func = Funcionario()
        func.nome = 'Titione'
        func.cpf = '00862508924'
        unif = Uniforme()
        unif.nome = 'Pista'

        # repo.insert_one_funcionario(func)
        # repo.insert_one_uniforme(unif)
        fs = repo.select_all_funcionarios()
        us = repo.select_all_uniformes()
        f = fs[0]
        u = us[0]
        repo.insert_emprestimos(f, u)
        date_1 = datetime.datetime.today()
        date_2 = datetime.datetime.now() - datetime.timedelta(days=2)

        #Consulta de relatorios de emprestimos
        emprestimos = repo.select_emprestimos_in_period(date_2, date_1)
        # print(f'\nRelatório baseado na data inicio = {date_2} e data fim {date_1}')
        # for emprestimo, funcionario, uniforme in emprestimos:
        #     print("ID do Empréstimo:", emprestimo.funcionario_id)  # ou qualquer outro atributo de Emprestimo
        #     print("Nome do Funcionário:", funcionario.nome)  # ou qualquer outro atributo de Funcionario
        #     print("CPF do Funcionário:", funcionario.cpf)  # ou qualquer outro atributo de Funcionario
        #     print("Nome do Uniforme:", uniforme.nome)  # ou qualquer outro atributo de Uniforme
        #     print("------------------------")
        #
        #
        # #Consulta de emprestimos ativos
        # emprestimos_ativos = repo.select_emprestimos_ativos()
        # print('\nEmpréstimos ativos')
        # for emprestimo, funcionario, uniforme in emprestimos_ativos:
        #     print("ID do Empréstimo:", emprestimo.funcionario_id)  # ou qualquer outro atributo de Emprestimo
        #     print("Nome do Funcionário:", funcionario.nome)  # ou qualquer outro atributo de Funcionario
        #     print("CPF do Funcionário:", funcionario.cpf)  # ou qualquer outro atributo de Funcionario
        #     print("Nome do Uniforme:", uniforme.nome)  # ou qualquer outro atributo de Uniforme
        #     print("------------------------")

        #repo.finalizes_emprestimo(f, u)
        # Se você quiser adicionar lógica adicional ou conexões de sinal/slot, faça-o aqui.

    # Função para instanciar a janela de adição de empréstimo
    def adicionar_emprestimo(self):
        self.emprestimo_dialog = EmprestimoDialog(self)
        self.emprestimo_dialog.show()


# Classe para instanciar o QDialog de empréstimo
class EmprestimoDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(EmprestimoDialog, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Definição de tema escuro
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Base, QColor(42, 42, 42))
    palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Dark, QColor(35, 35, 35))
    palette.setColor(QPalette.ColorRole.Shadow, QColor(20, 20, 20))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.black)
    palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
    palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(127, 127, 127))
    app.setPalette(palette)
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
