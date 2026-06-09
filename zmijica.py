import pygame
import random
import sys

pygame.init()

sirina = 800
visina = 600

screen = pygame.display.set_mode((sirina, visina))
pygame.display.set_caption("Snake Maze")

clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 30)
