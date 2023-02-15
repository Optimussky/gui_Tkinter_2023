# screen_recorder.py
# URL tuto: https://www.youtube.com/watch?v=lQP0pZ7rCKk&t=144s
# icons https://www.pngwing.com/es/search?q=bot%C3%B3n+Detener
import pyscreenrec
from PIL import Image
from PIL import ImageTk



# Create functions
def start_rec():
    try:

        file=Filename.get()
        rec.start_recording(str(file+".mp4"),5)
    except:
        print("Error en start record")

def pause_rec():
    try:

        rec.pause_recording()
    except:
        print("Error en pausa recording")

def resume_rec():
    try:

        rec.resume_recording()
    except:
        print("Error en resume recording")

def stop_rec():
    try:

        rec.stop_recording()
    except:
        print("Error en stop recording")



# start recording
rec = pyscreenrec.ScreenRecorder()

# data images =  W:234, Height=284 Resolution=72
#icon


# background images

# Heading
"""
    Screen Recorder SSC

"""


# Entry


opcion = [1,2,3,4]
menu = """
    Elija una opción:

[1] Opción 1 Empezar a grabar
[2] Opción 2 pausar la grabación
[3] Opción 3 Reanudar la grabación
[4] Opción 4 Detener la grabación
[0] Salir
"""

FileName = "Nuevo_video"
op = ""
while op != '0':
    print("\n",menu)
    op = input("\n\Opción elegida: ")
    if op == '1':
        print("Has elegido Iniciar la grabación")

        Filename = input("Escriba el Nombre de su video: ")
        op = input("\n\Opción elegida: ")
    elif op == '2':
        print("Has elegido pausar la grabación")
        op = input("\n\Opción elegida: ")
    elif op == '3':
        print("Has elegido reanudar la grabación")
        op = input("\n\Opción elegida: ")
    elif op == '4':
        print("Has elegido Detener la grabación")
        op = input("\n\Opción elegida: ")
    elif op !=opcion and op!='0':
        print("\tLa respuesta no está entre las opciones")
    else:
        os.system("cls")
        print("\t\n\n\n\n\n\n\n\n\n\n\nHas elegido SALIR ")
        print("\n\n\tDesigned by: \n\t\t®Alberto Romero™ - DDS - CDMX - January-2023\n\n\n")
        input("""   \t\n\n\nPresione Enter para salir...""")
        break
    break
