dados = [input(), input(), input()]

animais = {
    "aguia": ["vertebrado", "ave", "carnivoro"],
    "pomba": ["vertebrado", "ave", "onivoro"],
    "homem": ["vertebrado", "mamifero", "onivoro"],
    "vaca": ["vertebrado", "mamifero", "herbivoro"],
    "pulga": ["invertebrado", "inseto", "hematofago"],
    "lagarta": ["invertebrado", "inseto", "herbivoro"],
    "sanguessuga": ["invertebrado", "anelideo", "hematofago"],
    "minhoca": ["invertebrado", "anelideo", "onivoro"]
}

for animal, caracteristicas in animais.items():
    for caracteristica in caracteristicas:
        if caracteristica in dados:
            print(animal)
