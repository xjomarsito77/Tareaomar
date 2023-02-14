def leer_usuario(
    diccionario:dict
)->dict:
    """VISUALIZAR DATOS

    Args:
        dato1 (list): nombre del usuario
        dato2 (list): nombre del libro

    Returns:
        lee usuario
    """
    for i,j in diccionario.items():
        print ('[',i, ' => ', j,']')
        
    
    
        