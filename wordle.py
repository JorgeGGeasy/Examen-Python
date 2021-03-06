import random

def choose_secret():
    """Dado un nombre de fichero, esta funciÃ³n devuelve una palabra aleatoria de este fichero transformada a mayÃºsculas.
    Args:
      filename: El nombre del fichero. Ej. "palabras_reduced.txt"
    Returns:
      secret: Palabra elegida aleatoriamente del fichero transformada a mayÃºsculas. Ej. "CREMA"
    """
    listaPalabras=[]
    error = False
    try:
        with open("palabras_reduced.txt", mode="rt", encoding="utf-8") as f:
            for linea in f:
                listaPalabras.append(linea)
    except:
        error = True
    if(error or len(listaPalabras) == 0):
        raise ValueError("Fichero vacio")
    palabra = random.choice(listaPalabras)
    #lower(): transforma a minúsculas la cadena pasada como parámetro
    #upper(): transforma a mayúsculas la cadena pasada como parámetro
    return palabra.upper() 
    
def compare_words(word, secret):
    """Dadas dos palabras en mayÃºsculas (word y secret), esta funciÃ³n calcula las posiciones de las letras de word que aparecen 
    en la misma posiciÃ³n en secret, y las posiciones de las letras de word que aparecen en secret pero en una posiciÃ³n distinta.
    Args:
      word: Una palabra. Ej. "CAMPO"
      secret: Una palabra. Ej. "CREMA"
    Returns:
      same_position: Lista de posiciones de word cuyas letras coinciden en la misma posiciÃ³n en secret. En el caso anterior: [0]
      same_letter: Lista de posiciones de word cuyas letras estÃ¡n en secret pero en posiciones distintas. En el caso anterior: [1,2]
    """
    same_position=[]
    same_letter=[]

    if len(word) != len(secret)-1:
        raise ValueError("No tienen el mismo tamaño")


    for i in range(0,len(word)):
        if word[i] == secret[i]:
            same_position.append(i)

    for i in range(0,len(word)):
        for j in range(0,len(word)):
            if word[j] == secret[i]:
                same_letter.append(j)

    for i in range(0,len(same_letter)):
        if same_letter[i] < 0 or same_letter[i] > len(word):
            raise ValueError("Same_letter incluye valores negativos o tiene mayor longitud que la palabra")
    for i in range(0,len(same_position)):
        if same_position[i] < 0 or same_position[i] > len(word):
            raise ValueError("Same_position incluye valores negativos o tiene mayor longitud que la palabra")

    return same_position , same_letter

def print_word(word, same_position, same_letter):
    """Dada una palabra, una lista same_position y otra lista same_letter, esta funciÃ³n crearÃ¡ 
    un string donde aparezcan en mayÃºsculas las letras de la palabra que ocupen las posiciones de same_position, 
    en minÃºsculas las letras de la palabra que ocupen las posiciones de same_letter y un guiÃ³n (-) en el resto de posiciones
    Args:
      word: Una palabra. Ej. "CAMPO"
      same_letter_position: Lista de posiciones. Ej. [0]
      same_letter: Lista de posiciones. Ej. [1,2]
    Returns:
      transformed: La palabra aplicando las transformaciones. En el caso anterior: "Cam--"
      
      CAMPO
      
      CREMA

      C--ma
    """
    transformed = ["-","-","-","-","-"]
    for i in range(0,len(same_letter)):
        transformed[same_letter[i]] = word[same_letter[i]].lower()
    for i in range(0,len(same_position)):
        transformed[same_position[i]] = word[same_position[i]]


    
    return transformed
    
def choose_secret_advanced():
    """Dado un nombre de fichero, esta funciÃ³n filtra solo las palabras de 5 letras que no tienen acentos (Ã¡,Ã©,Ã­,Ã³,Ãº). 
       De estas palabras, la funciÃ³n devuelve una lista de 15 aleatorias no repetidas y una de estas 15, se selecciona aleatoriamente como palabra secret.
    Args:
      filename: El nombre del fichero. Ej. "palabras_extended.txt"
    Returns:
      selected: Lista de 15 palabras aleatorias no repetidas que tienen 5 letras y no tienen acentos
      secret: Palabra elegida aleatoriamente de la lista de 15 seleccionadas transformada a mayÃºsculas
    """
    listaPalabras=[]
    palabrasProhibidas=[]
    palabrasLargas=[]
    with open("palabras_extended.txt", mode="rt", encoding="utf-8") as f:
        for linea in f:
            listaPalabras.append(linea)

    for i in range(0, len(listaPalabras)):
        for j in range(0,len(listaPalabras[i])):
            if listaPalabras[i][j] == "á" or listaPalabras[i][j] == "é" or listaPalabras[i][j] == "í" or  listaPalabras[i][j] == "ó" or  listaPalabras[i][j] == "ú":
                palabrasProhibidas.append(listaPalabras[i])

    for i in range(0, len(palabrasProhibidas)):
        listaPalabras.remove(palabrasProhibidas[i])

    for i in range(0, len(listaPalabras)):
        if len(listaPalabras[i]) > 6:
            palabrasLargas.append(listaPalabras[i])

    for i in range(0, len(palabrasLargas)):
        listaPalabras.remove(palabrasLargas[i])
    
    # Falta lo de barajas 15 veces
    palabra = random.choice(listaPalabras)
    return palabra.upper() 
 
def check_valid_word(word, lista):
    """Dada una lista de palabras, esta funciÃ³n pregunta al usuario que introduzca una palabra hasta que introduzca una que estÃ© en la lista. Esta palabra es la que devolverÃ¡ la funciÃ³n.
    Args:
      selected: Lista de palabras.
    Returns:
      word: Palabra introducida por el usuario que estÃ¡ en la lista.
    """
    vacio = ""
    for i in range(0, len(lista)):
        if lista[i] == word:
            return word
    return vacio

if __name__ == "__main__":
    resultadoCheck = False
    while(resultadoCheck == False):
        word = input("Introduce una palabra que este en la lista ")
        lista=["UNO","DOS","TRES","CUATRO"]
        palabra = check_valid_word(word, lista)
        if palabra == word:
            resultadoCheck = True
            print("Bien")
        else:
            print("Mal intentalo de nuevo")

    secret=choose_secret()
    print("Palabra a adivinar: "+secret)#Debug: esto es para que sepas la palabra que debes adivinar
    for repeticiones in range(0,6):
        word = input("Introduce una nueva palabra: ")
        same_position, same_letter = compare_words(word, secret)
        resultado=print_word(word,same_position, same_letter)
        print(resultado)
        print( "Word y secret")
        print(word)
        print(secret)
        if word == secret:
            print("HAS GANADO!!")
            exit()
    print("LO SIENTO, NO LA HAS ADIVINIDADO. LA PALABRA ERA "+secret)   

    secret=choose_secret_advanced()
    print("Palabra a adivinar: "+secret)#Debug: esto es para que sepas la palabra que debes adivinar
    for repeticiones in range(0,6):
        word = input("Introduce una nueva palabra: ")
        same_position, same_letter = compare_words(word, secret)
        resultado=print_word(word,same_position, same_letter)
        print(resultado)
        print( "Word y secret")
        print(word)
        print(secret)
        if word == secret:
            print("HAS GANADO!!")
            exit()
    print("LO SIENTO, NO LA HAS ADIVINIDADO. LA PALABRA ERA "+secret)   