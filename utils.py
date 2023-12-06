def load_high_score():
    try:
        with open("high_score.txt", "r") as file:
            return int(file.read())
    except (FileNotFoundError, ValueError):
        return 0

def save_high_score(high_score):
    with open("high_score.txt", "w") as file:
        file.write(str(high_score))

def check_collision(pipes, bird_rect):
    for pipe_set in pipes:
        bottom_pipe, top_pipe, _ = pipe_set
        if bird_rect.colliderect(bottom_pipe) or bird_rect.colliderect(top_pipe):
            return False
    if bird_rect.top <= -50 or bird_rect.bottom >= 600:
        return False
    return True
