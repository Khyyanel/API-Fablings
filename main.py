from game_manager import GameManager #importar desde el archivo game_manager.py la clase GameManager


def main():
    game = GameManager() #creamos un objeto o instancia llamada game, de la clase GameManager
    game.run() #llamamos a la función run () de game


if __name__ == "__main__": 
    main() 
    # Este bloque asegura que la función 'main()' se llame solo cuando el script se ejecuta directamente.
    # Evita que 'main()' se ejecute si este archivo es importado como un módulo en otro script.