import shutil
import os

source_folder = r"C:\Users\Personal\Desktop\detecciones\detecciones\redimensionado_sano"

destination_folder = r"D:\data\test_dw\sana\sana_r"


file_names = [
    "IMG_20230430_151854.jpg",
    "IMG_20230430_151945.jpg",
    "IMG_20230430_152026.jpg",
    "IMG_20230430_152119.jpg",
    "IMG_20230430_152134.jpg",
    "IMG_20230430_152154.jpg",
    "IMG_20230430_152204.jpg",
    "IMG_20230430_152215.jpg",
    "IMG_20230430_152217.jpg",
    "IMG_20230430_152316.jpg",
    "IMG_20230430_152337.jpg",
    "IMG_20230430_152339.jpg",
    "IMG_20230430_152352.jpg",
    "IMG_20230430_152440.jpg",
    "IMG_20230430_152535.jpg",
    "IMG_20230430_152632.jpg",
    "IMG_20230430_152752.jpg",
    "IMG_20230430_152812.jpg",
    "IMG_20230430_152825.jpg",
    "IMG_20230430_152903.jpg",
    "IMG_20230430_152957.jpg",
    "IMG_20230430_153426.jpg",
    "IMG_20230430_153527.jpg",
    "IMG_20230430_153630.jpg",
    "IMG_20230430_153701.jpg",
    "IMG_20230430_153856.jpg",
    "IMG_20230430_153858.jpg",
    "IMG_20230430_153951.jpg",
    "IMG_20230430_154032.jpg",
    "IMG_20230430_154155.jpg",
    "IMG_20230430_154303.jpg",
    "IMG_20230430_154359.jpg",
    "IMG_20230430_154605.jpg",
    "IMG_20230430_154821.jpg",
    "IMG_20230430_154832.jpg",
    "IMG_20230430_154902.jpg",
    "IMG_20230430_154958.jpg",
    "IMG_20230430_155015.jpg",
    "IMG_20230430_155039.jpg",
    "IMG_20230430_155106.jpg",
    "IMG_20230430_155111.jpg",
    "IMG_20230430_155144.jpg",
    "IMG_20230430_155249.jpg",
    "IMG_20230430_155336.jpg",
    "IMG_20230430_155346.jpg",
    "IMG_20230430_155439.jpg",
    "IMG_20230430_155500.jpg",
    "IMG_20230430_153451.jpg",
    "IMG_20230430_154208.jpg",
    "IMG_20230430_160023.jpg"

]

# Crear la nueva carpeta si no existe
for file_name in file_names:
    source_path = os.path.join(source_folder, file_name)
    destination_path = os.path.join(destination_folder, file_name)
    shutil.copyfile(source_path, destination_path)