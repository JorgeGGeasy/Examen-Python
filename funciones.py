import random

def encontrar_menores(diccionario,letra):
    """Dado un diccionario de palabras, y una letra, esta funciÃ³n devuelve la lista de palabras que empiezan por una 
       letra que alfabÃ©ticamente estÃ¡ antes que la indicada.
    Args:
      diccionario
      letra
    Returns:
      resultado: ej. ['AUNQUE','ABINAR']
    """
    letras = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
    posicion = 0
    posicionPalabras = 0
    resultado=[]

    for i in range(0,26):
        if letra == letras[i]:
            break
        posicion+=1
    
    for clave in diccionario:
        for palabra in diccionario[clave]:
            for i in range(0,26):
                print(palabra[0])
                print(letras[i])
                if palabra[0] == letras[i]:
                    break
                posicionPalabras+=1
            print(posicionPalabras)
            if posicionPalabras <= posicion:
                resultado.append(palabra)
        posicionPalabras = 0
                
    return resultado

def add_client(clients_list,nif,name,address,phone,email):
    """Dado un diccionario de clientes y datos de un nuevo cliente, esta funciÃ³n inserta estos datos como un nuevo cliente.
    Args:
      diccionario
      nif
      name 
      address
      phone
      email
    """
    clients_list[nif] = {
        nif: {'name': name,
              'address': address,
              'phone': phone,
              'email': email
        }
    }

def repartir_cartas(cartas_iniciales,repeticiones):
    """Dada una baraja de cartas iniciales y un nÃºmero de repeticiones, esta funciÃ³n selecciona 
       5 cartas aleatorias de esta baraja y las mete en un diccionario llamado combinaciones. 
       El proceso se repite tantas veces como repeticiones se indiquen.
    Args:
      cartas_iniciales
      repeticiones
    Returns:
      combinaciones: ej. {'repeticion1': ['contable', 'alguacil', 'asesino', 'cardenal', 'obispo']}
    """    
    combinaciones={}
    for i in range(1,repeticiones+1):
        cartas_aleatorias = cartas_iniciales 
        combinaciones["repeticion"+str(i)]=[]
        for j in range(0,5):
            carta=random.choice(cartas_aleatorias)
            combinaciones["repeticion"+str(i)].append(carta)
            cartas_aleatorias.remove(carta)

    return combinaciones

    