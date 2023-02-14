def eliminar_usuario(
    dicc:dict
)->dict:
    """ELIMINAR DATO DEL DICCIONARIO

    Args:
        dicc (dict): lugar donde se almacena los datos
        nom (str): el nombre que va a ser eliminado

    Returns:
        elimina usuario
    """
    
    nom=input("ingrese nombre del usuario a eliminar: ")
    dicc.pop(nom)
    
    return