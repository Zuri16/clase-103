from distutils.command.build_scripts import first_line_re
import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "INGRESA LA RUTA DE LA CARPETA DESCARGAS (UTILIZA " / ") en VSC"
# to_dir = "INGRESA LA RUTA DE LA CARPETA DESTINO(UTILIZA " / ") en VSC"

from_dir = r"C:/Users/malak/Downloads"
to_dir = r"C:/Users/malak/Downloads"

# variable tipo objeto que guarda todas las extenciones que vamos a usar
dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Clase event handler 
#clase que administra los eventos(crear, modificar, mover, eliminar)
class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        name_extencion=os.path.splitext(event.src_path)
        for key,value in dir_tree.items():
            if name_extencion[1] in key:
                file_name=os.path.basename(event.src_path)
                print("descargando..." + file_name)
                ruta1=from_dir+"/"+file_name
                ruta2=to_dir+"/"+key
                ruta3=to_dir+"/"+key+"/"+file_name
                #exists checa si existe el directorio o la ruta
                if(os.path.exists(ruta2)):
                    print("moviendo"+file_name)
                    shutil.move(ruta1,ruta3)
                    time.sleep(1)
                else:
                    os.makedirs(ruta2)
                    print("moviendo"+file_name)
                    shutil.move(ruta1,ruta3)  
                    time.sleep(1)      

# Inicia la clase event handler
event_handler = FileMovementHandler()


# Inicia Observer
observer = Observer()

# Programa Observer (objeto a observar, la ruta del objeto, que observe todos los directorios)
observer.schedule(event_handler, from_dir, recursive=True)


# Inicia Observer
observer.start()

# la condicion true significa que se esta ejecutando todo el programa, y mientras se ejecuta se imprime el("ejecutando")
try:
  while True:
     time.sleep(2)
     print("ejecutando...")
except KeyboardInterrupt:
    print("error")
    observer.stop()

    
