import os

import pygame
import numpy as np


from helper import check, move, create, fill


def start_generate(count, id_user):
    pygame.init()
    screen = pygame.display.set_mode((540, 540))

    data = np.zeros((1, 0))

    for i in range(count):
        data = check(data)
        data = move(data)
        data = create(data)

    colors = np.array([
        [0, 0, 0],
        [175, 238, 238],
        [238, 130, 238],
        [152, 251, 152],
        [240, 230, 140],
    ])

    screen.fill((30, 30, 30))
    make = fill(data)

    screen = pygame.surfarray.make_surface(colors[make.astype(int)])
    screen = pygame.transform.scale(screen, (540, 540))
    pygame.image.save(screen, os.path.join('images', 'save_image' + str(id_user) + '.JPG'))



