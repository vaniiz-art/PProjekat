import pygame
import random
import sys

pygame.init()

sirina = 800
visina = 600

blok=20

screen = pygame.display.set_mode((sirina, visina))
pygame.display.set_caption("Snake Maze")

clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 30)

crna=(15, 15, 15)
zelena=(0, 220, 0)


def kreiraj_zmijicu():
    return [
        (100, 100),
        (80, 100),
        (60, 100)
    ]

trenutni_level=0
zmijica=kreiraj_zmijicu()
kraj_igra=False

while True:
    screen.fill(crna)
    for dio in zmijica:
        pygame.draw.rect(screen,zelena,(dio[0],dio[1],blok,blok),border_radius=6)
    pygame.display.update()
