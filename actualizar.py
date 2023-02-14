def actualizar_usuario(
    dicc:dict
    
):
    """ACTUALIZAR DATO DEL DICCIONARIO

    Args:
        dicc (dict) : lugar donde se almacena la informacion
        antius(str): usuario antiguo
        newus(str): usuario nuevo
        libro(str): nuevo libro 

    Returns:
        actualiza usuario
    """
    
    antius=str(input("ingrese nombre del usuario antiguo: "))
    newus=str(input("ingrese el nuevo usuario: "))
    libro=str(input("ingrese el nuevo libro: "))
    dicc[newus]= libro
    dicc.pop(antius)
    return
    
    
    
    
    
    
   
        