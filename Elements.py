class Elements:
    def __init__(self):  
        self.shapes = ['T','l','L','s','S','I','O']
        self.color_pieces = {'T':(255,0,0),
                             'l':(0,255,0),
                             'L':(0,0,255),
                             's':(255,0,255),
                             'S':(255,255,0),
                             'I':(0,255,255),
                             'O':(255,128,0)}

        T = [None]*4
        T[0] = [[' ',' ',' ',' '],
                [' ',' ',' ',' '],
                ['#','#','#',' '],
                [' ','#',' ',' ']
               ]            
        T[1] = [[' ',' ',' ',' '],
                [' ','#',' ',' '],
                ['#','#',' ',' '],
                [' ','#',' ',' ']
               ]           
        T[2] = [[' ',' ',' ',' '],
                [' ','#',' ',' '],
                ['#','#','#',' '],
                [' ',' ',' ',' ']
               ]            
        T[3] = [[' ',' ',' ',' '],
                [' ','#',' ',' '],
                [' ','#','#',' '],
                [' ','#',' ',' ']
               ]
        
        l = [None]*4
        l[0] = [[' ',' ',' ',' '],
                [' ',' ',' ',' '],
                ['#','#','#',' '],
                [' ',' ','#',' ']
               ]            
        l[1] = [[' ',' ',' ',' '],
                [' ','#',' ',' '],
                [' ','#',' ',' '],
                ['#','#',' ',' ']
               ]           
        l[2] = [[' ',' ',' ',' '],
                ['#',' ',' ',' '],
                ['#','#','#',' '],
                [' ',' ',' ',' ']
               ]            
        l[3] = [[' ',' ',' ',' '],
                [' ','#','#',' '],
                [' ','#',' ',' '],
                [' ','#',' ',' ']
               ]
                     
        L = [None]*4
        L[0] = [[' ',' ',' ',' '],
                [' ',' ',' ',' '],
                ['#','#','#',' '],
                ['#',' ',' ',' ']
               ]            
        L[1] = [[' ',' ',' ',' '],
                ['#','#',' ',' '],
                [' ','#',' ',' '],
                [' ','#',' ',' ']
               ]           
        L[2] = [[' ',' ',' ',' '],
                [' ',' ','#',' '],
                ['#','#','#',' '],
                [' ',' ',' ',' ']
               ]            
        L[3] = [[' ',' ',' ',' '],
                [' ','#',' ',' '],
                [' ','#',' ',' '],
                [' ','#','#',' ']
               ]
                     
        s = [None]*2
        s[0] = [[' ',' ',' ',' '],
                [' ',' ',' ',' '],
                [' ','#','#',' '],
                ['#','#',' ',' ']
               ]            
        s[1] = [[' ',' ',' ',' '],
                [' ','#',' ',' '],
                [' ','#','#',' '],
                [' ',' ','#',' ']
               ]
                     
        S = [None]*2
        S[0] = [[' ',' ',' ',' '],
                [' ',' ',' ',' '],
                ['#','#',' ',' '],
                [' ','#','#',' ']
               ]            
        S[1] = [[' ',' ',' ',' '],
                [' ',' ','#',' '],
                [' ','#','#',' '],
                [' ','#',' ',' ']
               ]
                     
        I = [None]*2
        I[0] = [[' ',' ',' ',' '],
                [' ',' ',' ',' '],
                ['#','#','#','#'],
                [' ',' ',' ',' ']
               ]            
        I[1] = [[' ',' ','#',' '],
                [' ',' ','#',' '],
                [' ',' ','#',' '],
                [' ',' ','#',' ']
               ]
                     
        O = [None]*1
        O[0] = [[' ',' ',' ',' '],
                [' ','#','#',' '],
                [' ','#','#',' '],
                [' ',' ',' ',' ']
               ]

        self.states = {'T':T,
                       'l':l,
                       'L':L,
                       's':s,
                       'S':S,
                       'I':I,
                       'O':O}
                       
        self.posy = {'T':-2,
                     'l':-2,
                     'L':-2,
                     's':-2,
                     'S':-2,
                     'I':-2,
                     'O':-1}
