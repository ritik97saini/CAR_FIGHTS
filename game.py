import pygame
import time
import random
pygame.init()
surf=pygame.display.set_mode((800,600))
pygame.display.set_caption("game")

fps=60
clock=pygame.time.Clock()
car1=pygame.image.load('1.png')
car2=pygame.image.load('2.png')
grass=pygame.image.load('grass.png')
font=pygame.font.SysFont("comicsansms",50)
def showtext(msg,g,h) :
    text=font.render(msg,True,(255,0,0))
    surf.blit(text,(g,h))
    

def carshow(x1,y1,x2,y2) :
    surf.blit(car1,(x1,y1))
    surf.blit(car2,(x2,y2))
def showgrass(p,i) :
	surf.blit(grass,(int(patch[i][0]),(7-i)*100+p))
	surf.blit(grass,(int(patch[i][1]),(7-i)*100+p))
	
car1_mask=pygame.mask.from_surface(car1)
car2_mask=pygame.mask.from_surface(car2)
grass_mask=pygame.mask.from_surface(grass)
crash_sound=pygame.mixer.Sound("Crash.wav")

def crash (x1,x2,y1,y2,p) :
    for i in range(0,8):
        x=int(patch[i][0])
        y=(7-i)*100+p
        offset=(int(x-x1),int(y-y1))
        result1=car1_mask.overlap(grass_mask,offset)
        offset=(int(x-x2),int(y-y2))
        result2=car2_mask.overlap(grass_mask,offset)
        if result1:
                return 1
        if result2:
                return 2

        x=int(patch[i][1])
        y=(7-i)*100+p
        offset=(int(x-x1),int(y-y1))
        result1=car1_mask.overlap(grass_mask,offset)
        offset=(int(x-x2),int(y-y2))

        result2=car2_mask.overlap(grass_mask,offset)
        if result1:
                return 1
        if result2:

                return 2	
		
        
crashed =False
out = True
while out :
    patch=[]
    x1=600
    y1=500
    x2=100
    y2=500
    pygame.key.set_repeat(1,28)
    p=0
    paused=False
    for i in range(0,8) :
        patch.append((-1000,-1000))

    
    
    while not crashed:
                for event in pygame.event.get():
                        keys=pygame.key.get_pressed()
                        if event.type == pygame.QUIT :
                                crashed=True
                if event.type == pygame.KEYDOWN :
                    if keys[pygame.K_ESCAPE] :
                        paused=True
               ################################ PAUSING ##############################################
                while paused :
                    
                    for event in pygame.event.get():
                        keys=pygame.key.get_pressed()
                    
                   
                    if event.type == pygame.KEYDOWN :
                        if keys[pygame.K_SPACE] :
                            paused=False
                    surf.fill((255,255,255))
                    showtext("press space to continue",150,300)
                    pygame.display.update()
                    clock.tick(30)    
                ###############################################################################       
                #####################################  cars movement #########################################
                if event.type == pygame.KEYDOWN :
                        if keys[pygame.K_LEFT] :
                            if (y1-y2<100) and (y1-y2>-100) and x1-x2==50 :    x1-=0
                            else : x1-=5
                        if keys[pygame.K_RIGHT] :    
                            if y1-y2<100 and y1-y2>-100 and x2-x1==50 :    x1+=0
                            else : x1+=5
                        if keys[pygame.K_UP] :
                            if (x1-x2<50) and (x1-x2>-50) and y1-y2==100 :    y1-=0
                            else : y1-=5
                        if keys[pygame.K_DOWN] :
                            if x1-x2<50 and x1-x2>-50 and y2-y1==100 :    y1+=0
                            else : y1+=5
                        if keys[pygame.K_a] :
                            if y1-y2<100 and y1-y2>-100 and x2-x1==50 :    x2-=0
                            else : x2-=5
                        if keys[pygame.K_d] :    
                            if y1-y2<100 and y1-y2>-100 and x1-x2==50:    x2+=0
                            else : x2+=5
                        if keys[pygame.K_w] :    
                            if x1-x2<50 and x1-x2>-50 and y2-y1==100 :    y2-=0
                            else : y2-=5
                        if keys[pygame.K_s] :
                            if x1-x2<50 and x1-x2>-50 and y1-y2==100:    y2+=0
                            else : y2+=5
                x1=max(x1,0)
                x2=max(x2,0)
                y1=max(y1,0)
                y2=max(y2,0)
                x1=min(x1,750)
                x2=min(x2,750)
                y1=min(y1,500)
                y2=min(y2,500)
                            
                         ##############################################################################################     
                            
                #######################################  grassss patches    ###############################################
                p+=5
                if p==100 :
                        p=0
                        obj=patch[0]
                        patch.pop(0)
                        patch.append((random.uniform(0,750),random.uniform(0,750)))
                
                                    
                                    
                surf.fill((173,255,47))
                for i in range(0,8) :
                     showgrass(p,i)
                ############################################################################################################
                ###################################### car crash ###########################################################     
                carshow(x1,y1,x2,y2)
                k=crash(x1,x2,y1,y2,p)
                if k==1 :
                    pygame.mixer.Sound.play(crash_sound)
                    surf.fill((255,255,255))
                    showtext("car 2 won",300,300)
                    pygame.display.update()
                    time.sleep(2)
                    crashed=True
                elif k==2 :
                    pygame.mixer.Sound.play(crash_sound)
                    surf.fill((255,255,255))
                    showtext("car 1 won",300,300)
                    pygame.display.update()
                    time.sleep(2)
                    crashed=True
                

                pygame.display.update()
                clock.tick(60)
    surf.fill((255,255,255))            
    showtext("press q to quit",275,250)
    showtext("or",400,300)
    showtext("p to play",350,350)
    pygame.display.update()
    for event in pygame.event.get():
                        keys=pygame.key.get_pressed()
                        if event.type == pygame.KEYDOWN :
                            if keys[pygame.K_q] :
                                out= False
                            elif keys[pygame.K_p]:
                                crashed=False
                            
    pygame.display.update()
             
pygame.quit()
quit()
