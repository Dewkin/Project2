import pygame
import random
from constants import *

class PipeManager:
    """
    Class for managing the pipes in the Flappy Bird game.

    Attributes:
        pipe_image (pygame.Surface): The image for the bottom pipe.
        flipped_pipe_image (pygame.Surface): The image for the top pipe (flipped version of pipe_image).
        pipes (list): A list of pipes currently in the game.
    """

    def __init__(self, pipe_image_path: str, flipped_pipe_image_path: str):
        """
        Initialize a new PipeManager object.
        """
        self.pipe_image = pygame.transform.scale(pygame.image.load(pipe_image_path).convert_alpha(), (PIPE_WIDTH, PIPE_HEIGHT))
        self.flipped_pipe_image = pygame.transform.flip(self.pipe_image, False, True)
        self.pipes = []
        self.debug = False

    def create_pipe(self) -> list:
        """
        Creates a new pair of pipes (top and bottom) and adds them to the game.

        Returns:
            list: A list containing the bottom and top pipe Rects, and a boolean for if the pipe has been passed.
        """
        min_top_pipe_height = 50
        max_top_pipe_height = SCREEN_HEIGHT - PIPE_GAP - min_top_pipe_height
        distance_from_top = random.randint(min_top_pipe_height, max_top_pipe_height)

        hitbox_height = PIPE_HEIGHT - 20

        bottom_pipe = self.pipe_image.get_rect(midtop=(500, distance_from_top + PIPE_GAP))
        bottom_pipe.height = hitbox_height
        top_pipe = self.flipped_pipe_image.get_rect(midbottom=(500, distance_from_top))
        top_pipe.height = hitbox_height
        return [bottom_pipe, top_pipe, False]

    def move_pipes(self, speed) -> list:
        """
        Moves all pipes in the game to the left, simulating the bird moving forward.

        Returns:
            list: The updated list of pipes after moving.
        """

        for pipe_set in self.pipes:
            bottom_pipe, top_pipe, _ = pipe_set
            bottom_pipe.centerx -= speed
            top_pipe.centerx -= speed
        self.pipes = [pipe for pipe in self.pipes if pipe[0].right > 0]
        return self.pipes

    def draw_pipes(self, screen: pygame.Surface, debug: bool = False) -> None:
        """
        Draws all the pipes on the given screen.

        debug (bool): If True, draws a rectangle around the pipes for debugging purposes.
        """
        for pipe_set in self.pipes:
            bottom_pipe, top_pipe, _ = pipe_set
            screen.blit(self.pipe_image, bottom_pipe)
            screen.blit(self.flipped_pipe_image, top_pipe)

            if self.debug:
                for pipe_set in self.pipes:
                    bottom_pipe, top_pipe, _ = pipe_set
                    pygame.draw.rect(screen, (0, 0, 255), bottom_pipe, 2)
                    pygame.draw.rect(screen, (0, 0, 255), top_pipe, 2)

    def check_collision(self, bird_rect: pygame.Rect) -> bool:
        """
        Checks if the bird has collided with any of the pipes.

        Returns:
            bool: True if there is a collision, False otherwise.
        """

        for pipe_set in self.pipes:
            bottom_pipe, top_pipe, _ = pipe_set
            if bird_rect.colliderect(bottom_pipe) or bird_rect.colliderect(top_pipe):
                return False
        return True