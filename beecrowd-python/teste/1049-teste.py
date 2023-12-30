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


for animal in animais:
    count = 0
    if animais[animal][0] == dados[0] or animais[animal][0] == dados[1] or animais[animal][0] == dados[2]:
       count+= 1
    if animais[animal][1] == dados[0] or animais[animal][1] == dados[1] or animais[animal][1] == dados[2]:
       count+= 1
    if animais[animal][2] == dados[0] or animais[animal][2] == dados[1] or animais[animal][2] == dados[2]:
       count+= 1
    if count == 3:
        print(animal)

