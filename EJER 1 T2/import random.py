import random

def obtener_min_max_mult3(arreglo, indice=0, min_val=float('inf'), max_val=float('-inf')):
    if indice == len(arreglo):
        return min_val, max_val
    
    numero_actual = arreglo[indice]
    
    if numero_actual % 3 == 0:
        if numero_actual < min_val:
            min_val = numero_actual
        if numero_actual > max_val:
            max_val = numero_actual
            
    return obtener_min_max_mult3(arreglo, indice + 1, min_val, max_val)

def main():
    arreglo_ejemplo = [5, 6, 10, 9, 12, 14]
    print(f"--- PRUEBA DEL EJEMPLO ---")
    print(f"Arreglo: {arreglo_ejemplo}")
    min_ej, max_ej = obtener_min_max_mult3(arreglo_ejemplo)
    print(f"Resultado = ({max_ej} + {min_ej}) / 2 = {(max_ej + min_ej) / 2}\n")

    print("--- PROGRAMA PRINCIPAL ---")
    try:
        n = int(input("Ingrese el tamaño del arreglo: "))
        
        if n <= 0:
            print("El tamaño debe ser mayor a cero.")
            return

        arreglo_aleatorio = [random.randint(10, 9999) for _ in range(n)]
        print(f"Arreglo generado: {arreglo_aleatorio}")

        min_encontrado, max_encontrado = obtener_min_max_mult3(arreglo_aleatorio)

        if min_encontrado != float('inf'):
            promedio = (min_encontrado + max_encontrado) / 2
            print(f"El mínimo múltiplo de 3 encontrado es: {min_encontrado}")
            print(f"El máximo múltiplo de 3 encontrado es: {max_encontrado}")
            print(f"El promedio es: {promedio}")
        else:
            print("No se generaron números que sean múltiplos de 3 en el arreglo.")
            
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

main()