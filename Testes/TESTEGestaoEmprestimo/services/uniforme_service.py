from PySide6.QtWidgets import QMessageBox

from infra.entities.funcionario import Funcionario
from infra.entities.uniforme import Uniforme
from infra.repository.emprestimo_repository import EmprestimoRepository
from infra.repository.funcionario_repository import FuncionarioRepository
from infra.repository.uniforme_repository import UniformeRepository
from services.mainwindow_service import MainWindowService


class UniformeService:
    def __init__(self):

        self.emprestimos_repository = EmprestimoRepository()
        self.uniforme_repository = UniformeRepository()
        self.funcionario_repository = FuncionarioRepository()
        self.main_window_service = MainWindowService()


    def insert_uniforme(self, main_window):
        uniforme = Uniforme()
        uniforme.nome = main_window.txt_nome_uniforme.text()
        try:
            self.uniforme_repository.insert_one_uniforme(uniforme)
            main_window.txt_nome_uniforme.setText('')
            self.main_window_service.populate_table_uniforme(main_window)
            QMessageBox.information(main_window, "Cadastro de uniforme", "Uniforme cadastrado com sucesso!")
        except Exception as e:
            QMessageBox.warning(main_window, "Atenção", f'Problema ao cadastrar uniforme.\n')

    def populate_uniformes(self, emprestimo_ui):
        emprestimo_ui.cb_uniforme.clear()
        emprestimo_ui.cb_uniforme.addItem('Selecione um item')
        emprestimo_ui.uniformes = self.uniforme_repository.select_all_uniformes()
        for uniforme in emprestimo_ui.uniformes:
            # Supondo que o Uniforme tenha um atributo 'nome' que você quer mostrar no QComboBox
            emprestimo_ui.cb_uniforme.addItem(uniforme.nome)