import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill((0,23,255))
pygame.display.update()


candycrush = pygame.image.load("candycrush.jpg")
ludo = pygame.image.load("ludo.png")
subwaysuffers = pygame.image.load("subwaysuffers.png")
temple_run = pygame.image.load("temple_run.png")

screen.blit(candycrush,(150,150))
screen.blit(ludo,(150,200))
screen.blit(subwaysuffers,(150,250))
screen.blit(temple_run,(150,300))