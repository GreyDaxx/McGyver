"""coding: utf-8"""

# importing all the necessary modules
import pygame

from package import character
from package import objet
from package import laby

if __name__ == "__main__":

    pygame.init()
    IN_PROGRESS = True

    # setting the window size
    fenetre = pygame.display.set_mode((480, 512), pygame.RESIZABLE)
    win = pygame.image.load("pics/Win.png")
    lose = pygame.image.load("pics/lose.jpg")

    # initialising the lab, McGyver's and the guardian's position, logic and graphic
    lab = laby.Labyrinth()
    lab.generate()
    lab.draw(fenetre)

    mcgyver = character.Character(
        lab.get_mcg_pos(), pygame.image.load("pics/MacGyver.png").convert_alpha(), lab
    )
    mcgyver.draw(fenetre)
    gardien = character.Character(
        lab.get_gard_pos(), pygame.image.load("pics/Gardien.png").convert_alpha(), lab
    )
    gardien.draw(fenetre)

    mushroom = objet.Objet(
        "mushroom",
        pygame.image.load("pics/Shroom32.png").convert_alpha(),
        lab.get_area(),
    )
    mushroom.draw(fenetre)
    crowbar = objet.Objet(
        "crowbar",
        pygame.image.load("pics/crowbar.png").convert_alpha(),
        lab.get_area(),
    )
    crowbar.draw(fenetre)
    seringe = objet.Objet(
        "seringe",
        pygame.image.load("pics/seringe.png").convert_alpha(),
        lab.get_area(),
    )
    seringe.draw(fenetre)
    lab.place_objet(mushroom)
    lab.place_objet(crowbar)
    lab.place_objet(seringe)

    pygame.display.flip()

    CONTINUER = 1
    while True:
        if CONTINUER != 0:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    CONTINUER = 0

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        mcgyver.deplacement([0, -1])
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        mcgyver.deplacement([0, 1])
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        mcgyver.deplacement([-1, 0])
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        mcgyver.deplacement([1, 0])

                    lab.draw(fenetre)
                    mushroom.draw(fenetre)
                    crowbar.draw(fenetre)
                    seringe.draw(fenetre)
                    gardien.draw(fenetre)
                    mcgyver.draw(fenetre)
                    mcgyver.update_map(lab._area)
                    pygame.display.flip()

                # if McGyver has all 3 Objets and have the same position as the guardian, you win
                if (
                    mcgyver.get_position()[0] == gardien.get_position()[0]
                    and mcgyver.get_position()[1] == gardien.get_position()[1]
                ):
                    if mcgyver.get_inventory() == 3:
                        fenetre.blit(win, (0, 0))
                        pygame.display.flip()
                        CONTINUER = 0

                    else:
                        fenetre.blit(lose, (0, 0))
                        pygame.display.flip()
                    CONTINUER = 0
