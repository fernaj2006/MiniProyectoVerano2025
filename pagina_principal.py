import tkinter as tk
from tkinter import ttk

from gestor_audio import GestorAudioInterfaz

class PaginaInicial():
    
    def __init__(self):
        
        self.gestor_audio = GestorAudioInterfaz()
        
        """Configuraciones principales de ventana"""
        
        self.ventana_inicio = tk.Tk()
        self.ventana_inicio.title("Menú Principal")
        self.ventana_inicio.geometry("1000x800")
        self.ventana_inicio.minsize(600,500)
        self.ventana_inicio.configure(background="#132904")

        self.logo_app = tk.PhotoImage(file='Logo.png')
        self.ventana_inicio.iconphoto(True, self.logo_app)

        """Fuentes"""
        
        self.fuente_principal = ("Courier New", 18, "bold")
        self.fuente_segundaria = ("Courier New", 14)
        
        """Boton Play"""
        
        self.boton_iniciador = tk.Button(text="Play",
                                         command=self.iniciar_juego,
                                         font=self.fuente_principal,
                                         bd=10,
                                         width=10, 
                                         height=2,
                                         relief=tk.SOLID)
        
        """Boton Options"""
        
        self.boton_opciones = tk.Button(text="Options",
                                        command=self.iniciar_opciones,
                                        font=self.fuente_segundaria,
                                        bd=10,
                                        width=10, 
                                        height=2,
                                        relief=tk.SOLID)
        
        """Boton Exit"""
        
        self.boton_salida = tk.Button(text="Exit",
                                      command=self.salir_aplicacion,
                                      font=self.fuente_segundaria,
                                      bd=10,
                                      width=10, 
                                      height=2,
                                      relief=tk.SOLID)
        
        
        self.boton_iniciador.pack()
        self.boton_opciones.pack(pady=20)
        self.boton_salida.pack(pady=20)
        
        self.ventana_inicio.mainloop()
    
    # ========================================
    #            LOGICA DE BOTONES 
    # ========================================
    
    ### METODO INICIO JUEGO ###
    
    def iniciar_juego(self):
        self.gestor_audio.reproducir_sonido_click()
        pass
    
    ### METODO OPCIONES ###
    
    def iniciar_opciones(self):
        
        self.gestor_audio.reproducir_sonido_click()
        
        """Toplevel para controlar el volumen"""
        
        ventana_opciones = tk.Toplevel(self.ventana_inicio)
        ventana_opciones.title("Configuración de Audio")
        ventana_opciones.geometry("400x300")
        ventana_opciones.configure(background="#1e3d08")
        ventana_opciones.grab_set()  

        """Etiqueta"""
        lbl = tk.Label(ventana_opciones, text="Volumen de la Música", 
                       font=self.fuente_segundaria, bg="#1e3d08", fg="white")
        lbl.pack(pady=20)

        slider = tk.Scale(ventana_opciones, 
                          from_=0, to=100, 
                          orient=tk.HORIZONTAL,
                          length=300,
                          command=self.actualizar_volumen, 
                          bg="#1e3d08", fg="white", highlightthickness=0)
        
        slider.set(self.gestor_audio.get_volumen_actual())
        slider.pack(pady=10)

        """Boton Cerrar Opciones"""
        boton_cerrar = tk.Button(ventana_opciones, text="Volver", command=ventana_opciones.destroy)
        boton_cerrar.pack(pady=30)

    def actualizar_volumen(self, valor):
        """Esta funcion es llamada automáticamente por el Slider"""
        self.gestor_audio.set_volumen(valor)
    
    #### METODO DE SALIDA ###
    
    def salir_aplicacion(self):
        
        self.gestor_audio.reproducir_sonido_click()
        
        self.ventana_inicio.destroy()
        

if __name__ == "__main__":
    PaginaInicial()
