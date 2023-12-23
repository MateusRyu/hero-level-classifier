import json

red = "\033[91m"
green = "\033[92m"
reset = "\033[0m"

def alert(message):
    print(f"{red}{message}{reset}")

def success(message):
    print(f"{green}{message}{reset}")

def read_json_file(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        alert(f"O arquivo '{filename}' não foi encontrado.")
    except json.JSONDecodeError:
        alert(f"Erro ao decodificar o JSON no arquivo '{filename}'.")

def get_inputs():
    name = input("Qual o nome do herói? Digite o nome e pressione [ENTER]!\n")
    xp = -1

    while xp < 0:
        xp = guess_xp(name)
    return [name, xp]

def guess_xp(name):
    try:
        xp = int(input(f"\nQual a quantidade de experência (XP) de {name}? \nDigite o valor apenas com números e pressione [ENTER]!\n"))
        if xp < 0:
            raise ValueError
        return xp
    except ValueError:
        alert("O valor de XP deve ser um número inteiro positivo, sem espaços, pontos ou vírgulas!")
        return -1

def classify_hero(xp):
    levels = read_json_file("levels.json")
    hero_level = ""
    for level in levels:
        if xp >= level["min_xp"]:
            hero_level = level["name"]

    return hero_level

if __name__ == "__main__":
    name, xp = get_inputs()
    hero_level = classify_hero(xp)
    success(f"O Herói de nome {name} está no nível de {hero_level}")
