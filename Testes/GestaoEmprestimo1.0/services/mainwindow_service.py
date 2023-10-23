from PySide6.QtWidgets import QTableWidgetItem

from infra.repository.emprestimo_repository import EmprestimoRepository
from infra.repository.uniforme_repository import UniformeRepository
from infra.repository.funcionario_repository import FuncionarioRepository


class MainWindowService:
    def __init__(self):

        self.emprestimos_repository = EmprestimoRepository()
        self.uniforme_repository = UniformeRepository()
        self.funcionario_repository = FuncionarioRepository()

    def populate_table_funcionario(self, main_window):
        main_window.tb_funcionario.setRowCount(0)
        lista_funcionarios = self.funcionario_repository.select_all_funcionarios()
        # lista_uniforme[:] para criar uma cópia da lista original e iterar sobre essa cópia, enquanto modificamos a lista original.
        for funcionario in lista_funcionarios[:]:
            if not funcionario.ativo:
                lista_funcionarios.remove(funcionario)
        main_window.tb_funcionario.setRowCount(len(lista_funcionarios))
        for linha, funcionario in enumerate(lista_funcionarios):
            if funcionario.ativo is True:
                main_window.tb_funcionario.setItem(linha, 0, QTableWidgetItem(funcionario.nome))
                main_window.tb_funcionario.setItem(linha, 1, QTableWidgetItem(funcionario.cpf))

    def populate_table_uniforme(self, main_window):
        main_window.tb_uniformes.setRowCount(0)
        lista_uniforme = self.uniforme_repository.select_all_uniformes()
        #lista_uniforme[:] para criar uma cópia da lista original e iterar sobre essa cópia, enquanto modificamos a lista original.
        for uniforme in lista_uniforme[:]:
            if not uniforme.ativo:
                lista_uniforme.remove(uniforme)
        main_window.tb_uniformes.setRowCount(len(lista_uniforme))
        for linha, uniforme in enumerate(lista_uniforme):
            if uniforme.ativo is True:
                main_window.tb_uniformes.setItem(linha, 0, QTableWidgetItem(uniforme.nome))


    def populate_table_emprestimos_ativos(self, main_window):
        emprestimos_ativos = self.emprestimos_repository.select_emprestimos_ativos()

        main_window.tb_emprestimos_ativos.setRowCount(len(emprestimos_ativos))
        for linha, (emp, funcionario, uniforme) in enumerate(emprestimos_ativos):
            main_window.tb_emprestimos_ativos.setItem(linha, 0, QTableWidgetItem(funcionario.nome))
            main_window.tb_emprestimos_ativos.setItem(linha, 1, QTableWidgetItem(funcionario.cpf))
            main_window.tb_emprestimos_ativos.setItem(linha, 2, QTableWidgetItem(emp.data_emprestimo.strftime('%d/%m/%Y')))
            main_window.tb_emprestimos_ativos.setItem(linha, 3, QTableWidgetItem(uniforme.nome))

    def populate_uniformes(self, emprestimo_ui):
        emprestimo_ui.cb_uniforme.clear()
        emprestimo_ui.cb_uniforme.addItem('Selecione um item')
        emprestimo_ui.uniformes = self.uniforme_repository.select_all_uniformes()
        # lista_uniforme[:] para criar uma cópia da lista original e iterar sobre essa cópia, enquanto modificamos a lista original.
        for uniforme in emprestimo_ui.uniformes[:]:
            if not uniforme.ativo:
                emprestimo_ui.uniformes.remove(uniforme)
        for uniforme in emprestimo_ui.uniformes:
            # Supondo que o Uniforme tenha um atributo 'nome' que você quer mostrar no QComboBox
            emprestimo_ui.cb_uniforme.addItem(uniforme.nome)

    def populate_relatorio(self, main_window):
        pass