import json

default_db_file = "excript.txt"


def cargar_datos():
    arreglo_file = []
    with open(default_db_file) as f:
        for item in f:
            timen = item.replace('\n', "")
            arreglo_file.append(timen)
    return arreglo_file


def encriptar(palabra, arreglo_file):
    excripted_words = ""
    posArr = {}

    for char in palabra:
        remplazado = False
        for i in arreglo_file:
            ii = i.split(",")
            if str(ii[0]).lower() == str(char).lower():
                remplazado = True
                excripted_words += str(ii[1])
                break

        if remplazado:
            reverse = excripted_words[::-1]
            posArr[len(excripted_words) - 1] = reverse[0]

    return excripted_words, posArr


def desencriptar(palabra, arreglo_file, posArr):
    original_word = ""

    for i, char in enumerate(palabra):
        if i in posArr:
            reverse_char = posArr[i]
            for item in arreglo_file:
                ii = item.split(",")
                if str(ii[1]) == reverse_char:
                    original_word += str(ii[0])
                    break
        else:
            original_word += char

    return original_word


word = input("Ingrese Palabra a encriptar: ")

arreglo_file = cargar_datos()

encrypted_word, posArr = encriptar(word, arreglo_file)

print("Su frase encriptada es: " + str(encrypted_word))
print("Cantidad de caracteres leídos: " + str(len(encrypted_word)))

decrypted_word = desencriptar(encrypted_word, arreglo_file, posArr)
print("Su frase desencriptada es: " + decrypted_word)
