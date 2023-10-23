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
        uniforme.ativo = True
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

    def update_uniforme(self, main_window):
        if main_window.btn_editar_uniforme.text() == 'Editar':
            selected_rows = main_window.tb_uniformes.selectionModel().selectedRows()
            if not selected_rows:
                return
            selected_row = selected_rows[0].row()
            main_window.txt_nome_uniforme.setText(main_window.tb_uniformes.item(selected_row, 0).text())
            main_window.btn_editar_uniforme.setText('Atualizar')
            self.uniforme_updated = self.uniforme_repository.select_uniforme_by_name(main_window.tb_uniformes.item(selected_row, 0).text())
        else:
            self.uniforme_updated.nome = main_window.txt_nome_uniforme.text()
            try:
                self.uniforme_repository.update_uniforme(self.uniforme_updated)
                QMessageBox.information(main_window, "Cadastro de uniformes", "Uniforme atualizado com sucesso!")
                main_window.btn_editar_uniforme.setText('Editar')
                main_window.txt_nome_uniforme.clear()
                main_window.txt_cpf.clear()
                self.main_window_service.populate_table_uniforme(main_window)
            except Exception as e:
                QMessageBox.warning(main_window, "Atenção", f'Problema ao atualizar uniorme.\n')