import tkinter as tk
import os
import menu_seleccion_juegos
from tkinter import messagebox
from gestor_audio import GestorAudioInterfaz

class PaginaInicial(tk.Frame):
    
    def __init__(self, parent, *args, **kwargs):
        super(PaginaInicial, self).__init__(parent,bg="#132904", bd=0, highlightthickness=0, *args, **kwargs)
        self.parent = parent
        #--- Configuraciones principales de ventana ---
        
        self.parent.title("Menú Principal")
        self.parent.geometry("900x600")
        self.parent.minsize(600,500)
        self.parent.configure(background="#132904")
        
        #--- Asignamos a atributos los gestores y menús ---
        
        self.gestor_audio = GestorAudioInterfaz()
        
        ### Carga de imágenes ###

        directorio_base = os.path.dirname(__file__) #Obtiene la ruta desde donde se esta ejecutado el archivo
        ruta_logo = os.path.join(directorio_base, "Imagenes", "Logo.png") #Construye la ruta completa
        ruta_fondo = os.path.join(directorio_base, "Imagenes", "Fondo_principal.png") #Construye la ruta completa
        
        try:
            self.logo_app = tk.PhotoImage(file=ruta_logo)
            self.parent.iconphoto(True, self.logo_app)
        except Exception:
            messagebox.showwarning("Advertencia", "No se pudo cargar el icono de la aplicación")
        
        try:
            self.fondo_ventana_princpal = tk.PhotoImage(file=ruta_fondo)
        except Exception:
            messagebox.showwarning("Advertencia", "No se pudo cargar la imagen de fondo")
        
        #--- Canvas (Fondo) ---
        
        self.canvas1 = tk.Canvas(self.parent, highlightthickness=0, bg="#132904")
        self.canvas1.pack(fill = "both", expand = True)
        
        if self.fondo_ventana_princpal:
            self.id_imagen_fondo = self.canvas1.create_image(0, 0, image=self.fondo_ventana_princpal, anchor="center")
        else:
            self.id_imagen_fondo = None

        #--- Fuentes de texto ---
        
        self.fuente_principal = ("Courier New", 18, "bold")
        self.fuente_segundaria = ("Courier New", 14)
        
        #--- Frames (contetienen los botones) ---
        
        self.frame_botones = tk.Frame(self.canvas1, bg="#1e3d08", bd=15, relief=tk.RIDGE)
        
        #--- Botones ---
        
        # Boton Play
        
        self.boton_iniciador = tk.Button(self.frame_botones, 
                                         text="Play",
                                         command=self.iniciar_juego,
                                         font=self.fuente_principal,
                                         bd=10,
                                         width=10, height=2,
                                         relief=tk.SOLID)
        
        # Boton Options
        
        self.boton_opciones = tk.Button(self.frame_botones,
                                        text="Options",
                                        command=self.iniciar_opciones,
                                        font=self.fuente_segundaria,
                                        bd=10,
                                        width=10, height=2,
                                        relief=tk.SOLID)
        
        # Boton Exit
        
        self.boton_salida = tk.Button(self.frame_botones, 
                                      text="Exit",
                                      command=self.salir_aplicacion,
                                      font=self.fuente_segundaria,
                                      bd=10,
                                      width=10, height=2,
                                      relief=tk.SOLID)
        
        self.boton_iniciador.pack()
        self.boton_opciones.pack(pady=20)
        self.boton_salida.pack(pady=20)
        
        self.id_frame_botones = self.canvas1.create_window(0, 0, window=self.frame_botones, anchor="center")

        #--- Centramos los elementos al iniciar y al redimensionar ---
        
        self.canvas1.bind('<Configure>', self.centrar_elementos)
    
    # ========================================
    #            LOGICA DE BOTONES 
    # ========================================
    
    ### METODO INICIO JUEGO ###
    
    def iniciar_juego(self):
        self.gestor_audio.reproducir_sonido_click()
        
        self.parent.withdraw()
        
        ventana_juegos = tk.Toplevel(self)
        ventana_juegos.title("Selección de Juegos")
        geometria_actual = self.parent.geometry()
        ventana_juegos.geometry(geometria_actual)
        ventana_juegos.configure(bg="#132904")

        def volver_al_menu():
            geometria_al_cerrar = ventana_juegos.geometry()
            self.parent.geometry(geometria_al_cerrar)
            self.parent.deiconify() # Vuelve a mostrar el menú principal
            ventana_juegos.destroy()  
        
        ventana_juegos.protocol("WM_DELETE_WINDOW", volver_al_menu)
        
        menu = menu_seleccion_juegos.MenuSeleccionJuegos(ventana_juegos, accion_volver=volver_al_menu)
        menu.pack(fill="both", expand=True)
        
        
    ### METODO OPCIONES ###
    
    def iniciar_opciones(self):
        
        self.gestor_audio.reproducir_sonido_click()
        
        #--- Toplevel para controlar el volumen ---
        
        ventana_opciones = tk.Toplevel(self.parent)
        ventana_opciones.title("Configuración de Audio")
        ventana_opciones.geometry("400x300")
        ventana_opciones.configure(background="#1e3d08")
        ventana_opciones.grab_set()  

        # Etiqueta
        
        titulo_opcion_volumen = tk.Label(ventana_opciones, text="Volumen de la Música", 
                       font=self.fuente_segundaria, bg="#1e3d08", fg="white")
        titulo_opcion_volumen.pack(pady=20)
        
        # Barra deslizante de volumen

        barra_deslizante_volumen = tk.Scale(ventana_opciones, 
                          from_=0, to=100, 
                          orient=tk.HORIZONTAL,
                          length=300,
                          command=self.actualizar_volumen, 
                          bg="#1e3d08", fg="white", highlightthickness=0)
        
        barra_deslizante_volumen.set(self.gestor_audio.get_volumen_actual())
        barra_deslizante_volumen.pack(pady=10)

        # Boton Cerrar Opciones
        
        boton_cerrar = tk.Button(ventana_opciones, text="Volver", 
                                 command=ventana_opciones.destroy)
        boton_cerrar.pack(pady=30)

    ### METODO ACTUALIZAR VOLUMEN ###
    
    def actualizar_volumen(self, valor):
        self.gestor_audio.set_volumen(valor)
        
    ### METODO CENTRADO DE ELEMENTOS ###
    
    def centrar_elementos(self, event):
        
        # Obtenemos el nuevo ancho y alto de la ventana
        nuevo_ancho = event.width
        nuevo_alto = event.height
        
        centro_x = nuevo_ancho / 2
        centro_y = nuevo_alto / 2
        
        # Movemos la imagen de fondo al nuevo centro
        if self.id_imagen_fondo:
            self.canvas1.coords(self.id_imagen_fondo, centro_x, centro_y)
            
        # Movemos el cuadro de botones al nuevo centro
        self.canvas1.coords(self.id_frame_botones, centro_x, centro_y)
    
    #### METODO DE SALIDA ###
    
    def salir_aplicacion(self):
        self.parent.destroy()
        
if __name__ == "__main__":
    root = tk.Tk() 
    app = PaginaInicial(root)
    app.place(relwidth=1, relheight=1)
    root.mainloop()