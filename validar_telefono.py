#libreria para validar numeros de telefonos
import phonenumbers


def validar_telefono(telefono_str, codigo_pais=None):
        
    try:
        #convierte a un objeto el telefono
        telefono = phonenumbers.parse(telefono_str, codigo_pais)
        return phonenumbers.is_valid_number(telefono)
    #para ver la excepcion en caso de un error
    except Exception as e:
        print("Teléfono inválido:", e)
        return False


valido = validar_telefono("3003401030", "BR")
print(valido)