def suma_recursiva(lista, pi, pf):
    if pi > pf:
        return 0
    return lista[pi - 1] + suma_recursiva(lista, pi + 1, pf)

n = int(input("Ingrese la cantidad de elementos de la lista: "))
lista = []

for i in range(n):
    lista.append(int(input(f"Ingrese el número para la posición {i+1}: ")))

pi = int(input("Ingrese la posición inicial (PI): "))
pf = int(input("Ingrese la posición final (PF): "))

resultado = suma_recursiva(lista, pi, pf)

print("Lista ingresada:", lista)
print("Resultado =", resultado)