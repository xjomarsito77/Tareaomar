import acumulador
def eliminar_usuario(dato1:list,
                     dato2:list,
)->list:
    """ELIMINAR DATO DEL DICCIONARIO

    Args:
        dato1 (list): nombre del usuario
        dato2 (list): nombre del libro

    Returns:
        
    """
    print(acumulador)
    nom=input("ingrese nombre del usuario a eliminar: ")
    tomo=input("ingrese nombre del libro a eliminar : ")
    dato1.pop(nom)
    dato2.pop(tomo)
    return