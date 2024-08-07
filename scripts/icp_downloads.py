import os as OS
from dotenv import load_dotenv
import shutil
import re

load_dotenv()


def mover_y_renombrar_archivos(folio, cliente, source_folder, destination_folder):

    if not OS.path.exists(destination_folder):
        OS.makedirs(destination_folder)

    pattern = re.compile(rf".*_{folio}_.*\.(pdf|xml)$")

    for filename in OS.listdir(source_folder):
        if pattern.match(filename):
            source_file = OS.path.join(source_folder, filename)
            file_extension = OS.path.splitext(filename)[1]
            new_filename = f"{cliente}_{folio}{file_extension}"
            destination_file = OS.path.join(destination_folder, new_filename)
            shutil.move(source_file, destination_file)
            print(f"Archivo movido y renombrado: {new_filename}")


folio = "1092"
cliente = "cliente"
source_folder = OS.getenv("SOURCE_FOLDER")
destination_folder = OS.getenv("DESTINATION_FOLDER")


mover_y_renombrar_archivos(folio, cliente, source_folder, destination_folder)
