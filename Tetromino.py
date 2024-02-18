from Elements import *
import pygame

X = 50
Y = 50
ssq = 25
width = 1

class Tetromino:
    def __init__(self,screen,board,eltos,shape):
        self.screen = screen
        self.board = board
        self.x = 3
        self.shape = shape
        self.color = (eltos.color_pieces)[self.shape]
        self.states = (eltos.states)[self.shape]
        self.nstates = len(self.states)
        
        self.rotation = 0
        
        self.y = -self.lim('U')
        
    def rotate(self):   
        self.rotation = (self.rotation+1)%self.nstates
        if (not self.board.checkCol(self)):
            self.rotation = (self.rotation-1)%self.nstates
        
    def move(self,d):
        z = {'L' : (self.x>0-self.lim(d),-1),
             'R' : (self.x<10-self.lim(d),1)}
        old = self.x
        if z[d][0]:
            self.x += z[d][1]
            if (not self.board.checkCol(self)):
                self.x = old
        
        
    def fall(self):
        self.y += 1
                
    def lim(self,ch):
        d = {'L':(True,0,3,1,0),
             'R':(True,3,0,-1,1),
             'U':(False,0,3,1,0),
             'D':(False,3,0,-1,1)}
        t = d[ch]
        if t[0]:
            m = self.transpost(self.states[self.rotation])
        else:
            m = self.states[self.rotation]
        for i in range(t[1],t[2],t[3]):
            if m[i]!=[' ',' ',' ',' ']:
                return i+t[4]
                
    def transpost(self,m):
        def nullMat(x,y):
            n = [None]*4
            for i in range(y):
                n[i] = [None]*x
            return n
        
        n = nullMat(4,4)
        for i in range(4):
            for j in range(4):
                n[i][j] = m[j][i]
        return n
        
    def draw(self):
        for i in range(4):
            for j in range(4):
                if self.states[self.rotation][i][j]=='#':
                    r=pygame.Rect((X+(self.x+j)*ssq,Y+(self.y+i)*ssq,ssq,ssq))
                    pygame.draw.rect(self.screen,self.color,r)
                    pygame.draw.rect(self.screen,(0,0,0),r,width)