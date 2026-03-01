import sys 


def procesar_linea(linea):
    resultado =0
    linea = linea.strip()
    linea = linea.split(",")
    for valor in range(len(linea)):
        resultado+=valor
    
    return resultado
        




def main():
    for linea in sys.stdin:
        resultado = procesar_linea(linea)
        print(resultado)
    
if __name__ == "__main__":
    main()