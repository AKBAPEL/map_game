"""
Главный скрипт запуска
"""
import pygame
import map_game.database
from map_game.graphics import Polygon, Road


def run():
    WIDTH = 1024  # ширина игрового окна
    HEIGHT = 768 # высота игрового окна
    FPS = 30 # частота кадров в секунду
    BLACK = (0, 0, 0)

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()

    house_sprites, area_sprites, road_sprites = init_sprites()
    #Цикл Игры
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            # проверить закрытие окна
            if event.type == pygame.QUIT:
                running = False
        # Рендеринг
        screen.fill(BLACK)
        area_sprites.draw()
        house_sprites.draw()
        road_sprites.draw()

        # после отрисовки всего, переворачиваем экран
        pygame.display.flip()


def init_sprites():
    db = map_game.database.DataBase()
    data = db.load()
    running = True
    points = data['Points']
    houses = data['Houses']
    areas = data['Areas']
    roads = data['Roads']
    house_sprites = pygame.sprite.Group()
    area_sprites = pygame.sprite.Group()
    road_sprites = pygame.sprite.Group()
    for house in houses:
        p = (Polygon(house, points))
        p.fill_surface()
        house_sprites.add(p)
    for area in areas:
        p = (Polygon(area, points))
        p.fill_surface()
        house_sprites.add(p)
    for road in roads:
        r = (Road(road, points))
        r.fill_surface()
        house_sprites.add(r)

    return house_sprites, area_sprites, road_sprites


def convert_coord(house_data, points):
    points_ = [points[p] for p in house_data.points]
    screen_coord = [(p.x, p.y) for p in points_]
    return screen_coord


if __name__ == '__main__':
    run()