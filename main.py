def Menu():
    print("--- MENU ---")
    print("1. Ingresar Estudiantes")
    print("2. Ver estudiantes")
    print("3. Salir")

def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores)+iguales+quick_sort(mayores)

estudiantes = []

while True:
    Menu()
    try:
        opcion = int(input("Ingrese una opcion: "))
        match opcion:
            case 1:
                print("Ingresando Estudiantes")
                cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes que desea ingresar: "))
                for estudiante in range(cantidad_estudiantes):
                    estudiantes.append(input(f"Ingrese el nombre del estudiante #{estudiante + 1}: "))
            case 2:
                print("Lista de Estudiantes")
                resultado = quick_sort(estudiantes)
                print(resultado)
            case 3:
                print("Gracias por utilizar el programa")
                break
            case _:
                print("Opcion no valida")
    except Exception:
        print("La opcion debe ser numerica")