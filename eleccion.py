import os

# Ruta de la carpeta A (contiene los nombres de archivos a comparar)
carpeta_A = r'D:\data\prueba_d_W'

# Ruta de la carpeta B (donde se encuentran las imágenes)
carpeta_B = r'D:\data\seleccion_dataset360Original'

# Obtener los nombres de archivos de la carpeta A
nombres_archivos_A = os.listdir(carpeta_A)

# Obtener los nombres de archivos de la carpeta B
nombres_archivos_B = os.listdir(carpeta_B)

# Comparar los nombres de archivos
hay_coincidencias = False

# Comparar los nombres de archivos
for nombre_archivo in nombres_archivos_A:
    if nombre_archivo in nombres_archivos_B:
        print(f"El archivo {nombre_archivo} se encuentra en la carpeta B.")
        hay_coincidencias = True

# Si no hay coincidencias, imprimir "No hay"
if not hay_coincidencias:
    print("No hay coincidencias.")