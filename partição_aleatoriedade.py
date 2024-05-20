import random

dic_receitas = {'Pizza' : 'Pré-aqueça o forno a 230°C.Estique a massa de pizza em uma forma untada.Espalhe o molho de tomate sobre a massa.Cubra com queijo mussarela e os ingredientes opcionais.Asse por 10-15 minutos, ou até que a massa esteja crocante e o queijo derretido.Retire do forno, corte em fatias e sirva.',
                'Salada de Frutas':'Modo de preparo: Corte as frutas em pedaços pequenos e misture em uma tigela. Regue com um pouco de suco de laranja ou limão para dar um toque refrescante.',
                  'Sanduíche de Frango':'Modo de preparo: Misture o frango desfiado com a maionese. Espalhe a mistura sobre uma fatia de pão, adicione a cenoura ralada e algumas folhas de alface. Cubra com outra fatia de pão e sirva.' }

lista = dic_receitas.items()
lista_receitas = [f"{chave}: {valor}" for chave, valor in lista]
receitas = ", ".join(lista_receitas)
print(random.choice(lista_receitas))