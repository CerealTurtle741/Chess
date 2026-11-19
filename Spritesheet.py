import pygame
class Spritesheet:
    def __init__(
        self,
        image: pygame.Surface
        ) -> None:
        self.sheet = image

    def get_image(
        self,
        width: int,
        height: int,
        frame_x: int,
        frame_y: int,
        scale: int,
        color
        ) -> pygame.Surface:
        """
        Gets the desired image from the spritesheet and returns it to be blitted into the game
        """
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0,0), ((frame_x * width), (frame_y * height), width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colokey(color)
        return image
