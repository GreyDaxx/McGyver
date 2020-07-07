import pygame
from Constantes import SPRITE_SIZE


class Labyrinth:
    """initialising laby Class"""
    def __init__(self):
        self.area = []
        self.mcg_pos = []
        self.gard_pos = []
        self.objets = []

    """Generating tiles, wall, and guardian position from .txt file"""
    def generate(self):
        with open("Labyrinthe.txt") as generating_file:
            content = []
            for struc_y, ligne in enumerate(generating_file):
                ligne_map = []
                for struc_x, element in enumerate(ligne):
                    if element != '\n':
                        ligne_map.append(int(element))
                    if element == '3':
                        self.mcg_pos = [struc_x, struc_y]
                    if element == '4':
                        self.gard_pos = [struc_x, struc_y]
                content.append(ligne_map)
            self.area = content

    """generating objet's logic position"""
    def place_objet(self,objet):
        self.area[objet.position [0]][objet.position[1]] = 9
        self.objets.append(objet)
        print(self.area)

    """Draw the lab, and inventory from the .txt infos, with the determined sprite size"""
    def draw(self, fenetre):
        wall = pygame.image.load("brick.png").convert_alpha()
        tile = pygame.image.load("grass.png").convert_alpha()
        inv_slot = pygame.image.load("inv_slot.jpg").convert_alpha()

        struc_x = 0
        struc_y = 0

        for ligne in self.area:
            for element in ligne:
                element = int(element)
                if element == 1:
                    fenetre.blit(wall,(struc_x*SPRITE_SIZE,struc_y*SPRITE_SIZE))

                elif element == 6:
                    fenetre.blit(inv_slot,(struc_x*SPRITE_SIZE, struc_y*SPRITE_SIZE))

                else:
                    fenetre.blit(tile,(struc_x*SPRITE_SIZE,struc_y*SPRITE_SIZE))
                struc_x += 1

            struc_x = 0
            struc_y +=1