# gui_Tkinter_2023




Para crear un ejecutable al que se le puedan agregar imágenes como proyecto es necesario tener instalados:

	python -m pip install pyinstaller
	python -m pip install auto-py-to-exe

y en el script principal myApp.py añadir esta función:


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for Pyinstaller """
    try:
        # PyInstaller creates a tem folder and sotres paht in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path,relative_path)


Posterior a esta función es necesario que todas las imágenes se alojen en un mismo directorio, ejemplo:
	Images
	Images/foto1.png
	Images/foto2.png and so on...


Además cada path de imagen debe estar contenida en la función que agregamos al inicio, así:


	image_icon = PhotoImage(file=resource_path("Images/camera.png"))

	image3 = Image.open(resource_path("Images/camera.png"))

Con esto garantizamos que el programa podrá encontrar el path correcto y podrmos crear nuestro ejecutable con la siguiente instrucción


Desde nuestro entorno virtual ejecutamos:
	auto-py-to-exe

Y elegimos el path de nuestro file.py principal
elegimos el path de nuestra carpeta Images

y al final ejecutamos la interfaz gráfica indicando crear ejecutable





