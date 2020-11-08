"""coding: utf-8"""

import random
from .constantes import SPRITE_SIZE


class Objet:
    """Objet class creating and placing objet within the lab"""
    def __init__(self, name, img, laby):
        """initialising Objet Class"""
        self._laby = laby
        self._position = self.generate_position()
        self._img = img
        self._name = name

    def get_laby(self):
        """get the hidden laby value"""
        return self._laby

    def get_position(self):
        """get the hidden position value"""
        return self._position

    def get_img(self):
        """get the hidden img value"""
        return self._img

    def get_name(self):
        """get the hidden name value"""
        return self._name

    def generate_position(self):
        """generate random objet position within the walkable tiles"""
        rand_x = random.randint(0, len(self._laby)-2)
        rand_y = random.randint(0, len(self._laby[0])-1)

        while self._laby[rand_x][rand_y] != 0:
            rand_x = random.randint(0, len(self._laby)-1)
            rand_y = random.randint(0, len(self._laby[0])-1)
        return [rand_x, rand_y]

    def draw(self, fenetre):
        """draw Objets from their position"""
        fenetre.blit(self._img, (self._position[1]*SPRITE_SIZE, self._position[0]*SPRITE_SIZE))
