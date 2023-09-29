from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from infra.configs.base import Base


# association_table = Table(
#     "ator_filmes",
#     Base.metadata,
#     Column("ator_id", ForeignKey("atores.id"), primary_key=True),
#     Column("filme_id", ForeignKey("filmes.id"), primary_key=True),
# )

class Filme(Base):
    __tablename__ = 'filmes'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(nullable=False)
    genero: Mapped[str] = mapped_column(nullable=False)
    ano: Mapped[int] = mapped_column(nullable=False)
    atores: Mapped[List["Ator"]] = relationship()


    # Esta função demonstra o objeto de uma forma mais legível
    def __repr__(self):
        return f'Filme [titulo={self.titulo}, ano={self.ano}]'


class Ator(Base):
    __tablename__ = 'atores'

    id: Mapped[int]  = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str]  = mapped_column(nullable=False)
    nascimento: Mapped[int]  = mapped_column(nullable=False)
    filme_id: Mapped[int] = mapped_column(ForeignKey("filmes.id"))


    # Esta função demonstra o objeto de uma forma mais legível
    def __repr__(self):
        return f'Ator [Nome = {self.nome}, Ano de nascimento = {self.nascimento}]'