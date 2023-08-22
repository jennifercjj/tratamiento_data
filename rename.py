import os
import shutil

def copy_images_with_prefix(original_directory, new_directory):
    prefix = "IMG_S_"
    counter = 1

    for filename in os.listdir(original_directory):
        if filename.lower().endswith(".jpg"):
            new_filename = f"{prefix}{counter}.jpg"
            old_path = os.path.join(original_directory, filename)
            new_path = os.path.join(new_directory, new_filename)
            shutil.copy(old_path, new_path)
            print(f"Se copió el archivo '{filename}' como '{new_filename}'")
            counter += 1
# Directorio que contiene las imágenes originales
original_image_directory = r"D:\data\test_dw\sana\sana_r"

# Directorio donde se almacenarán las copias de las imágenes con el nuevo nombre
new_image_directory = r"D:\data\test_dw\sana\sana_rename"

# Copiar las imágenes con el prefijo "DS_" y extensión ".jpg" al nuevo directorio
copy_images_with_prefix(original_image_directory, new_image_directory)
