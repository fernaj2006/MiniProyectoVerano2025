import pygame
import os

class GestorAudioInterfaz:
    
    def __init__(self):
        
        # Inicializamos el mixer solo si no está ya iniciado
        
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        
        #--- Variables de estado ---
        
        self.volumen = 0.3 
        self.musica_cargada = False
        self.sonido_click = None 
        
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_carpeta_audios = os.path.join(directorio_actual, "Audios")
        
        #--- Carga de Efectos de Sonido ---
        
        ruta_sonido_click = os.path.join(ruta_carpeta_audios, "Sonido_click.mp3") #Construye la ruta completa
        
        try:
            self.sonido_click = pygame.mixer.Sound(ruta_sonido_click) 
            self.sonido_click.set_volume(0.8) 
        except Exception as e:
            print(f"Advertencia: No se pudo cargar 'Sonido_click.mp3': {e}")

        # --- Carga de Música de Fondo ---
        
        ruta_sonido_principal = os.path.join(ruta_carpeta_audios, "Sonido_principal.mp3") #Construye la ruta completa
        
        try:
            pygame.mixer.music.load(ruta_sonido_principal)
            pygame.mixer.music.set_volume(self.volumen)
            pygame.mixer.music.play(-1) # Loop infinito
            self.musica_cargada = True
        except pygame.error as e:
            print(f"Advertencia: No se encontró 'Sonido_principal.mp3': {e}")

    def set_volumen(self, valor_0_a_100):
        """Convierte valor de slider (0-100) a volumen Pygame (0.0-1.0)"""
        self.volumen = float(valor_0_a_100) / 100.0
        pygame.mixer.music.set_volume(self.volumen)
        
    def get_volumen_actual(self):
        """Devuelve el volumen actual en escala 0-100 para la UI"""
        return int(self.volumen * 100)
    
    def reproducir_sonido_click(self):
        """Reproduce el sonido de click de forma segura"""
        if self.sonido_click:
            self.sonido_click.play()