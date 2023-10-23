from PySide6.QtWidgets import QMessageBox

from infra.entities.funcionario import Funcionario
from infra.repository.emprestimo_repository import EmprestimoRepository
from infra.repository.funcionario_repository import FuncionarioRepository
from infra.repository.uniforme_repository import UniformeRepository
from services.mainwindow_service import MainWindowService


class FuncionarioService:
    def __init__(self):

        self.emprestimos_repository = EmprestimoRepository()
        self.uniforme_repository = UniformeRepository()
        self.funcionario_repository = FuncionarioRepository()
        self.main_window_service = MainWindowService()

    def insert_funcionario(self, main_window):
        funcionario = Funcionario()
        funcionario.nome = main_window.txt_nome.text()
        funcionario.cpf = main_window.txt_cpf.text()
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