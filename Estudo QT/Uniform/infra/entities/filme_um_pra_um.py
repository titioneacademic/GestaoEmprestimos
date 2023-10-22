from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from infra.configs.base import Base


class Filme(Base):
    __tablename__ = 'filmes'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(nullable=False)
    genero: Mapped[str] = mapped_column(nullable=False)
    ano: Mapped[int] = mapped_column(nullable=False)
    ator: Mapped["Ator"] = relationship(back_populates="filme")


    # Esta função demonstra o objeto de uma forma mais legível
    def __repr__(self):
        return f'Filme [titulo={self.titulo}, ano={self.ano}]'


class Ator(Base):
    __tablename__ = 'atores'

    id: Mapped[int]  = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str]  = mapped_column(nullable=False)
    nascimento: Mapped[int]  = mapped_column(nullable=False)
    filme_id : Mapped[int] = mapped_column(ForeignKey("filmes.id"))
    filme: Mapped["Filme"] = relationship(back_populates='ator')


    # Esta função demonstra o objeto de uma forma mais legível
    def __repr__(self):
        return f'Ator [Nome = {self.nome}, Ano de nascimento = {self.nascimento}]'