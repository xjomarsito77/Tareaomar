def registro_usuario(
    dicc:dict
):
    """REGISTRAR USUARIO


    Args:
        nom (str): nombre del usuario
        tomo (str): nombre del libro
        dicc (dict): lugar donde se almacena los datos

    Returns:
        se agrega usuario
    """
    
    nom=str(input("ingrese nombre del usuario: "))
    tomo=str(input("ingrese nombre del libro: "))
    dicc[nom] = tomo
    
    
    return
    
    

        