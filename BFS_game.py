import pygame
import random
import os.path
import inspect
import threading
import time
import sys
pygame.init()
pygame.font.init()


def bfs(N,ij,start,end):
    discovered = []  
    queue = [] 
    pred = {}
    discovered.append(start)
    queue.append(start)
    neighbours={}
    path=[]
    #red.append(start)
    #print("Visit: ")
    while queue:
        s = queue.pop(0)
        #print(f'{s}', end=" --> ")
        neighbours[s]=[]
        si=s[0]
        sj=s[1]
        print(f'neighbours of {s}',end= " : ")

        #find neighbours of s
        for i in range(si-1,-1,-1):
            if((i,sj) not in discovered and (i,sj) not in ij):
                neighbours[s].append((i,sj))
            else:
                break

        for j in range(sj-1,-1,-1):
            if((si,j) not in discovered and (si,j) not in ij):
                neighbours[s].append((si,j))
            else:
                    break
        
        print("  ",end="")
        for i in range(si+1,N):
            if((i,sj) not in discovered and (i,sj) not in ij):
                neighbours[s].append((i,sj))
            else:
                break

        for j in range(sj+1,N):
            if((si,j) not in discovered and (si,j) not in ij):
                neighbours[s].append((si,j))
            else:
                    break
 
        print(f'{neighbours[s]}')

        for neighbour in neighbours[s]:
            if neighbour not in discovered:
                if(neighbour == end):
                    print(neighbour)
                    path.append(neighbour)
                    print(s)
                    path.append(s)
                    while(s != start):
                        s=pred[s]
                        print(s)
                        path.append(s)
                    path.reverse()
                    return path,neighbours
                else:
                    discovered.append(neighbour)
                    queue.append(neighbour)
                    pred[neighbour]=s
 
WHITE = (255,255,255)
GREEN = (124,252,0)
RED = (255,0,0)
#BLUE = (0,0,200)
#LIGHT_BLUE = (0,0,100)



N=20

start=(0,0)
end = (N-1,N-1)

filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(filename))
print(path)
print(filename)

class Cell:
   
    allCellsMap={}    #(x,y) ->self
    size=50

    #CURRENT_EPOCH_COLOR=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    
    def __init__(self, posX, posY):
              
        self.posX=posX
        self.posY=posY
        self.color = WHITE
        Cell.allCellsMap[(self.posX,self.posY)]= self

class Mouse:

    def __init__(self, posX=start[0], posY=start[1]):
        self.posX=posX
        self.posY=posY
        self.mouseSizeX=Cell.size
        self.mouseSizeY=Cell.size
        self.image = pygame.transform.scale(pygame.image.load(path + "/mouse.png"),(self.mouseSizeX-self.mouseSizeX/8,self.mouseSizeY-self.mouseSizeY/8))
        self.moveToPositions=[]
        self.position=0


for i in range(0,N):
    for j in range(0,N):
        Cell(i,j)

mouse = Mouse(start[0],start[1])



pygame.init()
pygame.font.init()

screenSizeX=N*Cell.size
screenSizeY=N*Cell.size

maxCellsX=screenSizeX/Cell.size
maxCellsY=screenSizeY/Cell.size

screen = pygame.display.set_mode((screenSizeX, screenSizeY), 0)

mouseDrawingPositions=[]

playerSpawns=False
drawing = False


delay=1000

visitedNodes={}

 
while(True):
                
    screen.fill(0)

    if(mouse.moveToPositions):
        delay=500
        move=mouse.moveToPositions.pop(0)
        mouse.posX= move[0]*Cell.size
        mouse.posY= move[1]*Cell.size
        print("MOUSE MOVED:")
        print(mouse.posX)
        print(mouse.posY)
        if(not mouse.moveToPositions):
            temp=start
            start=end
            end = temp
            #test reset BLUE
            for key in visitedNodes.keys():
                    Cell.allCellsMap[key].color=WHITE
                    for neighbour in visitedNodes[key]:
                        Cell.allCellsMap[neighbour].color=WHITE

    else:
        delay=60

    
    
           
    #draw Cells
    for key in Cell.allCellsMap.keys():
        cell=Cell.allCellsMap[key]  
        if((cell.posX,cell.posY) == start):
            cell.color=GREEN
        elif((cell.posX,cell.posY) == end):
            cell.color=RED
        

        #pygame.draw.rect(screen,cell.color,((cell.posX+10)*Cell.size, (cell.posY+10)*Cell.size, Cell.size, Cell.size
        s = pygame.Surface((Cell.size-2,Cell.size-2))  # size of rect
        #s.set_alpha(50)                # alpha level
        s.fill(cell.color)           # fills entire surface
        screen.blit(s, (cell.posX*Cell.size,cell.posY*Cell.size))
        
            
    #draw player spawning cells       
    ###draw.rect will not draw alpha .. so :
    for showDrawingRect in mouseDrawingPositions:  
        s = pygame.Surface((Cell.size,Cell.size))  # size of rect
        s.set_alpha(50)                # alpha level
        s.fill((0,0,0))           # fills entire surface
        screen.blit(s, (showDrawingRect[0],showDrawingRect[1]))

    #draw mouse
    screen.blit(mouse.image,(mouse.posX,mouse.posY))
    
    
    #events
    for event in pygame.event.get():
    
        if(event.type == pygame.QUIT):
             pygame.display.quit()
             pygame.quit()
             sys.exit()
        
        if(event.type == pygame.MOUSEBUTTONDOWN):
            drawing=True
        
        if(event.type == pygame.MOUSEBUTTONUP):
            drawing=False  
         
        if(event.type == pygame.MOUSEMOTION and drawing):
            mousePos= (pygame.mouse.get_pos()[0]- (pygame.mouse.get_pos()[0]%Cell.size)  ,  pygame.mouse.get_pos()[1]- (pygame.mouse.get_pos()[1]%Cell.size)    )     
            if(mousePos not in mouseDrawingPositions):
                mouseDrawingPositions.append(mousePos)          
       
        if(event.type == pygame.KEYDOWN):
                
            if(event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN):
                print("BLOCKED:")
                print(mouseDrawingPositions)
                blockedPositions= [(mouseDrawingPositions[i][0]//Cell.size,mouseDrawingPositions[i][1]//Cell.size) for i in range(0,len(mouseDrawingPositions))]
                print(blockedPositions)
                print("BFS:")

                mouse.moveToPositions,visitedNodes= bfs(N,blockedPositions,start,end)
                print("MOUSE WILL MOVE TO:")
                print(mouse.moveToPositions)

                """
                #TEST
                for key in visitedNodes.keys():
                    for neighbour in visitedNodes[key]:
                        Cell.allCellsMap[neighbour].color=LIGHT_BLUE
                    Cell.allCellsMap[key].color=BLUE
                """




            if(event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE or event.key == pygame.K_CLEAR  ):
                if(len(mouseDrawingPositions)>0):
                    mouseDrawingPositions.pop()
                    
    pygame.display.update()     
    pygame.time.delay(delay)
      

    
    
    
    

