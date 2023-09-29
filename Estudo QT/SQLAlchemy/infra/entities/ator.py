from typing import List
from infra.configs.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship



# class Ator(Base):
#     __tablename__ = 'atores'
#
#     id: Mapped[int]  = mapped_column(primary_key=True, autoincrement=True)
#     nome: Mapped[str]  = mapped_column(nullable=False)
#     nascimento: Mapped[int]  = mapped_column(nullable=False)
#     filme: Mapped[List["Filme"]] = relationship('filmes', secondary=association_table, back_populates='atores')
#
#
#     # Esta função demonstra o objeto de uma forma mais legível
#     def __repr__(self):
#         return f'Ator [Nome = {self.nome}, Ano de nascimento = {self.nascimento}]'