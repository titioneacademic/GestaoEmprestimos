from PySide6.QtWidgets import QMessageBox

from infra.repository.emprestimo_repository import EmprestimoRepository
from infra.repository.funcionario_repository import FuncionarioRepository
from infra.repository.uniforme_repository import UniformeRepository
from services.mainwindow_service import MainWindowService


class EmprestimoService:
    def __init__(self):
        self.service_main_window = MainWindowService()
        self.emprestimo_repository = EmprestimoRepository()
        self.uniforme_repository = UniformeRepository()
        self.funcionario_repository = FuncionarioRepository()
        
    
    def adicionar_emprestimo(self, emprestimo_dialog):
        self.emprestimo_dialog.show()
        #O uso do lambda garante que, quando o sinal finished for emitido, a função populate_table_emprestimos_ativos seja chamada com self (o objeto MainWindow) como argumento.
        self.emprestimo_dialog.finished.connect(lambda: self.service.populate_table_emprestimos_ativos(self))

    def finalize_emprestimo(self):
        emprestimo_repository = EmprestimoRepository()
        funcionario_repository = FuncionarioRepository()
        uniforme_repository = UniformeRepository()
        selected_rows = self.tb_emprestimos_ativos.selectionModel().selectedRows()
        if not selected_rows:
            return
        selected_row = selected_rows[0].row()
        cpf_funcionario = self.tb_emprestimos_ativos.item(selected_row, 1).text()
        uniforme_selecionado = self.tb_emprestimos_ativos.item(selected_row, 3).text()
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle('Finalizar Empréstimo')
        msg_box.setText('Tem certeza de que deseja finalizar este empréstimo?')
        msg_box.setIcon(QMessageBox.Question)
        yes_button = msg_box.addButton("Claro", QMessageBox.YesRole)
        no_button = msg_box.addButton("Ainda não", QMessageBox.NoRole)
        msg_box.exec()
        if msg_box.clickedButton() == yes_button:
            funcionario_recebido = funcionario_repository.select_funcionario_by_cpf(cpf_funcionario)
            uniforme_recebido = uniforme_repository.select_uniforme_by_name(uniforme_selecionado)
            try:
                emprestimo_repository.finalizes_emprestimo(funcionario_recebido, uniforme_recebido)
                QMessageBox.information(self, "Empréstimos", "Emprésitmo finalizado com sucesso!")
                self.service.populate_table_emprestimos_ativos(self)
            except Exception as e:
                QMessageBox.warning(self, "Atenção", f'Problema ao realizar recebimento.\n'
                                                     f'Erro: {e}')


    def insert_emprestimo(self, emprestimo_ui):
        if emprestimo_ui.cb_uniforme.currentText() != 'Selecione um item' and emprestimo_ui.selected_funcionario is not None:
            uniforme = self.uniforme_repository.select_uniforme_by_name(emprestimo_ui.cb_uniforme.currentText())
            try:
                self.emprestimo_repository.insert_emprestimos(emprestimo_ui.selected_funcionario, uniforme)
                QMessageBox.information(emprestimo_ui, "Empréstimos", "Emprésitmo cadastrado com sucesso!")
            except Exception as e:
                QMessageBox.warning(emprestimo_ui, "Atenção", "Erro ao cadastrar empréstimo!")
        else:
            if emprestimo_ui.cb_uniforme.currentText() == 'Selecione um item':
                QMessageBox.warning(emprestimo_ui, "Atenção", "Selecione um uniforme!")
            else:
                QMessageBox.warning(emprestimo_ui, "Atenção", "Nenhum funcionário informado!")


    def finalize_emprestimo(self, main_window):
        selected_rows = main_window.tb_emprestimos_ativos.selectionModel().selectedRows()
        if not selected_rows:
            return
        selected_row = selected_rows[0].row()
        cpf_funcionario = main_window.tb_emprestimos_ativos.item(selected_row, 1).text()
        uniforme_selecionado = main_window.tb_emprestimos_ativos.item(selected_row, 3).text()
        msg_box = QMessageBox(main_window)
        msg_box.setWindowTitle('Finalizar Empréstimo')
        msg_box.setText('Tem certeza de que deseja finalizar este empréstimo?')
        msg_box.setIcon(QMessageBox.Question)
        yes_button = msg_box.addButton("Sim", QMessageBox.YesRole)
        no_button = msg_box.addButton("Não", QMessageBox.NoRole)
        msg_box.exec()
        if msg_box.clickedButton() == yes_button:
            funcionario_recebido = self.funcionario_repository.select_funcionario_by_cpf(cpf_funcionario)
            uniforme_recebido = self.uniforme_repository.select_uniforme_by_name(uniforme_selecionado)
            try:
                self.emprestimo_repository.finalizes_emprestimo(funcionario_recebido, uniforme_recebido)
                QMessageBox.information(main_window, "Empréstimos", "Emprésitmo finalizado com sucesso!")
                self.service_main_window.populate_table_emprestimos_ativos(main_window)
            except Exception as e:
                QMessageBox.warning(main_window, "Atenção", f'Problema ao realizar recebimento.\n'
                                                     f'Erro: {e}')