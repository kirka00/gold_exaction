import pygame
from intro import game_intro
#from end import end_game

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Gold exaction')

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        if running:
            game_intro()



if __name__ == '__main__':
    main()