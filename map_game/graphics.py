import pygame

class Ground(pygame.sprite.Sprite):
    def __init__(self,data,points):
        super().__init__()
        self.color = data.color
        screen_coord = self.convert_coord(data,points)
        pygame.sprite.Sprite.__init__(self)
        x,y = self.get_dimension(screen_coord)
        self.image = pygame.Surface((x,y))
        self.rect = self.image.get_rect()
        self.image.fill((0,0,0))

    def convert_coord(self,data,points):
        points_ = [points[p] for p in data.points]
        screen_coord = [(p.x, p.y) for p in points_]
        return  screen_coord

    def get_dimension(self, coords):
        x = [c[0] for c in coords]
        y = [c[1] for c in coords]
        diff_x = abs(max(x) - min(x))
        diff_y = abs(max(y) - min(y))
        return diff_x, diff_y

class Polygon(Ground):
    def fill_surface(self):
        pygame.draw.polygon(self.screen, self.color, self.screen_coord, 0)

class Road(Ground):
    def __init__(self, data, points):
        super().__init__(data, points)
        self.width = data.width

    def fill_surface(self):
        pygame.draw.polygon(self.screen, self.color, False, self.screen_coord, width)