import pygame


WIDTH = 800
HEIGHT = 800
MIDDLE_SCREEN = (WIDTH // 2, HEIGHT // 2)
FPS = 60

FONT = lambda size: pygame.font.SysFont('verdana', size, True)
COLORS = {
    'white':  (200, 200, 200),
    'black':  (50, 50, 50),
    'orange': (150, 80, 40),
    'green':  (0, 200, 0),
    'blue':   (0, 0, 200),
    'gray':   (150, 150, 150),
    'purple': (120, 0, 120),
    'red':    (200, 0, 0),
    'bg':     (20, 20, 20)
}

