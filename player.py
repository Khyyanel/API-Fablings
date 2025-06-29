import pygame, constants, ui, errors

class Player():
    def __init__(self, name, character_image_path):
        self.name = name

        #CARACTERÍSTICAS
        self.stadistics = {
             "pericia": 0, 
             "supervivencia": 0,
             "conocimiento": 0, 
             "suerte": 0
        }
        self.items = []
        self.health = 3
        
        #IMAGENES
        #Diccionario imágenes
        self.images = {
            "character": { #key = llave
                "path": character_image_path, #datos - data para ubicación de imagen
                "image_loaded": None,  #datos - data para imagen cargada para pygame
                "x": constants.PLAYER_X,
                "y": constants.PLAYER_Y, 
                "width": constants.PLAYER_WIDTH, 
                "height": constants.PLAYER_HEIGHT
            },
            "pericia": {
                "path": "assets/img/pericia.png",
                "image_loaded": None,
                "x": constants.STADISTIC_FIRST_X,
                "y": constants.STADISTIC_FIRST_Y,
                "width": constants.STADISTIC_WIDTH,
                "height": constants.STADISTIC_HEIGHT
            },
            "suerte": {
                "path": "assets/img/suerte.png",
                "image_loaded": None,
                "x": constants.STADISTIC_FIRST_X + 50,
                "y": constants.STADISTIC_FIRST_Y,
                "width": constants.STADISTIC_WIDTH,
                "height": constants.STADISTIC_HEIGHT
            },
            "supervivencia": {
                "path": "assets/img/supervivencia.png",
                "image_loaded": None,
                "x": constants.STADISTIC_FIRST_X + 100,
                "y": constants.STADISTIC_FIRST_Y,
                "width": constants.STADISTIC_WIDTH,
                "height": constants.STADISTIC_HEIGHT
            },
            "conocimiento": {
                "path": "assets/img/conocimiento.png",
                "image_loaded": None,
                "x": constants.STADISTIC_FIRST_X + 150,
                "y": constants.STADISTIC_FIRST_Y,
                "width": constants.STADISTIC_WIDTH,
                "height": constants.STADISTIC_HEIGHT
            }, 
            "health":
            {
                "path": "assets/img/heart.png",
                "image_loaded": None,
                "x": constants.HEART_FIRST_X,
                "y": constants.HEART_FIRST_Y,
                "width": constants.HEART_WIDTH,
                "height": constants.HEART_HEIGHT, 
                "show": True
            }
        }

        self.set_stadistics() #llamamos a una función en el constructor de la clase 


    def set_stadistics(self):
        if self.name == "personaje1":
            self.stadistics["pericia"] = 1
            self.stadistics["suerte"] = 2
            self.stadistics["supervivencia"] = 3
            self.stadistics["conocimiento"] = 4

        elif self.name == "personaje2":
            self.stadistics["pericia"] = 4
            self.stadistics["suerte"] = 3
            self.stadistics["supervivencia"] = 2
            self.stadistics["conocimiento"] = 1

        elif self.name == "personaje3":
            self.stadistics["pericia"] = 2
            self.stadistics["suerte"] = 2
            self.stadistics["supervivencia"] = 2
            self.stadistics["conocimiento"] = 2


    def load_images(self):
        #Aunque no usamos el image_name explícitamente en el código, es necesario ponerlo. 
         #Así pygame primero elige una imagen y después mira los datos que tiene dentro
        for image_name, image_info in self.images.items():                                      
            image_path = image_info["path"]

            try:
                image_to_load = pygame.image.load(image_path).convert_alpha()
                image_info["image_loaded"] = pygame.transform.scale(image_to_load, (image_info["width"], image_info["height"])) #le damos el tamaño a la imagen
                    #shape = self.image.get_rect(center=(self.x, self.y)) 

            except pygame.error as e:
                errors.img_error()
      

    def draw(self, screen: pygame.Surface):
        self.load_images() #cargamos todas las imagenes en el diccionario 

        for image_name, image_info in self.images.items():
            if image_info["image_loaded"] is not None:
                screen.blit(image_info["image_loaded"], (image_info["x"], image_info["y"])) #después las dibujamos
            else:
                errors.img_error(image_name)

        self.draw_health(screen)
        self.show_number_stadistics(screen)


    def draw_health(self, screen):
        heart_image = self.images["health"]["image_loaded"]
        heart_x = self.images["health"]["x"]
        heart_y = self.images["health"]["y"]
        x_offset = 40

        if self.health == 3:
           screen.blit(heart_image, (heart_x + x_offset, heart_y))
           screen.blit(heart_image, (heart_x + x_offset*2, heart_y))
        
        elif self.health == 2:
           screen.blit(heart_image, (heart_x + x_offset, heart_y))

    def show_number_stadistics(self, screen):
        x_offset = 50
        for name, value in self.stadistics.items():  
            text_stadistics = ui.font_stadistics.render(str(value), True, 0) 
            #El valor de value es un int - número entero (Por ejemplo, self.stadistics["pericia"] = 1)
            #Entonces, para escribir el texto, necesitamos que ese valor entero sea una cadena de texto
            #Por eso convertirmos de int a str (string - texto) con str(value)

            #Posición en X de dónde se muestra el número de la estadística
            if name == "pericia":
                x = constants.TEXT_STADISTICS_X
            elif name == "suerte":
                x = constants.TEXT_STADISTICS_X + x_offset 
            elif name == "supervivencia":
                x = constants.TEXT_STADISTICS_X + x_offset*2
            elif name == "conocimiento":
                x = constants.TEXT_STADISTICS_X + x_offset*3
                
                
            screen.blit(text_stadistics, (x, constants.TEXT_STADISTICS_Y)) #Dibujamos el número

    def get_current_stadistic(self,stadistic):
        stadistica = self.stadistics[stadistic]
        return stadistica

