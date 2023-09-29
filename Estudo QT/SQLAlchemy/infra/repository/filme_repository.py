from infra.configs.connection import DBConnectioHandler
from infra.entities.filme_muitos_pra_muitos import Filme, Ator


class FilmeRepository:


    def select_filme_by_id(self, id):
        with (DBConnectioHandler() as db):
            filme = db.session.query(Filme).filter(Filme.id == id).first()
            return filme

    def select_ator_by_id(self, id):
        with DBConnectioHandler() as db:
            ator = db.session.query(Ator).filter(Ator.id == id).first()
            return ator

    def select_atores_by_filme_id(self, id):
        with DBConnectioHandler() as db:
            atores = db.session.query(Ator).filter(Ator.filme_id == id).all()
            return atores
    def select_all(self):
        with DBConnectioHandler() as db:
            data = db.session.query(Filme).all()
            return data

    def select_one(self):
        with DBConnectioHandler() as db:
            data = db.session.query(Filme).first()
            return data

    def insert(self, filmes):
        with DBConnectioHandler() as db:
            db.session.add_all(filmes)
            db.session.commit()

    def delete(self, titulo):
        with DBConnectioHandler() as db:
            db.session.query(Filme).filter(Filme.titulo == titulo).delete()
            db.session.commit()

    def update(self, titulo, ano):
        with DBConnectioHandler() as db:
            db.session.query(Filme).filter(Filme.titulo == titulo).update({'ano': ano})
            db.session.commit()