import pygame

class GestorAudioInterfaz:
    def __init__(self):

        pygame.mixer.init()
        
        self.volumen = 0.3 
        self.musica_cargada = False
        
        self.sonido_click = None #Variable vacía por si falla la carga
        
        try:
            self.sonido_click = pygame.mixer.Sound("Sonido_click.mp3") 
            self.sonido_click.set_volume(0.8) #Volumen del efecto
        except Exception as e:
            print(f"No se pudo cargar el sonido de click: {e}")


        try:
            pygame.mixer.music.load("Sonido_principal.mp3")
            pygame.mixer.music.play(-1) # Loop infinito
            pygame.mixer.music.set_volume(self.volumen)
            self.musica_cargada = True
        except pygame.error:
            print("No se encontró archivo \"Sonido_principal.mp3\" de música")

    def set_volumen(self, valor_0_a_100):
        """Recibe un valor de 0 a 100 (del slider de Tkinter) y lo convierte a 0.0-1.0"""
        self.volumen = float(valor_0_a_100) / 100.0
        pygame.mixer.music.set_volume(self.volumen)
        
    def get_volumen_actual(self):
        """Devuelve el volumen actual en escala 0-100 para la interfaz"""
        return int(self.volumen * 100)
    
    def reproducir_sonido_click(self):
        """Reproduce el sonido de click si fue cargado correctamente"""
        if self.sonido_click:
            self.sonido_click.play()