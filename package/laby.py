"""coding: utf-8"""

import pygame
from .constantes import SPRITE_SIZE


class Labyrinth:
    """Laby class used to generate the area to play within from .txt, as position of characters and objet"""
    def __init__(self):
        """initialising laby Class"""
        self._area = []
        self._mcg_pos = []
        self._gard_pos = []
        self._objets = []

    def get_area(self):
        """get the hidden area value"""
        return self._area

    def get_mcg_pos(self):
        """get the hidden mcg_pos value"""
        return self._mcg_pos

    def get_gard_pos(self):
        """get the hidden gard_pos value"""
        return self._gard_pos

    def get_objets(self):
        """get the hidden objets value"""
        return self._objets

    def pickup_objets(self, objets):
        """remove an said object from the list"""
        self._objets.remove(objets)

    def generate(self):
        """Generating tiles, wall, and guardian position from .txt file"""
        with open("Labyrinthe.txt") as generating_file:
            content = []
            for struc_y, ligne in enumerate(generating_file):
                ligne_map = []
                for struc_x, element in enumerate(ligne):
                    if element != '\n':
                        ligne_map.append(int(element))
                    if element == '3':
                        self._mcg_pos = [struc_x, struc_y]
                    if element == '4':
                        self._gard_pos = [struc_x, struc_y]
                content.append(ligne_map)
            self._area = content

    def place_objet(self, _objets):
        """generating object's logic position"""
        self._area[_objets.get_position()[0]][_objets.get_position()[1]] = 9
        self._objets.append(_objets)
        print(self._area)

    def draw(self, fenetre):
        """Draw the lab, and inventory from the .txt infos, with the determined sprite size"""
        wall = pygame.image.load("pics/brick.png").convert_alpha()
        tile = pygame.image.load("pics/grass.png").convert_alpha()
        inv_slot = pygame.image.load("pics/inv_slot.jpg").convert_alpha()

        struc_x = 0
        struc_y = 0

        for ligne in self._area:
            for element in ligne:
                element = int(element)
                if element == 1:
                    fenetre.blit(wall, (struc_x*SPRITE_SIZE, struc_y*SPRITE_SIZE))

                elif element == 6:
                    fenetre.blit(inv_slot, (struc_x*SPRITE_SIZE, struc_y*SPRITE_SIZE))

                else:
                    fenetre.blit(tile, (struc_x*SPRITE_SIZE, struc_y*SPRITE_SIZE))
                struc_x += 1

            struc_x = 0
            struc_y += 1
