from __future__ import annotations

from sqlalchemy.orm import relationship, Mapped, mapped_column
from infra.configs.base import Base


class Funcionario(Base):
    __tablename__ = 'funcionarios'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    cpf: Mapped[str] = mapped_column(nullable=False, unique=True)
    #todo remover abaixo
    # uniformes: Mapped[List[Uniforme]] = relationship(secondary='emprestimos', back_populates='funcionarios', lazy=False)
    emprestimos = relationship("Emprestimo", back_populates="funcionario")

    # Esta função demonstra o objeto de uma forma mais legível
    def __repr__(self):
        return f'Funcionario [nome={self.nome}, cpf={self.cpf}]'
