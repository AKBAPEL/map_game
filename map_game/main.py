"""
Главный скрипт запуска
"""
import pygame
import map_game.database

def run():
    WIDTH = 1024  # ширина игрового окна
    HEIGHT = 768 # высота игрового окна
    FPS = 30 # частота кадров в секунду
    BLACK = (0, 0, 0)

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()

    db = map_game.database.DataBase()
    data = db.load()

    # Цикл игры
    running = True
    points = data['Points']
    houses = data['Houses']
    areas = data['Areas']
    roads = data['Roads']
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            # проверить закрытие окна
            if event.type == pygame.QUIT:
                running = False
        # Рендеринг
        screen.fill(BLACK)

        for area_id in areas:
            area_data = areas[area_id]
            color = area_data.color
            screen_coord = convert_coord(area_data, points)
            pygame.draw.polygon(screen, color, screen_coord, 0)
        for house_id in houses:
            house_data = houses[house_id]
            color = house_data.color
            screen_coord = convert_coord(house_data, points)
            pygame.draw.polygon(screen, color, screen_coord, 0)
        for road_id in roads:
            road_data = roads[road_id]
            color = road_data.color
            width = road_data.width
            screen_coord = convert_coord(road_data, points)
            pygame.draw.lines(screen, color, False, screen_coord, width)
        # после отрисовки всего, переворачиваем экран
        pygame.display.flip()


def convert_coord(house_data, points):
    points_ = [points[p] for p in house_data.points]
    screen_coord = [(p.x, p.y) for p in points_]
    return screen_coord


if __name__ == '__main__':
    run()