import pygame
from constants import BIRD_WIDTH, BIRD_HEIGHT, GRAVITY, JUMP_HEIGHT, SCREEN_HEIGHT

class Bird:
    """
    Class representing the bird in the game.

    Attributes:
        image (pygame.Surface): The image of the bird.
        rect (pygame.Rect): The rectangle representing the bird's position and size.
        movement (float): The vertical movement speed of the bird.
        rotated_image (pygame.Surface): The rotated image of the bird based on its movement.
    """

    def __init__(self, image_path: str):
        """
        Initialize a new bird object.
        """
        self.image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(), (BIRD_WIDTH, BIRD_HEIGHT))
        self.rect = self.image.get_rect(center=(100, SCREEN_HEIGHT // 2))
        self.movement = 0
        self.debug = False

    def flap(self) -> None:
        """
        Makes the bird jump up.
        """
        self.movement = JUMP_HEIGHT

    def update(self) -> None:
        """
        Updates the bird's position and rotation.
        """
        self.movement += GRAVITY
        self.rect.centery += self.movement
        self.rotated_image = self._rotate_bird()

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the bird on the given screen.
        """
        new_rect = self.rotated_image.get_rect(center=self.rect.center)
        screen.blit(self.rotated_image, new_rect)

        if self.debug:
            hitbox = self.get_hitbox()
            pygame.draw.rect(screen, (255, 0, 0), hitbox, 2)

    def _rotate_bird(self) -> pygame.Surface:
        """
        Rotates the bird image based on its vertical movement.
        """
        rotation_degree = -self.movement * 3
        return pygame.transform.rotate(self.image, rotation_degree)

    def get_hitbox(self) -> pygame.Rect:
        """
        Returns the hitbox for the bird.
        """
        hitbox = self.rect.inflate(-14, -14)
        return hitbox
