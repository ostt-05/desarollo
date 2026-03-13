import csv
import os

class Animal:
    def __init__(self, datos_dict):
        for clave, valor in datos_dict.items():
            if clave != 'nombre_animal':
                try:
                    setattr(self, clave, int(valor))
                except ValueError:
                    setattr(self, clave, valor)
            else:
                setattr(self, clave, valor)

    def __str__(self):
        return f"Animal: {self.nombre_animal.capitalize()} (Clase ID: {self.clase})"

def cargar_csv_a_dict(nombre_archivo, llave_primaria):
    datos = {}
    if not os.path.exists(nombre_archivo):
        return {}
    
    with open(nombre_archivo, mode='r', encoding='utf-8-sig') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            llave = fila[llave_primaria].strip('"').strip()
            datos[llave] = fila
    return datos

def guardar_dict_a_csv(nombre_archivo, datos_dict):
    if not datos_dict: return
    columnas = list(next(iter(datos_dict.values())).keys())
    with open(nombre_archivo, mode='w', encoding='utf-8', newline='') as f:
        escritor = csv.DictWriter(f, fieldnames=columnas)
        escritor.writeheader()
        for registro in datos_dict.values():
            escritor.writerow(registro)

def listar_por_clase(animales, clase_id):
    return [Animal(a) for a in animales.values() if str(a['clase']) == str(clase_id)]

def listar_por_caracteristica(animales, caracteristica):
    return [Animal(a) for a in animales.values() if a.get(caracteristica) == '1']

def obtener_lista_caracteristicas(animales):
    """Extrae las columnas que son características (excluyendo nombre, clase y patas)."""
    if not animales: return []
    primer_registro = next(iter(animales.values()))
    excluir = ['nombre_animal', 'clase', 'patas']
    return [col for col in primer_registro.keys() if col not in excluir]