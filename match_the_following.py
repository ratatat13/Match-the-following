import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill((255,23,255))
pygame.display.update()


candycrush = pygame.image.load("candycrush.jpg")
ludo = pygame.image.load("ludo.png")
subwaysuffers = pygame.image.load("subwaysuffers.png")
temple_run = pygame.image.load("temple_run.png")

screen.blit(candycrush,(150,60))
screen.blit(ludo,(150,180))
screen.blit(subwaysuffers,(150,300))
screen.blit(temple_run,(150,420))

font = pygame.font.SysFont("Ariel", 60)


text1 = font.render("Ludo", True, (0,0,0))
text2 = font.render("Subwaysuffers", True, (213,241,49))
text3 = font.render("Templerun", True, (23,84,239))
text4 = font.render("Candycrush",True, (76,12,31))


screen.blit(text1,(300,60))
screen.blit(text2,(300,180))
screen.blit(text3,(300,300))
screen.blit(text4,(300,420))

pygame.display.update()

while True:
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen,(74,30,20),pos, 20, 0)
        pygame.display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
        pos2 = pygame.mouse.get_pos()
        pygame.draw.line(screen, (23,42,24), pos,  pos2, 5)
        pygame.draw.circle(screen, (23,37,255), pos2, 20, 0)
        pygame.display.update()

pygame.quit()