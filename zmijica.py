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
tamna_zelena=(0, 180, 0)

def kreiraj_zmijicu():
    return [
        (100, 100),
        (80, 100),
        (60, 100)
    ]
x_osa=blok
y_osa=0
trenutni_level=0
zmijica=kreiraj_zmijicu()
kraj_igre=False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and y_osa == 0:

                x_osa = 0
                y_osa = -blok

            elif event.key == pygame.K_DOWN and y_osa == 0:

                x_osa = 0
                y_osa = blok

            elif event.key == pygame.K_LEFT and x_osa == 0:

                x_osa = -blok
                y_osa = 0

            elif event.key == pygame.K_RIGHT and x_osa == 0:

                x_osa = blok
                y_osa = 0

    if kraj_igre==False:
        glava_x_osa=zmijica[0][0] + x_osa
        glava_y_osa=zmijica[0][1] + y_osa

        nova_glava=(glava_x_osa,glava_y_osa)
        zmijica.insert(0,nova_glava)
        zmijica.pop()
        
        
    screen.fill(crna)
    for dio in zmijica:
        pygame.draw.rect(screen,zelena,(dio[0],dio[1],blok,blok),border_radius=6)
    pygame.draw.rect(screen,tamna_zelena,(zmijica[0][0],zmijica[0][1],blok,blok),border_radius=6)
    pygame.display.update()
    clock.tick(10)
