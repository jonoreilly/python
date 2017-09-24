import pygame


index = {}

def add(msg, pos):
    index[msg] = pos


add("hand",(3,3))
hand = [[
    "                        ",
    "   BB                   ",
    "  BWWB                  ",
    " BWWWWB       BB        ",
    " BWWWWWB     BWWB       ",
    "  BWWWWWB   BBWWWB      ",
    "   BWWWWWB BWWBWWWB     ",
    "    BWWWWWBWWWWWWWB     ",
    "     BWWWWWBWWWWWWWB    ",
    "      BWWWWWWWWWWWWB    ",
    "       BWWWWWWWWWWWWB   ",
    "      BWBWWWWWWWWWWWB   ",
    "     BWWWBWWWWWWWWWWB   ",
    "     BWWWBBWWWWWWWWWWBB ",
    "     BWWWWWWWWWWWWWWBWWB",
    "      BWWWWWWWWWWWWBWWB ",
    "      BWWWWWWWWWWWBWWB  ",
    "       BBWWWWWWWWBWWB   ",
    "         BBBWWWWBWWB    ",
    "            BBWBWWB     ",
    "              BWWB      ",
    "              BWB       ",
    "               B        ",
    "                        "
    ],[
    "                        ",
    "                        ",
    "                        ",
    "     BB       BB        ",
    "    BWWB     BWWB       ",
    "   BWWWWB   BBWWWB      ",
    "  BWWWWWWB BWWBWWWB     ",
    "  BWWBWWWWBWWWWWWWB     ",
    "   BBBWWWWWBWWWWWWWB    ",
    "      BWWWWWWWWWWWWB    ",
    "       BWWWWWWWWWWWWB   ",
    "      BWBWWWWWWWWWWWB   ",
    "     BWWWBWWWWWWWWWWB   ",
    "     BWWWBBWWWWWWWWWWBB ",
    "     BWWWWWWWWWWWWWWBWWB",
    "      BWWWWWWWWWWWWBWWB ",
    "      BWWWWWWWWWWWBWWB  ",
    "       BBWWWWWWWWBWWB   ",
    "         BBBWWWWBWWB    ",
    "            BBWBWWB     ",
    "              BWWB      ",
    "              BWB       ",
    "               B        ",
    "                        "
    ]]



add("sword", (10,6))
sword = [[
    "          B             ",
    "         BWB            ",
    "        BWWB            ",
    "        BWWB            ",
    "        BWWB            ",
    "       BWWB    B        ",
    "       BWWB   BWB       ",
    "       BWWB   BWB       ",
    "      BWWB    BWB       ",
    "      BWWB    BWWB      ",
    "      BWWB     BWB      ",
    "     BWWB      BWB BB   ",
    "     BWWB       BBBBB   ",
    " BB  BWWB      BBBB     ",
    " BBBBWWB      BBBBB     ",
    "  BBBBBB      BB  BB    ",
    "   BBBBBB         BB    ",
    "    BBBBBB              ",
    "   BBB  BB              ",
    "   BBB                  ",
    "  BBB                   ",
    "                        ",
    "                        ",
    "                        "
    ],[
    "                    BB  ",
    "       B     BB    BB   ",
    "       BB   BB          ",
    "            B           ",
    "            B     BB    ",
    " BB    B        BBWB    ",
    "  BB  BBBB     BWWWB    ",
    "      BWWBB  BBWWWB     ",
    "      BBWWBBBWWWWWB  BBB",
    "       BWWWBWWWWWB      ",
    "       BBWBWWWWWB       ",
    "  B     BBWWWWWB        ",
    " BBB   BBWWWWWBB        ",
    " BBBB BBWWWWBBWBBB      ",
    "  BBBBBWWWWBBBWWWBB  BB ",
    "   BBBWWWWB  BBWWWBBBBB ",
    "   BBBWWWB    BBWWBBBB  ",
    "  BBBBBWB      BBBBBB   ",
    " BBBBBBB        BBBBBB  ",
    "BBBBBBBBBB     BBB BBBB ",
    "BBBBBB BBB     BB   BBB ",
    " BBB                    ",
    "  B                     ",
    "                        "
    ]]


class cursors ():
    def __init__ (self):
        self.size = (24,24)
        self.selected = None
        self.hand = pygame.cursors.compile(hand[0],black="B",white="W",xor="o"),pygame.cursors.compile(hand[1],black="B",white="W",xor="o")
        self.sword = pygame.cursors.compile(sword[0],black="B",white="W",xor="o"),pygame.cursors.compile(sword[1],black="B",white="W",xor="o")
        self.cursormask = self.hand
        self.data,self.mask = self.cursormask[0]
        self.point = index["hand"]
        pygame.mouse.set_cursor(self.size, self.point, self.data, self.mask)

    def pressed(self):
        self.data,self.mask = self.cursormask[1]
        pygame.mouse.set_cursor(self.size, self.point, self.data, self.mask)

    def released(self):
        self.data,self.mask = self.cursormask[0]
        pygame.mouse.set_cursor(self.size, self.point, self.data, self.mask)

    def setmask(self, mask):
        exec ("self.cursormask = self.%s" % (mask))
        self.point = index[mask]
        
        





def readmouse(mouse, units):
    attacking = False
    target = None
    mouse.setmask("hand")
    #set flags and mouse icon if mous touching item
    for item in units:
        item.selected = False
        if item.status == "alive":
            if item.pos[0] - item.size[0]/2 <  pygame.mouse.get_pos()[0] < item.pos[0] + item.size[0]/2:
                if item.pos[1] - item.size[1]/2 <  pygame.mouse.get_pos()[1] < item.pos[1] + item.size[1]/2:
                    if item.team == "enemy":
                        mouse.setmask("sword")
                    target = item
                    target.selected = True

    #actions if clicked
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  #1-left, 2-wheel, 3-right
                mouse.pressed()
                if target == None:
                    mouse.selected = None
                elif target.team == "player":
                    mouse.selected = target
                    target.selected = True
            if event.button == 3 and mouse.selected != None:
                if mouse.selected.team == "player":
                    if target == None:                           
                        mouse.selected.attack = False
                        mouse.selected.target = None
                        mouse.selected.setdirection(pygame.mouse.get_pos())
                    else:
                        if target.team == "enemy":
                            mouse.selected.attack = True
                            mouse.selected.target = target
                            mouse.selected.setdirection(target.pos)
                        else:
                            mouse.selected.attack = False
                            mouse.selected.target = None
                            mouse.selected.setdirection(pygame.mouse.get_pos())
                            
                    mouse.pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
    if not pygame.mouse.get_pressed()[0] and not pygame.mouse.get_pressed()[2]:
        mouse.released()
    if mouse.selected != None:
        mouse.selected.selected = True



















        




















