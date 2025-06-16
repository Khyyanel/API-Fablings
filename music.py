import pygame, errors

def load_music(music_path):
        try:
            music_path = "assets/music/medieval-prueba.mp3"
            pygame.mixer.music.load(music_path)
        except pygame.error as e:
            errors.music_error(music_path, e)

def play_music(loops=-1): 
    """ 
    Reproduce la música actualmente cargada.
    -1 para bucle infinito, 0 para una vez, N para N+1 veces.
    """   
    if is_music_playing(): # Si ya está sonando, detenla primero para evitar superposiciones
        pygame.mixer.music.stop()
    pygame.mixer.music.play(loops)

def set_music_volume(volume):
    #Establece el volumen de la música (entre 0.0 y 1.0).
    pygame.mixer.music.set_volume(volume)

def stop_music():
    pygame.mixer.music.stop()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    #Reanuda la reproducción de la música.
    pygame.mixer.music.unpause()

def is_music_playing():
    #Devuelve True si la música está sonando, False en caso contrario.
    return pygame.mixer.music.get_busy()