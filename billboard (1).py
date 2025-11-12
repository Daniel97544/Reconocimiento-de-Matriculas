def cargar_canciones(ruta_archivo:str)->list:
    lista_canciones=[]
    
    archivo=open(ruta_archivo,'r')
    titulos=archivo.readline()
    print(titulos)
    informacion=archivo.readline()
    
    while len(informacion)>0:
        info=informacion.split(',')
        posicion=info[0]
        nombre_cancion=info[1]
        nombre_artista=info[2]
        anio=info[3]
        letra=info[4]
        
        l_canciones={'posicion':posicion,
                         'nombre_cancion':nombre_cancion,
                         'nombre_artista':nombre_artista,
                         'anio':anio,
                         'letra':letra}
        lista_canciones.append(l_canciones)
        
        informacion=archivo.readline()
    archivo.close()
    return lista_canciones

def buscar_cancion(lista_canciones:list,nombre_cancion:str,anio:int):
    rta=[]
    for cada_cancion in lista_canciones:
        if cada_cancion['nombre_cancion']==nombre_cancion and cada_cancion['anio']==anio:
            rta.append(cada_cancion)
    return rta

def canciones_anio(lista_canciones:list,anio:int)->list:
    cancion_anio=[]
    
    for cada_cancion in lista_canciones:
        if cada_cancion['anio']==anio:
            cancion_anio.append(cada_cancion[:3])
            
    return cancion_anio

def canciones_artista_periodo(lista_canciones:list,artista:str,anio_inicial:int,anio_final:int)->list:
    
    canciones_a=[]
    
    for cada_cancion in lista_canciones:
        if cada_cancion['nombre_artista']==artista and anio_inicial <= cancion['anio'] <= anio_final:
            canciones_a.append(cada_cancion)
            
    return canciones_a

def todas_canciones_artista(lista_canciones:list,artista:str)->list:
    canciones_artista=[]
    for cada_cancion in lista_canciones:
        if cada_cancion['nombre_artista']==artista:
            canciones_artista.append(cada_cancion)
    return canciones_artista

def todos_artistas_cancion(lista_canciones:list,cancion:str)->list:
    todos_a=[]
    for cada_cancion in lista_canciones:
        if cada_cancion['nombre_cancion']==cancion:
            todos_a.append(cada_cancion['nombre_artista'])
    return todos_a

def artistas_mas_populares(lista_canciones:list)->list:
    for cancion in canciones:
        artistas.add(cancion['nombre_artista'])
    diccionario_artistas = {}
    for artista in lista_artistas:
        contador = 0
    for cancion in canciones:
      if cancion['nombre_artista'] == artista:
        contador += 1
    diccionario_artistas[artista] = contador
    diccionario_artistas_filtrados = {}
    for artista, cantidad in diccionario_artistas.items():
        if cantidad >= cantidad_minima:
            diccionario_artistas_filtrados[artista] = cantidad
    return diccionario_artistas_filtrados

def artista_estrella(canciones:list)->list:
    diccionario_artistas = artistas_con_mas_canciones(canciones, 1)
    return max(diccionario_artistas, key=diccionario_artistas.get)

def artistas_y_sus_canciones(canciones:list)->list:
    diccionario_canciones_por_artista = {}
    for cancion in canciones:
        if cancion['nombre_artista'] not in diccionario_canciones_por_artista:
            diccionario_canciones_por_artista[cancion['nombre_artista']] = []
        diccionario_canciones_por_artista[cancion['nombre_artista']].append(cancion)
    return diccionario_canciones_por_artista

def promedio_canciones_por_artista(canciones:list)->list:
    cantidad_total_canciones = 0
    cantidad_total_artistas = 0
    for cancion in canciones:
        cantidad_total_canciones += 1
    if cancion['nombre_artista'] not in diccionario_canciones_por_artista:
        cantidad_total_artistas += 1
    return cantidad_total_canciones / cantidad_total_artistas