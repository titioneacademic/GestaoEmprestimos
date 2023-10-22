from __future__ import annotations

from typing import List

from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column
from infra.configs.base import Base


class Ator(Base):
    __tablename__ = 'atores'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    nascimento: Mapped[int] = mapped_column(nullable=False)
    filmes: Mapped[List[Filme]] = relationship(secondary=association_table, back_populates='atores', lazy=False)

    # Esta função demonstra o objeto de uma forma mais legível
    def __repr__(self):
        return f'Ator [Nome = {self.nome}, Ano de nascimento = {self.nascimento}]'
