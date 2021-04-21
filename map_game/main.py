"""
Главный скрипт запуска
"""
import pygame
import map_game.database
from map_game.graphics import Polygon, Road, Player
def run():
    WIDTH = 800  # ширина игрового окна
    HEIGHT = 600 # высота игрового окна
    FPS = 30 # частота кадров в секунду
    BLACK = (0, 0, 0)
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()
    house_sprites, area_sprites, road_sprites = init_sprites()
    player = Player()
    # Цикл игры
    cursor_keys = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
    keys = {key: False for key in cursor_keys}
    running = True
    while running:
        clock.tick(FPS)
        keys_up = {pygame.K_UP: False, pygame.K_DOWN: False, pygame.K_LEFT: False, pygame.K_RIGHT: False}
        for event in pygame.event.get():
            # проверить закрытие окна
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in cursor_keys:
                    keys[event.key] = True
            elif event.type == pygame.KEYUP:
                if event.key in cursor_keys:
                    keys[event.key] = False


        player.move(keys)

        # Рендеринг
        screen.fill((100, 100, 100))
        area_sprites.draw(screen)
        house_sprites.draw(screen)
        road_sprites.draw(screen)


        screen.blit(player.image, player.rect.center)
        # после отрисовки всего, переворачиваем экран
        pygame.display.flip()

def init_sprites():
    db = map_game.database.DataBase()
    data = db.load()
    points = data['Points']
    houses = data['Houses']
    areas = data['Areas']
    roads = data['Roads']
    house_sprites = pygame.sprite.Group()
    area_sprites = pygame.sprite.Group()
    road_sprites = pygame.sprite.Group()
    for house in houses:
        p = Polygon(houses[house], points)
        p.fill_surface()
        house_sprites.add(p)
    for area in areas:
        p = Polygon(areas[area], points)
        p.fill_surface()
        area_sprites.add(p)
    for road in roads:
        r = Road(roads[road], points)
        r.fill_surface()
        road_sprites.add(r)
    return house_sprites, area_sprites, road_sprites
if __name__ == '__main__':
    run()