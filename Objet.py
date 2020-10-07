# coding: utf-8

from Constantes import SPRITE_SIZE
import random


class Objet:
    """initialising Objet Class"""
    def __init__(self, name, img, laby):
        self._laby = laby
        self._position = self.generate_position()
        self._img = img
        self._name = name

    def get_laby(self):
        return self._laby

    def get_position(self):
        return self._position
    
    def get_img(self):
        return self._img
    
    def get_name(self):
        return self._name

    """generate random objet position within the walkable tiles"""
    def generate_position(self):
        rand_x = random.randint(0, len(self._laby)-2)
        rand_y = random.randint(0, len(self._laby[0])-1)

        while self._laby[rand_x][rand_y] != 0:
            rand_x = random.randint(0, len(self._laby)-1)
            rand_y = random.randint(0, len(self._laby[0])-1)
        return [rand_x, rand_y]

    """draw Objets from their position"""
    def draw(self, fenetre):
        fenetre.blit(self._img, (self._position[1]*SPRITE_SIZE, self._position[0]*SPRITE_SIZE))
