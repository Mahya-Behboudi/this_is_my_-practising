import pygame
def draw_board(the_board):
    pygame.init()
    color = [(255,0,0),(0,0,0)]
    n = len(the_board)
    surface_sizing = 500
    squre_sizing = surface_sizing //n
    surface_sizing = n*squre_sizing
    surface = pygame.display.set_mode((surface_sizing, surface_sizing))
    for row in range(n):
        c_index = row%2
        for col in range(n):
            the_squre = (col*squre_sizing,row*squre_sizing,squre_sizing,squre_sizing)
            surface.fill(color[c_index], the_squre)
            c_index = (c_index + 1)%2
    pygame.display.flip()
draw_board("nnnnnnnnnnnnn")
