import pygame
from player import Player
from levels import DemoLevel1, check
from settings import terminate, scr_width, draw_text, screen


def play():  # основная тестовая функция
    pygame.display.set_caption('Stealing gifts | 1 уровень')  # название окна
    player = Player()  # создание игрока
    player.rect.y = 520  # спаун игрока внизу
    level = DemoLevel1(player)
    active_session = pygame.sprite.Group()  # активная сессия
    player.level = level  # добавление уровня
    active_session.add(player)  # добавление игрока в группу спрайтов
    running = True  # флаг для цикла
    clock = pygame.time.Clock()  # для скорости обновления экрана
    while running:  # основной цикл
        for event in pygame.event.get():  # следим за действиями играющего
            if event.type == pygame.QUIT:  # выход из игры
                terminate()
            if event.type == pygame.KEYDOWN:  # обработка клавиатуры
                if event.key == pygame.K_ESCAPE:
                    terminate()
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
                    check(player.rect)
        active_session.update()  # обновление игрока
        level.update()  # обновление уровня
        if player.rect.left < 0:  # ограничение движения за экран слева
            player.rect.left = 0
        if player.rect.right > scr_width:  # справа
            player.rect.right = scr_width
        level.draw(screen)  # рисовка выбранного уровня
        active_session.draw(screen)
        draw_text('Чтобы забрать печенье и подарок, нажмите [e].',
                  'Также нажмите [е], когда заберётесь на трубу, чтобы перейти на следующий уровень.')
        clock.tick(30)  # fps
        pygame.display.flip()  # обновление экрана
    pygame.quit()  # закрытие игры