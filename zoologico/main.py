from utils import (
    cargar_csv_a_dict, 
    guardar_dict_a_csv, 
    listar_por_clase, 
    listar_por_caracteristica, 
    obtener_lista_caracteristicas
)

def menu():
    animales = cargar_csv_a_dict('zoo.csv', 'nombre_animal')
    clases = cargar_csv_a_dict('clases.csv', 'Clase_id')

    while True:
        print("\n" + "="*30)
        print("   SISTEMA DE GESTIÓN ZOO")
        print("="*30)
        print("1. Listar por Clasificación")
        print("2. Listar por Característica")
        print("3. Agregar nuevo animal")
        print("4. Salir y Guardar")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            print("\n--- Clasificaciones Disponibles ---")
            for cid, info in clases.items():
                print(f"[{cid}] {info['Clase_tipo']}")
            seleccion = input("\nIngrese el ID de la clasificación: ")
            resultados = listar_por_clase(animales, seleccion)
            for ani in resultados: print(f" • {ani}")

        elif opcion == "2":
            caracteristicas = obtener_lista_caracteristicas(animales)
            print("\n--- Características ---")
            for i, nombre in enumerate(caracteristicas, 1):
                print(f"- {nombre.ljust(15)}", end="\t" if i % 3 != 0 else "\n")
            
            seleccion = input("\nEscriba la característica: ").lower().strip()
            if seleccion in caracteristicas:
                resultados = listar_por_caracteristica(animales, seleccion)
                for ani in resultados: print(f" • {ani}")

        elif opcion == "3":
            nombre = input("\nNombre del nuevo animal: ").lower().strip()
            if nombre in animales:
                print("Ese animal ya existe.")
                continue
            
            # 1. Crear el diccionario vacío basado en las columnas existentes
            nuevo_animal = {k: '0' for k in next(iter(animales.values())).keys()}
            nuevo_animal['nombre_animal'] = f'"{nombre}"'
            
            # 2. Preguntar la Clase
            print("\nID de Clase (1-7):")
            for cid, info in clases.items(): print(f"{cid}: {info['Clase_tipo']}")
            nuevo_animal['clase'] = input("Selección: ")

            # 3. Preguntar las Patas (es un número, no 0/1)
            nuevo_animal['patas'] = input("¿Cuántas patas tiene?: ")

            # 4. Bucle para todas las características 0/1
            print("\nResponda con 1 (SÍ) o 0 (NO):")
            caracteristicas = obtener_lista_caracteristicas(animales)
            
            for carac in caracteristicas:
                while True:
                    valor = input(f"¿Tiene {carac}?: ")
                    if valor in ['0', '1']:
                        nuevo_animal[carac] = valor
                        break
                    print("Por favor, ingrese solo 0 o 1.")

            animales[nombre] = nuevo_animal
            print(f"\n¡{nombre.upper()} ha sido agregado exitosamente!")

        elif opcion == "4":
            guardar_dict_a_csv('zoo.csv', animales)
            print("Datos guardados. ¡Adiós!")
            break

if __name__ == "__main__":
    menu()