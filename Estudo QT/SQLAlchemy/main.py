from infra.repository.filme_repository import FilmeRepository
from infra.configs.connection import DBConnectioHandler
from infra.entities.filme_muitos_pra_muitos import Filme, Ator


#
# filme_1 = Filme(
#     titulo='Joker',
#     genero='ação',
#     ano=2018
# #    atores=[joaquim, jhon]
# )
# joaquim = Ator(
#     nome='Joaquim Phoenix',
#     nascimento=1075,
#     filme=filme_1
# )
#
# jhon = Ator(
#     nome='Jhon Cena',
#     nascimento=1075,
#     filme=filme_1
# )
#
# filme_2 = Filme(
#     titulo='Bátima',
#     genero='ação',
#     ano=1984
# #    atores=[joaquim, bacon]
# )
#
# bacon = Ator(
#     nome='Keving Bacon',
#     nascimento=1075,
#     filme=filme_2
#
# )


#
# filmes = [filme_2, filme_1]

repo = FilmeRepository()
data_base = DBConnectioHandler()
# repo.insert(filme_1)

# f = repo.select_all()

# f2 = repo.select_filme_by_id(1)
# atores2 = f2.atores
# a1 = repo.select_ator_by_id(1)
#
# print(f2)
# for ator in atores2:
#     print(ator)


# repo.insert('Algum', 'Comedia', 2023)
# repo.insert('Testando', 'Ação', 2014)
# data = repo.select_all()
#
# print(data)
