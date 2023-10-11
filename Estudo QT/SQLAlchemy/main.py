from infra.repository.filme_repository import FilmeRepository
from infra.configs.connection import DBConnectioHandler
from infra.entities.filme_um_pra_muitos import Filme, Ator



#Ajustar delete e cascade



joaquim = Ator(
    nome='Joaquim Phoenix',
    nascimento=1075
)

jhon = Ator(
    nome='Jhon Cena',
    nascimento=1075,
)

bacon = Ator(
    nome='Keving Bacon',
    nascimento=1075
)

atores=[joaquim, jhon]

filme_1 = Filme(
    titulo='Joker',
    genero='ação',
    ano=2018,
    atores=atores
)

filme_2 = Filme(
    titulo='Bátima',
    genero='ação',
    ano=1984,
)
filme_2.atores.append(bacon)



filmes = [filme_2, filme_1]

repo=FilmeRepository()
data_base=DBConnectioHandler()
# repo.insert(filme_1)
repo.insert_many(filmes)

f=repo.select_all()
batima=f[0]
batima.titulo='Batman The Bat'
# f2 = repo.select_filme_by_id(1)
# atores2 = f2.atores
# a1 = repo.select_ator_by_id(1)
#
repo.update(batima)
print(f)

repo.delete(batima)

f=repo.select_all()
print(f)
# for ator in atores2:
#     print(ator)


# repo.insert('Algum', 'Comedia', 2023)
# repo.insert('Testando', 'Ação', 2014)
# data = repo.select_all()
#
# print(data)
