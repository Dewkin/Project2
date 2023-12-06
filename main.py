import pygame
import sys
from bird import Bird
from pipe import PipeManager
from utils import load_high_score, save_high_score, check_collision
from constants import *
from display import Display


def main() -> None:
    """
    Main function for running the game. Initializes the game,
    handles the main game loop, and updates the game state.
    """
    pygame.init()
    pygame.font.init()

    speed = GAME_SPEED

    pygame.time.set_timer(PIPE_SPAWN, 1200)

    # Set up display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flappy Bird Clone")

    #  Display object
    display = Display('background.png')

    # Create game objects
    bird = Bird('bird.png')
    pipes = PipeManager('pipe.png', 'pipe.png')
    high_score = load_high_score()

    clock = pygame.time.Clock()
    score = 0
    game_active = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active:
                    bird.flap()
                if event.key == pygame.K_SPACE and not game_active:
                    # Resets game state
                    game_active = True
                    bird = Bird('bird.png')
                    pipes = PipeManager('pipe.png', 'pipe.png')
                    score = 0
                    speed = GAME_SPEED
                if event.key == pygame.K_d:  # Press 'D' to toggle debug mode
                    bird.debug = not bird.debug
                    pipes.debug = not pipes.debug
            if event.type == PIPE_SPAWN:
                pipes.pipes.append(pipes.create_pipe())

        display.draw_background(screen)

        if game_active:

            if score % 10 == 0 and score != 0:
                speed += 0.005

            bird.update()
            bird.draw(screen)

            pipes.move_pipes(speed)
            pipes.draw_pipes(screen)
            game_active = check_collision(pipes.pipes, bird.rect)

            # Update and displays score
            for pipe_set in pipes.pipes:
                bottom_pipe, top_pipe, passed = pipe_set
                if not passed and top_pipe.centerx < bird.rect.left:
                    score += 1
                    pipe_set[2] = True

            display.draw_score(screen, score)

        else:
            # End game screen
            display.draw_end_game_screen(screen, score, high_score)

            # Dynamic score update
            try:
                if score > high_score:
                    high_score = score
                    save_high_score(high_score)
            except IOError as e:
                print(f"Error saving high score: {e}")

        display.draw_game_speed(screen, speed, debug=bird.debug)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
