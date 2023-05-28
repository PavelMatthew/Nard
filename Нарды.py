import pygame

#Окно

pygame.init()
clock =pygame.time.Clock()
FPS=10

win = pygame.display.set_mode((1166,1282))
pygame.display.set_caption("Пацанские Нарды")

piece_imgb = pygame.image.load("1.png")
piece_imgw = pygame.image.load("piecewhite.png")
bg = pygame.image.load("board.png")


x=0
y=0

#координаты картинки
a=0
b=30
c=0
d=30


run = True
while(run):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
                
                elif event.type==pygame.MOUSEBUTTONDOWN:
                        x,y=pygame.mouse.get_pos()
                #elif event.type==pygame.MOUSEBUTTONUP:
                        
                        #x,y=pygame.mouse.get_pos()

                
                
                
                        
        clock.tick(FPS)
        # доска
        win.blit(bg,(0,0))
        win.blit(piece_imgb,(x,y))
        #рисуем фишки
        '''for i in range(15):
                win.blit(piece_imgb,(60,810-30*i))
        for i in range(15):
                win.blit(piece_imgw,(806,60+30*i))'''
                

        pygame.display.update()
        
pygame.quit()

arr_sockets = [[0]*15 for i in range(24)]
#Массив ячеек на доске нард


class Piece:
        'Класс фишка'
#Класс фишка, которая стоит на доске
        color ='color'
#Цвет фишки белый или чёрный

white_piece = Piece()
white_piece.color = 'Белый'
black_piece = Piece()
black_piece.color ='Чёрный'
empty_piece = Piece()
empty_piece.color = 'Пусто'




for i in range(15):
        arr_sockets[0][i] = white_piece
for i in range(15):
        print(arr_sockets[0][i].color)
for i in range(15):
        arr_sockets[12][i] = black_piece
for i in range(15):
        print(arr_sockets[12][i].color)

        

