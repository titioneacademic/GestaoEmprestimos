from PySide6.QtWidgets import QMessageBox

from infra.entities.funcionario import Funcionario
from infra.repository.emprestimo_repository import EmprestimoRepository
from infra.repository.funcionario_repository import FuncionarioRepository
from infra.repository.uniforme_repository import UniformeRepository
from services.mainwindow_service import MainWindowService


class FuncionarioService:
    def __init__(self):

        self.service_main_window = MainWindowService()
        self.emprestimos_repository = EmprestimoRepository()
        self.uniforme_repository = UniformeRepository()
        self.funcionario_repository = FuncionarioRepository()
        self.main_window_service = MainWindowService()

    def insert_funcionario(self, main_window):
        funcionario = Funcionario()
        funcionario.nome = main_window.txt_nome.text()
        funcionario.cpf = main_window.txt_cpf.text()
        funcionario.ativo = True
        try:
            self.funcionario_repository.insert_one_funcionario(funcionario)
            main_window.txt_nome.setText('')
            main_window.txt_cpf.setText('')
            self.main_window_service.populate_table_funcionario(main_window)
            QMessageBox.information(main_window, "Cadastro de funcionário", "Funcionário cadastrado com sucesso!")
        except Exception as e:
            QMessageBox.warning(main_window, "Atenção", f'Problema ao cadastrar funcionário.\n')

    def select_funcionario(self, emprestimo_ui):
        if emprestimo_ui.btn_consulta_funcionario.text() == 'Limpar':
            emprestimo_ui.txt_nome_funcionario.clear()
            emprestimo_ui.txt_cpf_emprestimo.clear()
            emprestimo_ui.selected_funcionario = None
            emprestimo_ui.btn_consulta_funcionario.setText('Consultar')
        else:
            try:
                funcionario_emprestimo =  self.funcionario_repository.select_funcionario_by_cpf(emprestimo_ui.txt_cpf_emprestimo.text())
                if emprestimo_ui.txt_cpf_emprestimo.text() != '':
                    emprestimo_ui.txt_nome_funcionario.setText(funcionario_emprestimo.nome)
                    emprestimo_ui.selected_funcionario = funcionario_emprestimo
                    emprestimo_ui.txt_nome_funcionario.setReadOnly(True)
                    emprestimo_ui.btn_consulta_funcionario.setText('Limpar')
                else:
                    QMessageBox.warning(emprestimo_ui, "Atenção", "Digite um CPF para consulta!")
            except Exception as e:
                QMessageBox.warning(emprestimo_ui, "Atenção", "Funcionário não encontrado!")
                emprestimo_ui.txt_nome_funcionario.clear()

    def update_funcionario(self, main_window):
        if main_window.btn_editar_funcionario.text() == 'Editar':
            selected_rows = main_window.tb_funcionario.selectionModel().selectedRows()
            if not selected_rows:
                return
            selected_row = selected_rows[0].row()
            main_window.txt_nome.setText(main_window.tb_funcionario.item(selected_row, 0).text())
            main_window.txt_cpf.setText(main_window.tb_funcionario.item(selected_row, 1).text())
            main_window.txt_cpf.setReadOnly(True)
            main_window.btn_editar_funcionario.setText('Atualizar')
        else:
            cpf_funcionario = main_window.txt_cpf.text()
            funcionario_updated = self.funcionario_repository.select_funcionario_by_cpf(cpf_funcionario)
            funcionario_updated.nome = main_window.txt_nome.text()

            try:
                self.funcionario_repository.update_funcionario(funcionario_updated)
                QMessageBox.information(main_window, "Cadastro de funcionário", "Funcionário atualizado com sucesso!")
                main_window.btn_editar_funcionario.setText('Editar')
                main_window.txt_nome.clear()
                main_window.txt_cpf.clear()
                self.service_main_window.populate_table_funcionario(main_window)
            except Exception as e:
                QMessageBox.warning(main_window, "Atenção", f'Problema ao atualizar funcionário.\n')



    def delete_funcionario(self, main_window):
        selected_rows = main_window.tb_funcionario.selectionModel().selectedRows()
        if not selected_rows:
            return
        selected_row = selected_rows[0].row()
        funcionario_delete = self.funcionario_repository.select_funcionario_by_cpf(main_window.tb_funcionario.item(selected_row, 1).text())
        msg_box = QMessageBox(main_window)
        msg_box.setWindowTitle('Remover funcionário')
        msg_box.setText(f'Tem certeza de que deseja remover o funcionário {funcionario_delete.nome}?')
        msg_box.setIcon(QMessageBox.Question)
        yes_button = msg_box.addButton("Sim", QMessageBox.YesRole)
        no_button = msg_box.addButton("Cancelar", QMessageBox.NoRole)
        msg_box.exec()
        if msg_box.clickedButton() == yes_button:
            try:
                self.funcionario_repository.delete_funcionario(funcionario_delete)
                self.service_main_window.populate_table_funcionario(main_window)
            except Exception as e:
                QMessageBox.warning(main_window, "Atenção", f'Problema ao remover funcionário.\n'
                                                            f'Erro: {e}')
