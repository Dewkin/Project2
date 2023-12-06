import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Display:
    """
    Class for managing the display elements in the Flappy Bird game.

    Attributes:
        background_image (pygame.Surface): The background image of the game.
        score_font (pygame.font.Font): The font used for displaying scores.
    """

    def __init__(self, background_image_path: str):
        """
        Initialize a new Display object.
        """
        self.background_image = pygame.transform.scale(pygame.image.load(background_image_path).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.score_font = pygame.font.Font(None, 36)

    def draw_background(self, screen: pygame.Surface) -> None:
        """
        Draws the background image on the given screen.
        """
        screen.blit(self.background_image, (0, 0))

    def draw_score(self, screen: pygame.Surface, score: int) -> None:
        """
        Draws the current score on the screen.

        Args:
            screen (pygame.Surface): The game screen where the score is drawn.
            score (int): The current score to display.
        """
        score_surface = self.score_font.render(str(score), True, (0, 0, 0))
        score_rect = score_surface.get_rect(center=(SCREEN_WIDTH / 2, 50))
        screen.blit(score_surface, score_rect)

    def draw_high_score(self, screen: pygame.Surface, high_score: int) -> None:
        """
        Draws the high score on the screen.

        Args:
            screen (pygame.Surface): The game screen where the high score is drawn.
            high_score (int): The high score to display.
        """
        high_score_surface = self.score_font.render(f"High Score: {high_score}", True, (0, 0, 0))
        high_score_rect = high_score_surface.get_rect(center=(SCREEN_WIDTH / 2, 100))
        screen.blit(high_score_surface, high_score_rect)

    def draw_end_game_screen(self, screen: pygame.Surface, score: int, high_score: int) -> None:
        """
        Draws the end game screen, including the final score and high score.

        Args:
            screen (pygame.Surface): The game screen where the end game screen is drawn.
            score (int): The final score to display.
            high_score (int): The high score to display.
        """
        # Dims the background
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))  # Semi-transparent black overlay
        screen.blit(overlay, (0, 0))

        # Displays game over text
        game_over_font = pygame.font.Font(None, 54)
        game_over_surface = game_over_font.render("Game Over", True, (255, 255, 255))
        game_over_rect = game_over_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 60))
        screen.blit(game_over_surface, game_over_rect)

        # Displays score
        score_surface = self.score_font.render(f"Score: {score}", True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(score_surface, score_rect)

        # Displays high score
        high_score_surface = self.score_font.render(f"High Score: {high_score}", True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 60))
        screen.blit(high_score_surface, high_score_rect)

    def draw_game_speed(self, screen: pygame.Surface, speed: float, debug: bool) -> None:
        """
        Draws the current game speed on the screen if debug mode is on.

        Args:
            screen (pygame.Surface): The game screen where the game speed is drawn.
            speed (float): The current game speed to display.
            debug (bool): Indicates whether to show the game speed.
        """
        if debug:
            speed_font = pygame.font.Font(None, 24)  # Smaller font for game speed
            speed_surface = speed_font.render(f"Speed: {speed:.1f}", True, (0, 0, 0))
            speed_rect = speed_surface.get_rect(topright=(SCREEN_WIDTH - 10, 10))
            screen.blit(speed_surface, speed_rect)