import pygame
import math

import settings
from lineargebra import Vector3D, Vector2D, Matrix


# setup
pygame.init()
window = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
clock = pygame.time.Clock()
middle = Vector2D(settings.MIDDLE_SCREEN)

# scene setup
angle = 0
points = [
    Vector3D([-100, -100, -100]),
    Vector3D([100, -100, -100]),
    Vector3D([100, 100, -100]),
    Vector3D([-100, 100, -100]),
    Vector3D([-100, -100, 100]),
    Vector3D([100, -100, 100]),
    Vector3D([100, 100, 100]),
    Vector3D([-100, 100, 100])
]

while True:

    # This three matrix, represent the 3D rotations matrix (https://en.wikipedia.org/wiki/Rotation_matrix) of the 3 axis
    # X, Y and Z.
    rotationX = Matrix((
        [1, 0, 0],
        [0, math.cos(angle), - math.sin(angle)],
        [math.sin(angle), math.cos(angle), 0]
    ))

    rotationY = Matrix((
        [math.cos(angle), 0, - math.sin(angle)],
        [0, 1, 0],
        [math.sin(angle), 0, math.cos(angle)]
    ))

    rotationZ = Matrix((
        [math.cos(angle), - math.sin(angle), 0],
        [math.sin(angle), math.cos(angle), 0],
        [0, 0, 1]
    ))

    # EVENT GESTION
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        quit()


    # DRAWS
    window.fill(settings.COLORS['bg'])

    updated_points = [[] for _ in range(len(points))]
    for index, v in enumerate(points):
        rotated_point = rotationY * Matrix(list(map(lambda el: [el], v)))  # We're transforming the vector of the point
                                                                           # into a matrix, then applying matrix product
                                                                           # to calculate the coordinates of the rotated
                                                                           # point.
        rotated_point = rotationX * rotated_point  # Applying one more rotation

        updated_point = Vector2D([rotated_point[0][0], rotated_point[1][0]])  # Transforming back the matrix
                                                                              # into 2Dvector
        updated_point = updated_point + middle  # We're adding the middle vector, in order to draw from the center

        updated_points[index] = updated_point  # Push the new vector coordinates


    for i in range(4):
        # Drawing connexions between points of the cube
        pygame.draw.line(window, settings.COLORS['white'], updated_points[i], updated_points[(i+1) % 4])
        pygame.draw.line(window, settings.COLORS['white'], updated_points[i+4], updated_points[((i+1) % 4) + 4])
        pygame.draw.line(window, settings.COLORS['white'], updated_points[i], updated_points[i + 4])

    angle += 0.01  # This is the angle of the cube incrementing
    pygame.display.flip()
    clock.tick(settings.FPS)
