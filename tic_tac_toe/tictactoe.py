import pygame as pg
import sys
import time
from pygame.locals import *

xo='x'

winner = None
draw=None
width=400
height=400
white = (255,255,255)

line_color=(0,0,0)

board=[[None]*3,[None]*3,[None]*3]

pg.init()

fps=30
clock=pg.time.Clock()

screen=pg.display.set_mode((width,height+100),0,32)

pg.display.set_caption("Tic Tac Toe")
initial_window=pg.image.load("banner.png")
x_img=pg.image.load("cross.png")
y_img=pg.image.load("zero.png")


initial_window=pg.transform.scale(
    initial_window,
    (width,height+100)

)
x_img=pg.transform.scale(
    x_img,
    (80,80)
)

y_img=pg.transform.scale(
    y_img,
    (80,80)
)

def game_initial_window():
    screen.blit(initial_window,(0,0))
    pg.display.update()
    time.sleep(3)
    screen.fill(white)

    pg.draw.line(screen,line_color,(width/3,0),(width/3,height),7)
    pg.draw.line(screen, line_color, (width / 3 *2, 0), (width / 3 *2, height), 7)

    pg.draw.line(screen, line_color, (0, height/3), (width, height/3), 7)
    pg.draw.line(screen, line_color, (0, height/3 * 2), (width, height / 3 *2), 7)
    #pg.display.update()
    #time.sleep(10)
    draw_status()

def draw_status():
    global draw
    if winner is None:
        message=xo.upper()+"'s Turn"
    else:
        message=winner.upper() + "won"
    if draw:
        message=" game draw !"


    font=pg.font.Font(None,30)
    text=font.render(message,2,(255,255,255))
    screen.fill((0,0,0),(0,400,500,100))
    text_rect=text.get_rect(center=(width/2,500-50))
    screen.blit(text,text_rect)
    pg.display.update()
    time.sleep(10)

game_initial_window()

def check_win():
    global board,winner,draw

    for row in range(0,3):

        #check for horizontal winner

        if((board[row][0] == board[row][1]) and (board[row][1] == board[row][2])
                and board[row][0] is not None):
            winner=board[row][0]
            pg.draw.line(screen,(250,0,0),((row + 1)*width/3 -width/6 ,0),
                         ((row+1)*width/3 - width/6,height),4)
            break

        # check for vertical winner
        for col in range(0,3):
            if ((board[0][col] == board[1][col]) and (board[1][col] == board[2][col])
                    and board[0][col] is not None):
                winner = board[0][col]
                pg.draw.line(screen, (250, 0, 0), ((col + 1) * width / 3 - width / 6, 0),
                             ((col + 1) * width / 3 - width / 6, height), 4)
                break



        # check for diagonal winner

        #Left diagonal

        if(board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
            winner=board[0][0]
            pg.draw.line(screen,(250,70,70),(50,50),(350,350),4)

        # Right Diagonal
        if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
            winner = board[0][2]
            pg.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)




        # Draw everything

        draw_status()
