# README

## Descripción
Este programa en **Python** lee líneas de texto desde la **entrada estándar (`stdin`)**.  
Cada línea contiene números separados por comas. El programa limpia cada valor eliminando caracteres no válidos, convierte los valores a números enteros y calcula **la suma de los números de cada línea**.

El resultado de cada línea se imprime en pantalla.

## Funcionamiento
1. El programa lee cada línea desde `stdin`.
2. Se separan los valores usando la coma `,`.
3. Cada valor se limpia eliminando caracteres que no sean números, punto o signo negativo.
4. Los valores se convierten a números enteros.
5. Se suman todos los números de la línea.
6. Se imprime el resultado.

## Ejemplo

### Entrada
```
10,20,30
5.5,4.3,1
100abc,50,-20
```

### Salida
```
60
10
130
```

## Ejecución

```bash
python programa.py < datos.txt
```

También se puede ejecutar el programa y escribir los datos directamente desde el teclado.

## Autor
**Oswaldo Jafet Morales Flores**