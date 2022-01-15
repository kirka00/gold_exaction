import pygame


def car_music():  # звук машины из гонок
    pygame.mixer.music.stop()
    pygame.mixer.music.load('data/sounds/sound_car.ogg')  # музыка
    pygame.mixer.music.set_volume(0.1)  # устанвока нужной громкости
    pygame.mixer.music.play(-1)  # зацикливание


def main_sound():  # основной саундтрек игры
    pygame.mixer.music.load('data/sounds/soundtrack.mp3')  # основная музыка
    pygame.mixer.music.set_volume(0.1)  # устанвока нужной громкости
    pygame.mixer.music.play(-1)  # зацикливание
