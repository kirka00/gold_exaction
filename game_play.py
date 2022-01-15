import pygame
from player import Player
from levels import Level, check
from settings import terminate, scr_width, screen


def play():  # основная тестовая функция
    pygame.display.set_caption('Stealing gifts | 1 уровень')  # название окна
    player = Player()  # создание игрока
    player.rect.x, player.rect.y = 0, 20  # начальное положение игрока
    active_session = pygame.sprite.Group()  # активная сессия
    cur_level = Level(player, 'level1.txt')  # переключения на 1 уровень
    player.level = cur_level  # инициализация уровня
    active_session.add(player)  # добавление игрока в игровую сессию
    running = True  # флаг для цикла
    clock = pygame.time.Clock()  # для скорости обновления экрана
    while running:  # основной цикл
        for event in pygame.event.get():  # следим за действиями играющего
            if event.type == pygame.QUIT:  # выход из игры
                terminate()  # полный выход из игры
            if event.type == pygame.KEYDOWN:  # обработка клавиатуры
                if event.key == pygame.K_ESCAPE:
                    terminate()  # полный выход из игры
                if event.key == pygame.K_UP:  # прыжок
                    player.jump()
                elif event.key == pygame.K_LEFT:  # влево
                    player.go_to_left()
                elif event.key == pygame.K_RIGHT:  # вправо
                    player.go_to_right()
            if event.type == pygame.KEYUP:  # если ничего не зажато
                if event.key == pygame.K_LEFT:
                    player.stop()  # остновка, если герой идёт влево
                elif event.key == pygame.K_RIGHT:
                    player.stop()  # остновка, если вправо
                elif event.key == pygame.K_e:
                    # проверка выполнены ли условия для перехода на след лвл
                    if check(player.rect, cur_level):  # проверка перешёл ли игрок в трубу
                        player.rect.x, player.rect.y = 0, 500  # начальное положение игрока
                        cur_level.clear()  # очистить текущий уровень
                        # переключение на след уровень
                        cur_level = Level(player, 'level2.txt')
                        player.level = cur_level  # инициализация уровня
        active_session.update()  # обновление игрока
        cur_level.update()  # обновление уровня
        if player.rect.left < 0:  # ограничение движения за экран слева
            player.rect.left = 0
        if player.rect.right > scr_width:  # справа
            player.rect.right = scr_width
        cur_level.draw(screen)  # рисовка выбранного уровня
        active_session.draw(screen)
        cur_level.render_coins(screen)  # прорисовка монет
        clock.tick(30)  # fps
        pygame.display.flip()  # обновление экрана
    pygame.quit()  # закрытие игры