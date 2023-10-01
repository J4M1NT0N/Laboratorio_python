# Elaborar un programa que tenga un archivo de texto
# llamado EN-ES.txt el cual contiene las traducciones de palabras
# en ingles al español

traduccion_es_eng = {
    "perro": "dog",
    "gato": "cat",
    "silla": "chair",
    "tiempo": "time",
    "año": "year",
    "dia": "day",
    "cosa": "thing",
    "hombre": "man",
    "mundo": "world",
    "ciudad": "city",
}

traduccion_eng_es = {
    "dog": "perro",
    "cat": "gato",
    "chair": "silla",
    "time": "tiempo",
    "year": "año",
    "day": "dia",
    "thing": "cosa",
    "man": "hombre",
    "world": "mundo",
    "city": "ciudad",
}


def traducir(palabra, idioma_notrad, idioma_trad):
    if idioma_notrad == "español" and idioma_trad == "ingles":
        if palabra in traduccion_es_eng:
            return traduccion_es_eng[palabra]
        else:
            return "Palabra no encontrada en el diccionario."
    elif idioma_notrad == "ingles" and idioma_trad:
        if palabra in traduccion_eng_es:
            return traduccion_eng_es[palabra]
        else:
            return "Palabra no valida"


def agregar_palabra():
    palabra = input("Ingrese una nueva palabra en español: ")
    traduc = input("Ingrese la traduccion de la palabra en ingles: ")

    traduccion_eng_es[traduc] = palabra
    traduccion_es_eng[palabra] = traduc

    print(f"Se ha agregado una palabra al diccionario.")
    guard_en_dicci()


def guard_en_dicci():
    with open("En-Es.txt", "w") as archivo:
        archivo.write("Traducción de español a ingles:\n")
        for palabra, traduc in traduccion_es_eng.items():
            archivo.write(f"{palabra_a_traducir} ---> {resultado}")

        archivo.write("Traducción de español a ingles:\n")
        for palabra, traduc in traduccion_eng_es.items():
            archivo.write(f"{palabra_a_traducir} ---> {resultado}")


while True:
    print("1. Traducir una palabra")
    print("2. Agregar una nueva palabra al diccionario")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        idioma_notrad = input(
            "Elija el idioma de origen (español o ingles): ").lower()
        idioma_trad = input(
            "Elija el idioma de destino (español o ingles): ").lower()
        palabra_a_traducir = input("Ingrese la palabra a traducir: ")
        resultado = traducir(palabra_a_traducir, idioma_notrad, idioma_trad)
        print(f'{palabra_a_traducir} ----> {resultado}')
    elif opcion == '2':
        agregar_palabra()
    elif opcion == '3':
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

print("Vuelva pronto!!")
