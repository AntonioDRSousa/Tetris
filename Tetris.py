import pygame
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring
from random import randint
from Board import *
from Tetromino import *

sq = 25
xbox = 350
ybox = 470

zq = 7
xtable = 320
ytable = 50+2*sq

width=1

fps=60

class Tetris:
    def __init__(self):
        self.dimx = 10
        self.dimy = 20
        
        self.initScreen()
        self.font = pygame.font.SysFont('Comic Sans MS', 20)
        self.clock = pygame.time.Clock()
        
        self.loadHighscore()
        
        self.eltos = Elements()
        self.board = Board(self.dimx,self.dimy)
        self.coeficient_score=[0,40,100,300,1200]
        
        self.chooseLevel()
        
        self.start()
        
    def chooseLevel(self):
        while True:
            try:
                self.start_level = int(askstring(title='Start Level', prompt='Start Level : ',initialvalue="0"))
                if (self.start_level<0):
                    raise
                break
            except:
                showinfo('Error', 'Invalid Level .....')
        
    def initScreen(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600,600))
        pygame.display.set_caption("TETRIS")
        pygame.display.flip()
        
    def drawInf(self):
        states = self.eltos.states[self.shape2]
        
        r=pygame.Rect((xbox-sq,ybox-2*sq,sq*6,sq))
        pygame.draw.rect(self.screen,(0,0,0),r,width)
        text = self.font.render('NEXT',True,(0,0,0))
        self.screen.blit(text, (xbox+sq,ybox-2*sq))
        
        r=pygame.Rect((xbox-sq,ybox-sq,sq*6,sq*6))
        pygame.draw.rect(self.screen,(0,0,0),r,width)
        for i in range(4):
            for j in range(4):
                if states[0][i][j]=='#':
                    r=pygame.Rect((xbox+j*sq,ybox+i*sq,sq,sq))
                    pygame.draw.rect(self.screen,self.eltos.color_pieces[self.shape2],r)
                    pygame.draw.rect(self.screen,(0,0,0),r,width)
        
        text = self.font.render('STATISTICS',True,(0,0,0))
        self.screen.blit(text, (xtable+2*sq,ytable-2*sq))
        
        for k in range(len(self.eltos.shapes)): 
            states = self.eltos.states[self.eltos.shapes[k]]
            dy = k*6*zq
            
            r=pygame.Rect((xtable-zq,ytable-zq+dy,zq*6,zq*6))
            pygame.draw.rect(self.screen,(0,0,0),r,width)
            
            r=pygame.Rect((xtable+5*zq,ytable-zq+dy,200,zq*6))
            pygame.draw.rect(self.screen,(0,0,0),r,width)
            
            text = self.font.render(" "+str(self.statistics[self.eltos.shapes[k]]),True,(0,0,0))
            self.screen.blit(text, (xtable+5*zq,ytable-zq+dy))
            
            for i in range(4):
                for j in range(4):
                    if states[0][i][j]=='#':
                        r=pygame.Rect((xtable+j*zq,ytable+i*zq+dy,zq,zq))
                        pygame.draw.rect(self.screen,self.eltos.color_pieces[self.eltos.shapes[k]],r)
                        pygame.draw.rect(self.screen,(0,0,0),r,width)
                    
    def drawText(self):
        text_type = self.font.render('A-TYPE',True,(0,0,0))
        text_lines = self.font.render('LINES : '+str(self.nlines),True,(0,0,0))
        text_top = self.font.render('TOP     : '+str(self.top),True,(0,0,0))
        text_score = self.font.render('SCORE : '+str(self.score),True,(0,0,0))
        text_level = self.font.render('LEVEL : '+str(self.level),True,(0,0,0))
        
        self.screen.blit(text_type, (500,550))
        self.screen.blit(text_lines, (0,550))
        self.screen.blit(text_top, (0,0))
        self.screen.blit(text_score, (0,20))
        self.screen.blit(text_level, (0,570))
        
    def draw(self):
        self.board.draw(self.screen)
        self.piece.draw()
        self.drawInf()
        self.drawText()
        pygame.display.update()
        
    def calcSpeed(self):
        if self.level<9:
            return 48-self.level*5
        elif self.level==9:
            return 6
        elif self.level in range(10,13):
            return 5
        elif self.level in range(13,16):
            return 4
        elif self.level in range(16,19):
            return 3
        elif self.level in range(19,29):
            return 2
        else:
            return 1
        
    def step(self):
        if (self.board.checkCol(self.piece)) and (self.piece.y<self.board.dimy-self.piece.lim('D')):
            self.piece.fall()
        else:
            self.board.store(self.piece)
            z=self.board.clearLines()
            self.nlines += z
            self.score += self.coeficient_score[z]*(self.level+1)
            
            if self.start_level==self.level:
                sup1 = self.start_level*10+10
                sup2 = max(100, (self.start_level*10-50))
                if ((self.nlines>=sup1)or(self.nlines>=sup2)):
                    self.level+=1
            else:
                self.nl+=1
                if(self.nl==10):
                    self.nl=0
                    self.level+=1
            
            shape1 = self.shape2
            self.piece=Tetromino(self.screen,self.board,self.eltos,shape1)
            self.shape2 = self.eltos.shapes[randint(0,len(self.eltos.shapes)-1)]
            
            self.statistics[shape1] += 1
            
            if (not self.board.checkCol(self.piece)):
                return True
        return False
        
    def loadHighscore(self):
        fp = open("score/top.num",'r')
        self.highscores=fp.readlines()
        for i in range(len(self.highscores)):
            self.highscores[i]=int((self.highscores[i]).split('\n')[0])
        self.top = self.highscores[0]
        
    def saveHighscore(self):
        self.highscores.append(self.score)
        self.highscores.sort(reverse=True)
        self.highscores = self.highscores[:len(self.highscores)-1]
        for i in range(0,len(self.highscores)):
            self.highscores[i]=str(self.highscores[i])+"\n"
        fp = open("score/top.num","w")
        fp.writelines(self.highscores)
        
    def pause(self):
        p = True
        while p:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        exit()
                    elif event.key == pygame.K_p:
                        p = False
        
    def start(self):
        self.score = 0
        self.nlines = 0
        self.statistics = {'T':0,'l':0,'L':0,'s':0,'S':0,'I':0,'O':0}
        self.level = self.start_level
        
        # for counting lines after up start_level
        self.nl = 0
        
        shape1 = self.eltos.shapes[randint(0,len(self.eltos.shapes)-1)]
        self.shape2 = self.eltos.shapes[randint(0,len(self.eltos.shapes)-1)]
        
        self.statistics[shape1] += 1
        
        # count , max_count is used for separate fps of screen and speed of pieces
        count = 0
        self.calcSpeed()
        
        self.piece=Tetromino(self.screen,self.board,self.eltos,shape1)

        while True:
        
            if (count==self.calcSpeed()):
                if self.step():
                    showinfo('Game End','GAME END\n\nScore : '+str(self.score)+"\nLevel : "+str(self.level)+"\nTop : "+str(self.top))
                    self.saveHighscore()
                    break
                        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        exit()
                    elif event.key == pygame.K_p:
                        self.pause()
                        
                    elif event.key == pygame.K_LEFT:
                        self.piece.move('L')
                    elif event.key == pygame.K_RIGHT:
                        self.piece.move('R')
                    elif event.key == pygame.K_SPACE:
                        self.piece.rotate()
            
            count = (count+1)%(self.calcSpeed()+1)
            self.draw()
            self.clock.tick(fps)