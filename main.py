from spritesheet import Spritesheet #Importing the function that creates a sprite sheet then defines the image used and its parameters 
import pygame
from sys import exit
SHEET = 'ChessPiecesArray.png'#Bringing in the images that will act as our 
BLACK = (255, 255, 255)
WIDTH = 800
HEIGHT = 800

pygame.init()
SCREEN: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running =False
        pygame.display.update()
    pygame.quit()
    exit()

if __name__ == '__main__':
    main()
