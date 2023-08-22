import shutil
import os
# Lista de nombres de archivos de imágenes
nombres_archivos = [
    'DSC06574.jpg', 'DSC06575.jpg', 'DSC06670.jpg', 'DSC06677.jpg', 'DSC06694.jpg',
    'IMG_20230520_114306.jpg', 'IMG_20230520_115048.jpg', 'IMG_20230520_115248.jpg',
    'IMG_20230520_121641.jpg', 'IMG_20230520_121646.jpg', 'IMG_20230520_122716.jpg',
    'IMG_20230520_122746.jpg', 'IMG_20230520_123609.jpg', 'IMG_20230520_123728.jpg',
    'IMG_20230520_124720.jpg', 'IMG_20230520_125906.jpg', 'IMG_20230520_130111.jpg',
    'IMG_20230520_130519.jpg', 'IMG_20230520_131338.jpg', 'IMG_20230520_131608.jpg',
    'IMG_20230520_132234.jpg', 'IMG_20230520_132552.jpg', 'IMG_20230520_132634.jpg',
    'IMG_20230520_133557.jpg', 'IMG_20230520_133609.jpg', 'IMG_20230520_134914.jpg',
    'IMG_20230520_134916.jpg', 'IMG_20230520_135346.jpg', 'IMG_20230520_135421.jpg',
    'IMG_20230520_135433.jpg', 'IMG_20230520_142114.jpg', 'IMG_20230520_142201.jpg',
    'IMG_20230520_142654.jpg', 'IMG_20230520_142656.jpg', 'IMG_20230520_142812.jpg',
    'IMG_20230520_143221.jpg', 'IMG_20230520_143311.jpg', 'IMG_20230520_143535.jpg',
    'IMG_20230520_143722.jpg'
]

# Ruta de la carpeta de origen
ruta_origen = r'D:\data\prueba'

# Ruta de la carpeta de destino
ruta_destino = r'D:\data\prueba_cortar'
for nombre_archivo in nombres_archivos:
    ruta_archivo_origen = os.path.join(ruta_origen, nombre_archivo)
    ruta_archivo_destino = os.path.join(ruta_destino, nombre_archivo)
    shutil.move(ruta_archivo_origen, ruta_archivo_destino)

print('Archivos cortados y movidos con éxito.')


