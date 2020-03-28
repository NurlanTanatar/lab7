import pygame
pygame.init()

screen=pygame.display.set_mode((640,480))
background=pygame.Surface(screen.get_size())
background.fill((255,255,255))

pygame.draw.circle(background,(255,192,203),(320,240),150)

pygame.draw.polygon(background,(0,255,0),((320,120),(270,240),(370,360)))
pygame.draw.polygon(background,(0,255,0),((320,120),(353,240),(237,360)))
pygame.draw.polygon(background,(0,255,0),((320,300),(220,180),(420,180)))

pygame.draw.arc(background,(0,0,0),(0,0,1280,960),0,3.14)

for point in range(0,641,64): 
   pygame.draw.line(background, ( (255-(point%256))%256 ,(255-(228+point))%256 ,point%256), (0,0), (480, point), 1)
   pygame.draw.line(background, ( (255-(point%256))%256 , point%256 , (255+(point%256))%256), (640,0), (160, point), 1)             # lines
   pygame.draw.line(background, ( (255+(point%256))%256 ,point%256 , (100*point//64)%256 ), (640,480), (160, point), 1)             # lines
   pygame.draw.line(background, ( (100*point//64)%256 , (228+point)%256 , (255*(point%256))%256 ) , (0,480), (480, point), 1)

background=background.convert()
screen.blit(background, (0, 0))

running = True
FPS = 60
clock = pygame.time.Clock()

while running:
    milliseconds=clock.tick(FPS)
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            running=False
        elif(event.type==pygame.KEYDOWN):
            if(event.key==pygame.K_ESCAPE):
                running=False
    pygame.display.flip()

pygame.quit()