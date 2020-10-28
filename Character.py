"""coding: utf-8"""

from constantes import SPRITE_SIZE


class Character:
    """initialasing Character Class"""

    def __init__(self, depart, img, laby):
        self._position = depart
        self._img = img
        self._laby = laby
        self._inventory = 0

    def get_position(self):
        """get the hidden position value"""
        return self._position

    def get_img(self):
        """get the hidden img value"""
        return self._img

    def get_laby(self):
        """get the hidden laby value"""
        return self._laby

    def get_inventory(self):
        """get the hidden inventory value"""
        return self._inventory

    def add_inventory(self):
        """add 1 object to the hidden inventory"""
        self._inventory += 1

    def deplacement(self, mouv):
        """checks if the next position is a wall, then adjust the logic position of McGyver before its graphic one, then print McGyver and Objets"""
        next_x = self.get_position()[0] + mouv[0]
        next_y = self.get_position()[1] + mouv[1]
        if self._laby.get_area()[next_x][next_y] != 1:
            self.get_position()[0] += mouv[0]
            self.get_position()[1] += mouv[1]

        print(self._laby.get_area()[self.get_position()[0]][self.get_position()[1]])
        if self._laby.get_area()[next_x][next_y] == 9:
            for objets in self._laby.get_objets():
                if (
                    self.get_position()[0] == objets.get_position()[0]
                    and self.get_position()[1] == objets.get_position()[1]
                ):
                    objets.get_position()[0] = 15
                    objets.get_position()[1] = 7 + self.get_inventory()
                    self.add_inventory()
                    self._laby.pickup_objets(objets)

    def draw(self, fenetre):
        """draw each square of the lab from their logic position"""
        print(self.get_position(), SPRITE_SIZE)
        fenetre.blit(
            self.get_img(),
            (
                self.get_position()[1] * SPRITE_SIZE,
                self.get_position()[0] * SPRITE_SIZE,
            ),
        )

    def update_map(self, area):
        """actualising the displayed lab"""
        self._laby.area = area
