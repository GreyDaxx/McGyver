from Constantes import SPRITE_SIZE


class Character:
    #initialasing Character Class
    def __init__(self,depart,img, laby):
        self.position = depart
        self.img = img
        self.laby = laby
        self.inventory = 0
		
    """checks if the next position is a wall, then adjust the logic position of McGyver before its graphic one"""
    def deplacement(self, mouv):
        next_x = self.position[0] + mouv[0]
        next_y = self.position[1] + mouv[1]
        if self.laby.area[next_x][next_y] != 1:
            self.position[0] += mouv[0]
            self.position[1] += mouv[1]

        """printing back McGyver and the Objets"""
        print(self.laby.area[self.position[0]][self.position[1]])
        if self.laby.area[next_x][next_y] == 9:
            for objet in self.laby.objets:
                if self.position[0] == objet.position[0] and self.position[1] == objet.position[1]:
                    objet.position[0] = 15
                    objet.position[1] = 7 + self.inventory
                    self.inventory +=1
                    self.laby.objets.remove(objet)

    """draw each square of the lab from their logic position"""
    def draw(self, fenetre):
        print(self.position, SPRITE_SIZE)
        fenetre.blit(self.img,(self.position[1]*SPRITE_SIZE,self.position[0]*SPRITE_SIZE))

    """actualising the displayed lab"""
    def update_map(self,area):
        self.laby.area = area