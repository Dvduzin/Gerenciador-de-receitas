# Projeto-FPA-GP7: Gerenciamento de Receitas

## 1. Descrição

Este é um gerenciador de receitas, que através de um menu de multifunções consegue-se adicionar, visualizar, modificar e remover receitas, além de outras funcionalidades. A utilizadção do menu funciona da seguinte forma:

Ao pressionar: 
1 -> O usuário poderá adicionar pratos; 
2 -> O usuário poderá visualizar os seus pratos já adicionados; 
3 -> O usuário poderá modificar algum elemento já adicionado;
4 -> O usuário poderá remover uma receita já adicionada;
5 -> O usuário poderá filtrar as receitas por nacionalidade;
6 -> O usuário poderá sortear uma receita aleatórias pré-definidas;
7 -> O usuário poderá adicionar receitas à categoria favorito;
8 -> O usuário poderá sortear uma receita já inclusa entre os favoritos;
9 -> O usuário poderá visualizar as suas receitas favoritadas;
10 -> O usuário poderá remover uma receita favoritada;
11 -> O usuário poderá encerrar a utilização do programa.

Acentuações, pontuações e caracteres especiais são reconhecidos. Todos os primeiros caracteres da palavra serão retornados como maiúsculo.

Passo a passo de instalação e configuração:
## 2. Configuração

Pacotes utilizados:
1. Python 3.12.2 (extensão no Visual Studio Code)
2. Visual Studio Code


Passo a passo de instalação e configuração:

1. Instale a pasta "Projeto_Python";
2. Descompacte a pasta;
3. Realoque a pasta para o disco local "C";
4. Instale o Visual Studio Code e quando abri-lo instale a extensão do python;
5. No Visual Studio Code abra a pasta "Projeto_Python";
6. Rode a aplicação "Projeto_Python".

## 3. Requisitos

O código deve:

1. Possibilitar o cadastro de receitas com: seu país de origem, seu nome, seus ingredientes e o seu modo de preparo;
2. O programa é baseado na utilização de um CRUD de receitas;
3. O programa deverá oferecer a função de buscar receitas por sua nacionalidade;
4. O software fornece o armazenamento das informações, enviadas pelo usuário, diretamente ao banco de dados;
5. O programa oferece a possibilidade de classificar as receitas como favoritos para deixá-las e visualizá-las em destaque;
6. O software disponibiliza a função de aleatorizar receitas predefinidades;
7. Além de todas essas funcionalidades, o programa oferece uma função extra de sortear uma das receitas favoritadas pelo usuário.

## 4. Progresso Atual

Lista de requisitos:

- [x] Cadastro de itens por input
- [x] Armazenamento de itens em banco de dados
- [x] Visualização, modificação e remoção de elemento
- [x] Filtrar por elementos
- [x] Listar elementos separadamente
- [x] Aleatorizar aparição de itens
- [x] Ter uma função singular
- [x] Tratamentos de erros 

## 5. Briefing do Projeto
## Definição do objetivo:
Rafael é um entusiasta da culinária e adora experimentar novas receitas de
diversos países. No entanto, ele enfrenta dificuldades em organizar suas receitas
favoritas e muitas vezes acaba perdendo as que mais gostou. Como um programador
dedicado, você decidiu ajudá-lo a criar um sistema de Gerenciamento de Receitas
para que Rafael possa manter o controle de suas descobertas gastronômicas.

### Exemplo
- Menu de ações: 1

- Escreva o nome do prato: Pizza

-Digite o país: Itália

-Escreva os ingredientes do prato Pizza: Sal, farinha...

-Escreva o modo de preparo do prato Pizza: Misture bem os ingredientes...

## 6. Orientações de visualização

Quando for visualizar uma receita se atente na seguinte divisão:
1° A primeira palavra que vem é o país e ele separa-se do nome do prato por um ":";
2° A segunda palavra que vem é o nome do prato e ele separa-se do país sendo antecedido pelo ":" e se separa dos ingredientes sendo sucedido de um "|";
3° A terceira palavra que vem são os ingredientes que são antecedidos pela "|" e sucedido pela "/";
4° A quarta palavra que aparece é o modo de preparo que é antecedido pela "/".

## 7. Fluxograma
Link para o fluxograma: 
https://miro.com/app/board/uXjVKGZ8QeY=/?share_link_id=984132930001&shareablePresentation=1
