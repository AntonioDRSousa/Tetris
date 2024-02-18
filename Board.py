import pygame

X = 50
Y = 50
ssq = 25
width = 1

class Board:
    def __init__(self,dimx,dimy):
        self.dimx = dimx
        self.dimy = dimy
        self.grid = [None]*dimy
        self.void = (128,128,128)
        for i in range(dimy):
            self.grid[i] = [None]*dimx
            for j in range(dimx):
                self.grid[i][j]=self.void
            
    def checkCol(self,piece):
        for i in range(4):
            for j in range(4):
                b1 = piece.states[piece.rotation][j][i]=='#'
                if ((piece.y+j)<19)and((piece.x+i)<10):
                    b2 = self.grid[piece.y+1+j][piece.x+i]!=self.void
                else:
                    b2 = False
                if (b1 and b2):
                    return False
        return True

    def store(self,piece):
        for i in range(4):
            for j in range(4):
                if piece.states[piece.rotation][j][i]=='#':
                    self.grid[piece.y+j][piece.x+i] = piece.color
                    
    def clearLines(self):
        nlines=0
        for i in range(self.dimy):
            b = True
            for j in range(self.dimx):
                if self.grid[i][j]==self.void:
                    b=False
            if b:
                nlines+=1
                for ky in range(i,0,-1):
                    for kx in range(0,self.dimx):
                        self.grid[ky][kx] = self.grid[ky-1][kx]
                for kx in range(0,self.dimx):
                    self.grid[0][kx] = self.void
        return nlines
     
    def draw(self,screen):
        screen.fill((255,255,255))
        
        pygame.draw.rect(screen,(0,0,0),pygame.Rect((X,Y,10*ssq,20*ssq)),20)
        
        for i in range(self.dimy):
            for j in range(self.dimx):
                r=pygame.Rect((X+j*ssq,Y+i*ssq,ssq,ssq))
                pygame.draw.rect(screen,self.grid[i][j],r)
                pygame.draw.rect(screen,(0,0,0),r,width)