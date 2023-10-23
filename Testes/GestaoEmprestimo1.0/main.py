import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtGui import QPalette, QColor, Qt

from services.emprestimo_service import EmprestimoService
from services.uniforme_service import UniformeService
from view.emprestimo_ui import Ui_Dialog
from view.main_ui import Ui_MainWindow
from services.mainwindow_service import MainWindowService
from services.funcionario_service import FuncionarioService


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.emprestimo_dialog = None
        self.setupUi(self)
        self.uniforme_updated = None

        self.service_main_window = MainWindowService()
        self.service_funcionario = FuncionarioService()
        self.service_uniforme = UniformeService()
        self.service_emprestimo = EmprestimoService()
        self.service_main_window.populate_table_emprestimos_ativos(self)
        self.service_main_window.populate_table_funcionario(self)
        self.service_main_window.populate_table_uniforme(self)

        self.btn_emprestar.clicked.connect(self.adicionar_emprestimo)
        self.btn_adicionar_funcionario.clicked.connect(self.adicionar_funcionario)
        self.btn_editar_funcionario.clicked.connect(self.atualizar_funcionario)
        self.btn_remover_funcionario.clicked.connect(self.remover_funcionario)
        self.btn_adicionar_uniforme.clicked.connect(self.adicionar_uniforme)
        self.btn_receber.clicked.connect(self.finalizar_emprestimo)
        self.btn_editar_uniforme.clicked.connect(self.atualizar_uniforme)

    def adicionar_funcionario(self):
        self.service_funcionario.insert_funcionario(self)

    def atualizar_funcionario(self):
        self.service_funcionario.update_funcionario(self)

    def remover_funcionario(self):
        self.service_funcionario.delete_funcionario(self)

    def adicionar_uniforme(self):
        self.service_uniforme.insert_uniforme(self)

    def atualizar_uniforme(self):
        self.service_uniforme.update_uniforme(self)

    def finalizar_emprestimo(self):
        self.service_emprestimo.finalize_emprestimo(self)

    def adicionar_emprestimo(self):
        self.emprestimo_dialog = EmprestimoDialog(self)
        self.emprestimo_dialog.show()
        # O uso do lambda garante que, quando o sinal finished for emitido, a função populate_table_emprestimos_ativos
        # seja chamada com self (o objeto MainWindow) como argumento.
        self.emprestimo_dialog.finished.connect(
            lambda: self.service_main_window.populate_table_emprestimos_ativos(self))


# Classe para instanciar o QDialog de empréstimo
class EmprestimoDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(EmprestimoDialog, self).__init__(parent)
        self.setupUi(self)
        self.uiforme_service = UniformeService()
        self.service_funcionario = FuncionarioService()
        self.service_emprestimo = EmprestimoService()

        self.selected_funcionario = None
        self.uniformes = []

        self.populate_uniformes()
        self.btn_consulta_funcionario.clicked.connect(self.get_funcionario)
        self.btn_emprestar.clicked.connect(self.set_emprestimo)

    def get_funcionario(self):
        self.service_funcionario.select_funcionario(self)

    def populate_uniformes(self):
        self.uiforme_service.populate_uniformes(self)

    def set_emprestimo(self):
        self.service_emprestimo.insert_emprestimo(self)


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
    # TODO ajustar a cor do texto selecionado para preto
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(0, 0, 0))
    app.setPalette(palette)
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
