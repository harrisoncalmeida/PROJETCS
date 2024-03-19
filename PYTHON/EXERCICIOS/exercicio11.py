#Exemplo Dicionários
game = {"nome":"Super Mario",
        "desenvolvedora":"Nintendo",
        "ano":1990}
print(game)

#Exemplo 1
print(game["nome"])
print(game["desenvolvedora"])
print(game["ano"])

#Exemplo 2
print(game.values())

#Exemplo 3
for i in game.values():
    print(i)

#Exemplo 4
print(game.keys())

#Exemplo 5
for i in game.keys():
    print(i)

#Exemplo 6
print(game.items())

#Exemplo 7
for i,j in game.items():  # i = pega os nome da chaves e j = vai pegar os dados
    print("{} = {}".format(i, j))

#Exemplo 8
game = []
game1 = {"nome":"Super Mario",
         "VideoGame":"Super Nintendo",
         "ano":1990}
game2 = {"nome":"Zelda Ocarina of time",
         "VideoGame":"Nintendo 64",
         "ano":1998}
game3 = {"nome":"Pokemon Yellow",
         "VideoGame":"Game Boy",
         "ano":1999}
games = [game1, game2, game3]
print(games)

#Exemplo 9
game = {}
games = []
for i in range(3):
    game["nome"] = input("Qual o nome do jogo?")
    game["videogame"] = input("Para qual video-game ele foi lançado?")
    game["ano"] = input("Qual ano ele foi lançado?")
    games.append(game.copy())
print("-" * 20)
for e in games:
    for i,j in e.items():
        print("O campo {} tem o valor {}".format(i,j))

#Exemplo 10
games = {"nome":["Super Mario", "Zelda Ocarina of Time", "Pokemon Yellow"],
         "videogame": ["Super Nintendo", "Nintendo 64", "Game Boy"],
         "ano": [1990,1998,1999]}
print(games)

#Exemplo 11
games = {"nome":[], "videogame":[], "ano":[]}
for i in range(3):
    nome = input("Qual o nome do jogo?")
    videogame = input("Qual o video-game?")
    ano = input("Qual ano foi lançado?")
    games["nome"].append(nome)
    games["videogame"].append(videogame)
    games["ano"].append(ano)
print("-" * 20)
print(games)