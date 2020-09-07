# coding: utf-8

from Constantes import SPRITE_SIZE
import random


class Objet:
    """initialising Objet Class"""
    def __init__(self, name, img, laby):
        self.laby = laby
        self.position = self.generate_position()
        self.img = img
        self.name = name

    """generate random objet position within the walkable tiles"""
    def generate_position(self):
        rand_x = random.randint(0, len(self.laby)-2)
        rand_y = random.randint(0, len(self.laby[0])-1)

        while self.laby[rand_x][rand_y] != 0:
            rand_x = random.randint(0, len(self.laby)-1)
            rand_y = random.randint(0, len(self.laby)-1)
        return [rand_x, rand_y]

    """draw Objets from their position"""
    def draw(self, fenetre):
        fenetre.blit(self.img, (self.position[1]*SPRITE_SIZE, self.position[0]*SPRITE_SIZE))
