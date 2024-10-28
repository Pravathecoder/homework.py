import pygame
pygame.init()


screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Match the following')

font = pygame.font.SysFont('arial',32)

ludo = pygame.image.load('images/ludo.png')  
templerun = pygame.image.load('images/templerun.png')
candycrush = pygame.image.load('images/candy crush.jpg')
subway = pygame.image.load('images/subway.png')

while True:
    screen.blit(ludo, (0,0))
    screen.blit(templerun,(0,200))
    screen.blit(candycrush,(0,400))
    screen.blit(subway,(0,600))

    tem = font.render('Temple Run', False, 'yellow')
    screen.blit(tem,(600,0))
    sub = font.render('Subway',False,'green')
    screen.blit(sub,(600,200))
    lu = font.render('Ludo', False, 'blue')
    screen.blit(lu,(600,400))
    can = font.render('Candy crush',False,'pink')
    screen.blit(can,(600,600))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    pygame.display.update()