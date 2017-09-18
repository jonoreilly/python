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
        
        



















        




















