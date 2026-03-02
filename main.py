import sys 

def limpiar_valor(valor):
    valor = valor.strip() #eliminando los espacios a los costados
    caracteres_validos= '0123456789.-'  
    resultado =''
    for char in valor:
        if char in caracteres_validos:   #Eliminando caracteres no validos 
            resultado+=char
    return resultado


def convertir_a_entero(valor):
    if not valor:
        return 0
    try:
        numero = float(valor)
        return int(numero)
    except ValueError:
        return 0


def procesar_linea(linea):
    resultado = 0
    linea = linea.strip()
    linea = linea.split(",")
    for valor in linea:
        valor = limpiar_valor(valor) #limpiando cada valor de la linea
        numero = convertir_a_entero(valor) #Convirtiendo a enteros todos los valores de la linea
        resultado += numero  #sumando cada valor al resultado
    return resultado
    


def main():
    for linea in sys.stdin:
        resultado = procesar_linea(linea)
        print(resultado)



if __name__ == "__main__":
    main()