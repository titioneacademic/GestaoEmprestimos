from __future__ import annotations

from datetime import datetime
from typing import List
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column
from infra.configs.base import Base

class Uniforme(Base):
    __tablename__ = 'uniformes'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    #todo adicionar o atributo unique
    nome: Mapped[str] = mapped_column(nullable=False, unique=True)
    #todo remover abaixo
    # funcionarios: Mapped[List[Funcionario]] = relationship(secondary='emprestimos', back_populates='uniformes', lazy=False)
    emprestimos = relationship("Emprestimo", back_populates="uniforme")

    # Esta função demonstra o objeto de uma forma mais legível
    def __repr__(self):
        return f'Uniforme [Nome = {self.nome}]'
