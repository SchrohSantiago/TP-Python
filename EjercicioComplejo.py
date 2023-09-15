def potencia_nums():
    number_list = [2,5,4,6,2,6,7,8]

    potencia_num = [valor**2 for valor in number_list]
    return potencia_num

def lista_nombres():
    names_list = ["Santiago","Jorge","Hernan","Alan"]

    min_long = int(input("Porfavor introduzca el minimo de sus caracteres:"))

    long_num = [names for names in names_list if len(names) >= min_long]
    return long_num

def lectura_archivo():
    url = "/home/yo/Escritorio/TP3-Python/datos.txt"
    archivo = open(url, "r")

    lista_archivo = [palabra for linea in archivo for palabra in linea.split("-")]
    return lista_archivo

def dicc_defs():
    dic_palabras = {
        "Caminar": "accion que realiza una persona con el objetivo de transportarse utilizando sus piernas",
        "Alimentarse": "accion realizada por los animales ademas Insectos y Personas por la cual mediante los alimentos obtienen energia",
        "Hablar": "accion realizada por los seres humanos con el fin de comunicarse entre si"
    }

    lista_palabra = [palabra for definicion in dic_palabras.values() for palabra in definicion.split() if palabra.lower().startswith('a')]
    return lista_palabra

def num_primos(): 
    rango = range(1,101)

    list_primos = [nums for nums in rango if nums % 2 == 1 and nums % 3 != 0]
    return list_primos

def dicc_personas():

    dic_personas = {
        "juan":30,
        "jorge":45,
        "maria":23
    }
    
    edad = int(input("Ingrese la edad minima: "))

    list_edad = [name for name, edad_dic in dic_personas.items() if edad_dic > edad] # A tener en cuenta que la coma y "edad_dic" representan a el valor de los "keys" por eso utilizamos la coma "," en e list comprenshion e items envez de values.
    print(edad,list_edad)

# def pal_user():

#     contador = 0
#     salir = "salir"

    
#     while palabra_user != salir:


#         for vocales in palabra_user:
#             if vocales == "a" or vocales == "e" or vocales == "i" or vocales == "o" or vocales == "u":
#                 contador + 1

#     print(contador)
# pal_user()    