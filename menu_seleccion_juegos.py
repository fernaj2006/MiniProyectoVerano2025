import tkinter as tk
from gestor_audio import GestorAudioInterfaz

class MenuSeleccionJuegos(tk.Frame):
    def __init__(self, parent, accion_volver, *args, **kwargs): 
        super(MenuSeleccionJuegos, self).__init__(parent, bg="#1e3d08", *args, **kwargs)
        self.parent = parent  
        self.accion_volver = accion_volver
        
        self.gestor_audio = GestorAudioInterfaz()
        
        #--- Fuentes de texto ---
        
        self.fuente_principal = ("Courier New", 18, "bold")
        self.fuente_segundaria = ("Courier New", 14)
        
        self.frame_juegos = tk.Frame(self, bg="#1e3d08", bd=15, relief=tk.RIDGE)
        self.frame_juegos.pack(expand=True)
        
        self.boton_juego1 = tk.Button(self.frame_juegos, 
                                      text="Juego 1",
                                      command=self.iniciar_juego_uno,
                                      font=self.fuente_principal,
                                      bd=10,
                                      width=15, height=2,
                                      relief=tk.SOLID)
        
        self.volver_pagina_principal = tk.Button(self.frame_juegos,
                                                 text="Volver",
                                                 command=self.volver_al_menu_principal,
                                                 font=self.fuente_segundaria,
                                                 bd=10,
                                                 width=10, height=2,
                                                 relief=tk.SOLID)
                                                 
        
        self.boton_juego1.pack()
        self.volver_pagina_principal.pack(pady=20)
        self.pack(fill = "both", expand = True)

        
    def iniciar_juego_uno(self):        
        self.gestor_audio.reproducir_sonido_click()
    
    def volver_al_menu_principal(self):
        self.gestor_audio.reproducir_sonido_click()
        self.accion_volver()
        
        


if __name__ == "__main__":
    root = tk.Tk()
    MenuSeleccionJuegos(root).pack(side="top", fill="both", expand=True)
    root.geometry("800x600")
    root.mainloop()