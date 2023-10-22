from __future__ import annotations
from typing import List
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column
from infra.configs.base import Base

association_table = Table(
    "emprestimos",
    Base.metadata,
    Column("funcionario_id", ForeignKey("funcionarios.id"), primary_key=True),
    Column("uniforme_id", ForeignKey("uniformes.id"), primary_key=True),

)

class Filme(Base):
    __tablename__ = 'filmes'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(nullable=False)
    genero: Mapped[str] = mapped_column(nullable=False)
    ano: Mapped[int] = mapped_column(nullable=False)
    atores: Mapped[List[Ator]] = relationship(secondary=association_table, back_populates='filmes', lazy=False)

    # Esta função demonstra o objeto de uma forma mais legível
    def __repr__(self):
        return f'Filme [titulo={self.titulo}, ano={self.ano}]'


class Ator(Base):
    __tablename__ = 'atores'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    nascimento: Mapped[int] = mapped_column(nullable=False)
    filmes: Mapped[List[Filme]] = relationship(secondary=association_table, back_populates='atores', lazy=False)

    # Esta função demonstra o objeto de uma forma mais legível
    def __repr__(self):
        return f'Ator [Nome = {self.nome}, Ano de nascimento = {self.nascimento}]'
