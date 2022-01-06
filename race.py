import pygame
import random
from load import load_image, screen
from music import car_music
from settings import scr_width, scr_height, clock, \
    small_font, terminate


def draw_car(x, y):  # рисовка машины в нужном месте
    car_image = load_image('car.png')  # картинка машины
    screen.blit(car_image, (x, y))


def crash():  # столкновение
    pygame.mixer.music.stop()  # глушим звук мотора
    TextSurf, TextRect = text_in_screen('Вы умерли!', small_font)
    TextRect.center = ((scr_width / 2), (scr_height / 2))
    screen.blit(TextSurf, TextRect)  # вывод информации о проигрыше
    while True:  # пока есть возможность переиграть
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()  # выход из игры
            if event.type == pygame.KEYDOWN:  # продолжение игры
                if event.key == pygame.K_SPACE:
                    racing()
                if event.key == pygame.K_ESCAPE:  # выход из игры на Escape
                    terminate()
        button('Играть заново', 150, 450, 200, 50,
               'green', 'white', racing)  # кнопки для выхода и переигрыша
        button('Выход', 550, 450, 100, 50, 'red', 'white', terminate)
        pygame.display.flip()


def button(msg, x, y, w, h, color, direct_color, do=None):  # рисовка кнопок
    mouse_pos = pygame.mouse.get_pos()  # ловим мышь
    click_mouse = pygame.mouse.get_pressed()  # ловим клик мыши
    # ловим нужное положение курсора
    if x + w > mouse_pos[0] > x and y + h > mouse_pos[1] > y:
        # метка о нахождении курсора на кнопке
        pygame.draw.rect(screen, direct_color, (x, y, w, h))
        if do != None and click_mouse[0] == 1:
            do()  # срабатывает нужная нам функция
    else:  # в ином случае просто рисуем обычные кнопки
        pygame.draw.rect(screen, color, (x, y, w, h))
    textSurf, textRect = text_in_screen(msg, small_font)  # настройка текста
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)  # вывод кнопок на экран


def continuation():  # продолжегне игры
    global pause  # делаем переменную pause глобальной
    pygame.mixer.music.unpause()  # музыка снова играет
    pause = False  # фложок на False


def stopping():
    pygame.mixer.music.pause()
    TextSurf, TextRect = text_in_screen('Пауза', small_font)
    TextRect.center = ((scr_width / 2), (scr_height / 2))
    screen.blit(TextSurf, TextRect)  # вывод текста на экран
    while pause:
        for event in pygame.event.get():  # выход из игры
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:  # продолжение игры
                if event.key == pygame.K_SPACE:
                    continuation()
                if event.key == pygame.K_ESCAPE:  # выход из игры на Escape
                    terminate()
        if pause:  # вывод кнопок на экран
            button('Продолжить', 200, 450, 200, 50,
                   'green', 'white', continuation)
            button('Выход', 550, 450, 100, 50, 'red', 'white', terminate)
            pygame.display.flip()  # обновление экрана


def draw_coins(coins):  # вывод количества очков на экран
    conclusion = small_font.render(
        f'Количество очков: {coins}', True, 'black')
    screen.blit(conclusion, (0, 0))


def text_in_screen(text, font):  # вывод текста на экран
    conclusion = font.render(text, True, 'black')
    return conclusion, conclusion.get_rect()


def obstacles(thingx, thingy, thingw, thingh, color):  # отрисовка препятсвий
    tree = load_image('tree.png')
    screen.blit(tree, (thingx + 15, thingy - 100))
    pygame.draw.rect(screen, color, [thingx, thingy, thingw, thingh])


def racing():
    global pause  # не забываем делать переменную pause глобальной
    ''' Критерии машины '''
    car_width = 73  # ширина машины
    x, y = scr_width / 2 - 30, 480  # спаун машины
    score_car = 7  # скорость машины
    score_x = 0  # изменение скорости машины
    ''' Критерии препятсвий '''
    obstacle_start_x = random.randint(0, scr_width)  # спаун препятствий
    obstacle_start_y = -600  # выход препятствия сверху экрана
    obstacle_speed = 8  # начальная скорость препятствия
    obstacle_width, obstacle_height = 80, 10  # размер препятствия
    coins = 0  # очки
    ''' Остальное '''
    pygame.display.set_caption(
        'Stealing gifts | Финал')  # заголовок экрана
    pause = False  # рауза игры
    car_music()
    while True:
        for event in pygame.event.get():  # отслеживание действий
            if event.type == pygame.QUIT:  # выход из игры
                terminate()
            elif event.type == pygame.KEYDOWN:  # езда вправо
                if event.key == pygame.K_RIGHT:
                    score_x = score_car
                elif event.key == pygame.K_LEFT:  # езда влево
                    score_x = -score_car
                elif event.key == pygame.K_SPACE:  # пауза
                    pause = True  # флаг на True
                    stopping()  # аызов функции паузы
            elif event.type == pygame.KEYUP:  # остановка движения машины при отсутствии нажатия на кнопки
                score_x = 0
        x += score_x  # перемещение машины
        screen.fill('white')  # пока фон белый
        obstacles(obstacle_start_x, obstacle_start_y,  # отрисовка препятствий
                  obstacle_width, obstacle_height, (162, 101, 62))
        obstacle_start_y += obstacle_speed  # корректировка y для препятствий
        draw_car(x, y)  # рисовка машины по x и y
        draw_coins(coins)  # вывод очков
        if x < 0 or x > scr_width - car_width:
            crash()  # ограничители
        if obstacle_start_y > scr_height:
            obstacle_start_y = 0 - obstacle_height
            obstacle_start_x = random.randrange(0, scr_width)
            coins += 1  # добавление очков
            obstacle_speed += 1  # ускорение препятствий
            # увеличение ширины препятствий для усложнения игры
            obstacle_width += (coins * 1.5)
        if y < obstacle_start_y + obstacle_height:  # столкновение с препятствиями
            if x > obstacle_start_x and x < obstacle_start_x + obstacle_width or x+car_width > obstacle_start_x and x + car_width < obstacle_start_x + obstacle_width:
                crash()  # функция столкновения
        pygame.display.flip()  # обновление экрана
        clock.tick(60)  # фпс

#racing()