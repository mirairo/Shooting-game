import pygame, sys
from pygame import *
import random
pygame.init()
#####################################################################
size=(1000,590)
screen=pygame.display.set_mode(size)   
pygame.display.set_caption("Version 0.1_dev>gooblU_under:>Python_2.7")
#####################################################################
col_1=(242,225,31)
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)
green=(0,200,0)
black=(0,0,0)
yellow=(50,200,0)
font = pygame.font.Font(None, 20)
#####################################################################
label1=False
label2=False
label3=False
label4=False
label5=False
bullt =False
upp=True
downn=False
leftt=False
rightt=False
####################################################################
score=20
scr=0
x=350
y=440
dx=8
dy=8
p=600
q=300
n=440
tempx=0
vl=0
v=0
a=600
b=100
aa=600
bb=200
vt=0
zz=[]
for i in range(0,40):
       k = random.randrange(0,900)
       zz.append(k)
d11=[]       
for i in range(0,40):
       k = random.randrange(0,900)
       d11.append(k)
d111=[]
for i in range(0,40):
       k = random.randrange(0,900)
       d111.append(k)       
####################################################################
img1=pygame.image.load('pp1.gif')
img2=pygame.image.load('bn.jpg')
img3=pygame.image.load('b1.jpg')
img4=pygame.image.load('b1.jpg')
img5=pygame.image.load('brck.png')
img6=pygame.image.load('brck.png')
img7=pygame.image.load('vlnn.gif')
img8=pygame.image.load('left.gif')
img9=pygame.transform.flip(img8,True,False)
img10=pygame.image.load('frnt.gif')
img11=pygame.image.load('s1.png')
img12=pygame.image.load('bbk.jpg')
img13=pygame.image.load('gf.png')
img14=pygame.image.load('end.jpg')
####################################################################
bl=[]
for i in range(0,40):
       k = random.randrange(0,900)
       bl.append([k,0])
       
d1=[]
for i in range(0,40):
       k = random.randrange(0,1000)
       d1.append([k,0])
d2=[]
for i in range(0,40):
       k = random.randrange(0,600)
       d2.append([0,k])  
cnt=0       
#####################################################################
clock = pygame.time.Clock()
#####################################################################
#########################START_SCREEN################################
while True:

    while label1==False:
        for event in pygame.event.get():	
            if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
            if event.type ==pygame.MOUSEBUTTONDOWN:
               m,n=pygame.mouse.get_pos() 	
               if m> 320 and m<460:
                  if n>230 and n<290:   
                     label1=True
                     label2=False  
                     
        font = pygame.font.Font(None, 20)             
                     
        screen.blit(img12, [100,0])            
        for i in range(0,40):
           d11[i]=random.randrange(1,40) 	
        for i in range(0,40):
           pygame.draw.line(screen, blue,[d1[i][0],d1[i][1]],[d1[i][0],d1[i][1]+8] ,2)
           d1[i][1]+=d11[i]
         
        for i in range(0,20):
            if d1[i][1] >600:
               d1[i][1]=0
        for i in range(21,30):
            if d1[i][1] >500:
               d1[i][1]=0      
        for i in range(31,40):
            if d1[i][1] >400:
               d1[i][1]=0  
               
        for i in range(0,40):
           d111[i]=random.randrange(1,40) 	
        for i in range(0,40):
           pygame.draw.line(screen, yellow,[d2[i][0],d2[i][1]],[d2[i][0]+8,d2[i][1]] ,2)
           d2[i][0]+=d111[i]   
           
        for i in range(0,20):
            if d2[i][0] >1000:
               d2[i][0]=0
        for i in range(21,30):
            if d2[i][0] >800:
               d2[i][0]=0      
        for i in range(31,40):
            if d2[i][0] >600:
               d2[i][0]=0     
           
           
           
           
           
           
        fontt = pygame.font.Font(None, 40)
        fonttt = pygame.font.Font(None, 20)
        fontttt = pygame.font.Font(None, 30)
        fon = pygame.font.Font(None, 30)
        text = fon.render("        Click to Start   ",True,red)
        screen.blit(text, [350,250])   
        text = fontt.render("   Shooting Game   ",True,white)
        screen.blit(text, [350,280])
        text = fontttt.render("Developed with Python 2.7   ",True,white)
        screen.blit(text, [350,320])
        text = fonttt.render("                   by Gooblu  ",True,white)
        screen.blit(text, [350,350])   
        pygame.display.flip()
        clock.tick(20)
 #################################################################################       
    while label2==False:
        for event in pygame.event.get():	
            if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
        screen.fill(black)       
        keys = pygame.key.get_pressed()
 	  
        if keys[K_RETURN]:       
           label2=True
           label3=False  
                     
                     
                     
        screen.blit(img13, [200,100])            
        
           
           
           
           
           
           
           
        text = font.render("       Press Enter to continue  ",True,blue)
        screen.blit(text, [380,220])   
        text = font.render("       Hit your enemy to score points.  ",True,blue)
        screen.blit(text, [380,420])    
        text = font.render("       If score exceeds 1000 you win  ",True,blue)
        screen.blit(text, [380,435]) 
        text = font.render("       Maximum health is 20 .  ",True,blue)
        screen.blit(text, [380,450]) 
        text = font.render("       Use Space bar to shoot  .  ",True,blue)
        screen.blit(text, [380,465])
        pygame.display.flip()
        clock.tick(20)    
#######################################################################        
######################MAIN PROGRAM#####################################  



    while label3==False:
    	screen.fill(black)    
        for event in pygame.event.get():	
            if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
            if event.type ==pygame.MOUSEBUTTONDOWN:
               m,n=pygame.mouse.get_pos() 	
               if m> 860 and m<930:
                  if n>470 and n<520:     
                     label3=True
                     label4=False
                
        
        screen.blit(img2,[0,0])
        
        screen.blit(img11,[0,0])
        for i in range(0,26):
            screen.blit(img3,[0+40*i,100])
        for i in range(0,26):
            screen.blit(img3,[0+40*i,570])
        tx=x
        ty=y
        
        
        keys = pygame.key.get_pressed()
        if keys[K_SPACE]:
           bullt=True 
        if keys[K_LEFT] and keys[K_DOWN] :
           x-=dx
           y+=dy
          
           rightt=False
           leftt=True
           upp=False
           downn=True 
                     
        elif keys[K_LEFT] and keys[K_UP] :
           x-=dx
           y-=dy
          
           rightt=False
           leftt=True
           upp=True
           downn=False       
        elif keys[K_LEFT] and keys[K_DOWN] :
           x-=dx
           y+=dy
       
           rightt=False
           leftt=True
           upp=False
           downn=True 
        elif keys[K_RIGHT] and keys[K_DOWN] :
           x+=dx
           y+=dy
           
           rightt=True
           leftt=False
           upp=False
           downn=True
        elif keys[K_RIGHT] and keys[K_UP] :
           x+=dx
           y-=dy
           
           
           rightt=True
           leftt=False
           upp=True
           downn=False
        elif keys[K_LEFT]:
           x-=dx
          
           leftt=True
           rightt=False
           upp=False
           downn=False
        elif keys[K_RIGHT]:
           x+=dx
          
           rightt=True
           leftt=False
           upp=False
           downn=False   
        elif keys[K_UP]:
           y-=dy
           
           upp=True
           leftt=False
           rightt=False
           downn=False
        elif keys[K_DOWN]:
           y+=dy
           
           downn=True
           leftt=False
           rightt=False
           upp=False
            
        if x>400:
       	   x=tx     
        if y<200:
           y=ty
           
       # if y==120:       
        #   if x  in range(80,180): 
         #
        # y=ty
        #if y==296:       
         #  if x  in range(380,480):
          #    x=tx
           #   y=ty     
              
              
        
        
        
        
       
         
         
        if upp==True:
           screen.blit(img9,[x,y])
           
        elif leftt==True:
           screen.blit(img9,[x,y])
           
        elif rightt==True:
           screen.blit(img9,[x,y])
          
        elif downn==True:
           screen.blit(img9,[x,y])
          
        
        screen.blit(img8,[p,q])
        vl+=1
        if vl==20:
           p=random.randrange(500,1000)
           q=random.randrange(130,520)
           for i in range(0,30):   
               pygame.draw.line(screen, red,[p-25-25*i,q],[p-25*i-10,q],2)
           vl=0 
           if q>y-30 and q<y+30:
              score-=1
        
        screen.blit(img8,[a,b])
        v+=1
        if v==15:
           a=random.randrange(500,1000)
           b=random.randrange(130,520)
           for i in range(0,25):   
               pygame.draw.line(screen, red,[a-25-25*i,b],[a-25*i-10,b],2)
           v=0 
           if b>y-30 and b<y+30:
              score-=1
        
        screen.blit(img8,[aa,bb])
        vt+=1
        if vt==20:
           aa=random.randrange(500,1000)
           bb=random.randrange(130,520)
           for i in range(0,25):   
               pygame.draw.line(screen, red,[aa-25-25*i,bb],[aa-25*i-10,bb],2)
           vt=0 
           if bb>y-30 and bb<y+30:
              score-=1
              
              
        
           
        #if ( x not in range(80,180) or y<100) and ( x not in range(380,480) or y<300):   
        if bullt==True:
          
               
           if upp==True and rightt==True: 		   
              for i in range(0,9):   
                  pygame.draw.line(screen, blue,[x+10+25*i,y-25*i-10],[x+25+25*i,y-25-25*i],3)
                  if (y-25*i-10>b-10 and y-25*i-10<b+10) and (x+10+25*i>a-10 and x+10+25*i<a+10):
                     scr+=1
                  if (y-25*i-10>bb-10 and y-25*i-10<bb+10) and (x+10+25*i>aa-10 and x+10+25*i<aa+10):
                     scr+=1
                  if (y-25*i-10>q-10 and y-25*i-10<q+10) and (x+10+25*i>p-10 and x+10+25*i<p+10):
                      scr+=1   
           elif downn==True and rightt==True: 	
               for i in range(0,9):   
                   pygame.draw.line(screen, blue,[x+10+25*i,y+25*i+10],[x+22+25*i,y+25+25*i],3)                      
                   if (y+25*i+10>b-10 and y+25*i+10<b+10) and (x+10+25*i>a-10 and x+10+25*i<a+10):
                      scr+=1
                   if (y+25*i+10>bb-10 and y+25*i+10<bb+10) and (x+10+25*i>aa-10 and x+10+25*i<aa+10):
                      scr+=1
                   if (y+25*i+10>q-10 and y+25*i+10<q+10) and (x+10+25*i>p-10 and x+10+25*i<p+10):
                      scr+=1   
           elif rightt==True: 	
               for i in range(0,16):   
                   pygame.draw.line(screen, blue,[x+25+25*i,y+20],[x+40+25*i,y+20],3)  
                   if y+20>b-10 and y+20<b+10:
                      scr+=1
                   if y+20>bb-10 and y+20<bb+10:
                      scr+=1
                   if y+20>q-10 and y+20<q+10:
                      scr+=1     
           elif leftt==True: 	
               for i in range(0,16):   
                   pygame.draw.line(screen, blue,[x+25+25*i,y+20],[x+40+25*i,y+20],3)  
               if y+20>b-10 and y+20<b+10:
                  scr+=1
               if y+20>bb-10 and y+20<bb+10:
                  scr+=1
               if y+20>q-10 and y+20<q+10:
                  scr+=1     
           else:        
               for i in range(0,16):   
                   pygame.draw.line(screen, blue,[x+25+25*i,y+20],[x+40+25*i,y+20],3)
               if y+20>b-10 and y+20<b+10:
                  scr+=1
               if y+20>bb-10 and y+20<bb+10:
                  scr+=1
               if y+20>q-10 and y+20<q+10:
                  scr+=1    
        bullt=False
        for i in range(0,40):
           zz[i]=random.randrange(1,40) 	
        for i in range(0,40):
           pygame.draw.line(screen, blue,[bl[i][0],bl[i][1]],[bl[i][0],bl[i][1]+8] ,2)
           bl[i][1]+=zz[i]
        
        
        
             
              
              
      
       
        for i in range(0,10):
            if bl[i][1] >490:
               bl[i][1]=0
        for i in range(11,20):
            if bl[i][1] >370:
               bl[i][1]=0
        for i in range(21,30):
            if bl[i][1] >300:
               bl[i][1]=0 
        for i in range(31,40):
            if bl[i][1] >260:
               bl[i][1]=0       
         
        text = font.render("End the Game",True,black)
        screen.blit(text, [900,500])   
        text = font.render("Health : "+str(score),True,black)
        screen.blit(text, [900,480])
        text = font.render("Score  : "+str(scr),True,black)
        screen.blit(text, [900,460]) 
        screen.blit(img7,[900,520])
        
        
        if score<0:
           label3=True
           label4=False 
           label5=False
        elif scr>1000:
           label3=True
           label4=False 
           label5=True 	
        
        
        
        
        
        
        
        
        
       
        
        pygame.display.flip()
        clock.tick(20)
        
        
        
        
        
        
        
        
########################Restart#######################################        
        
    while label4==False:
        for event in pygame.event.get():	
            if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
            if event.type ==pygame.MOUSEBUTTONDOWN:
               m,n=pygame.mouse.get_pos() 	
               if m> 170 and m<230:
                  if n>270 and n<360:     
                     label4=True
                     label1=False
                     label5=False
                     score=20
                     scr=0
               if m>350    and m<400 :   
                  if n>380  and   n<420 :
                     pygame.quit()
                     sys.exit()  
           
        screen.fill(black)
        screen.blit(img14,[70,70])
        font = pygame.font.Font(None, 40)
        if label5==True:
            text = font.render("         YOU WIN   ",True,white)
            screen.blit(text, [400,300])
        else: 
            text = font.render("         YOU ARE DEAD   ",True,white)
            screen.blit(text, [400,300])
            
        text = font.render("Restart",True,yellow)
        screen.blit(text, [200,300])   
        text = font.render("Exit   ",True,red)
        screen.blit(text, [370,400])   
        pygame.display.flip()
        clock.tick(20) 
    
