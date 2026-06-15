import pygame
import random
import sys

pygame.init()

sirina = 800
visina = 600
blok = 20

screen = pygame.display.set_mode((sirina, visina))
pygame.display.set_caption("Snake Maze")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

crna = (15, 15, 15)
zelena = (0, 220, 0)
tamna_zelena = (0, 180, 0)
crvena = (255, 0, 0)
siva = (60, 60, 60)

def kreiraj_zmijicu():
    return [
        (100, 100),
        (80, 100),
        (60, 100)
    ]

def kreiraj_hranu(zmijica):
    while True:
        hrana_x = random.randrange(0, sirina, blok)
        hrana_y = random.randrange(0, visina, blok)

        if (hrana_x, hrana_y) not in zmijica:
            return (hrana_x, hrana_y)

x_osa = blok
y_osa = 0

zmijica = kreiraj_zmijicu()
hrana = kreiraj_hranu(zmijica)
kraj_igre = False

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

    if not kraj_igre:

        glava_x_osa = zmijica[0][0] + x_osa
        glava_y_osa = zmijica[0][1] + y_osa

        if (
            glava_x_osa < 0 or glava_x_osa >= sirina or
            glava_y_osa < 0 or glava_y_osa >= visina
        🙁
            kraj_igre = True
        else:
            nova_glava = (glava_x_osa, glava_y_osa)

            if nova_glava in zmijica:
                kraj_igre = True
            else:
                zmijica.insert(0, nova_glava)

                if nova_glava == hrana:
                    hrana = kreiraj_hranu(zmijica)
                else:
                    zmijica.pop()

    screen.fill(crna)

    pygame.draw.rect(screen, siva, (0, 0, sirina, visina), 5)

    for dio in zmijica:
        pygame.draw.rect(screen, zelena, (dio[0], dio[1], blok, blok), border_radius=6)

    pygame.draw.rect(
        screen,
        tamna_zelena,
        (zmijica[0][0], zmijica[0][1], blok, blok),
        border_radius=6
    )

    pygame.draw.rect(screen, crvena, (hrana[0], hrana[1], blok, blok), border_radius=6)

    if kraj_igre:
        tekst = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(tekst, (sirina // 2 - 100, visina // 2))

    pygame.display.update()
    clock.tick(10)
