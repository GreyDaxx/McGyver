"""
importing all the necessary modules
"""
import time
import random
import pygame

from Character import Character
from Objet import Objet
from Laby import Labyrinth


pygame.init()
IN_PROGRESS = True

"""setting the window size"""
fenetre = pygame.display.set_mode((480, 512), pygame.RESIZABLE)
win = pygame.image.load("Win.jpg")


"""initialising the lab, McGyver's and the guardian's position, logic and graphic"""
laby = Labyrinth()
laby.generate()
laby.draw(fenetre)

mcgyver = Character(laby.mcg_pos, pygame.image.load("MacGyver.png").convert_alpha(), laby.area)
mcgyver.draw(fenetre)
gardien = Character(laby.gard_pos, pygame.image.load("Gardien.png").convert_alpha(), laby.area)
gardien.draw(fenetre)

mushroom = Objet("mushroom", pygame.image.load("Shroom32.png").convert_alpha(), laby.area)
mushroom.draw(fenetre)
crowbar = Objet("crowbar", pygame.image.load("crowbar.png").convert_alpha(), laby.area)
crowbar.draw(fenetre)
seringe = Objet("seringe", pygame.image.load("seringe.png").convert_alpha(), laby.area)
seringe.draw(fenetre)
laby.place_objet(mushroom)
laby.place_objet(crowbar)
laby.place_objet(seringe)

pygame.display.flip()


CONTINUER = 1
while True:
    if CONTINUER != 0:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                CONTINUER == 0

            if event.type == pygame.KEYDOWN:
                """selecting the direction of McGyver, from the input"""

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    mcgyver.deplacement([0, -1])
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    mcgyver.deplacement([0, 1])
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    mcgyver.deplacement([-1, 0])
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    mcgyver.deplacement([1, 0])

                laby.draw(fenetre)
                mushroom.draw(fenetre)
                crowbar.draw(fenetre)
                seringe.draw(fenetre)
                gardien.draw(fenetre)
                mcgyver.draw(fenetre)
                mcgyver.update_map(laby.area)
                pygame.display.flip()


            #if McGyver has all 3 Objets and have the same position as the guardian, you win
            if mcgyver.position[0] == gardien.position[0] and mcgyver.position[1] == gardien.position[1]:
                if inventory == 3:
                    print("bravo vous etes sorti du labyrinthe, appuyez sur R pour recommencer ou ")

