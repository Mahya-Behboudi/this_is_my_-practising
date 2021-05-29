import pygame
import time
def p():
    pygame.init()
    main_surface = pygame.display.set_mode((500,400))
    set_rectangular = (10,20,70 , 35)
    set_color = (0,0,255)
    colors = [(255,0,0),(0,0,0)]
    my_font = pygame.font.SysFont("Nunito-ExtraBold", 20, bold=True, italic=False)
    the_text = my_font.render("hello", True, (0,0,0))
    main_surface.blit(the_text,(0,0))
    # image =pygame.image.load("Image_created_with_a_mobile_phone.png")          #intrduce the image 
    frame_count = 0
    frame_rate = 0
    to = time.process_time()
    while True:
        # ................................ about the event...........................................................
        ev=pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        if ev.type == pygame.KEYDOWN:
            key = ev.dict["key"]
            if key == 27:
                break
            elif key == ord("r"):
                colors[0] = (255,0,0)
            elif key==ord("b"):
              colors[0] = (0,0,0)
            elif key == ord("g"):
                colors[0]=(0,255,0)
        if ev.type == pygame.MOUSEBUTTONDOWN:
            pos_of_click = ev.dict["pos"]
            print(pos_of_click)
       # ................................ about the event...........................................................
        main_surface.fill((218,220,38))
        main_surface.fill(set_color,set_rectangular)
        # main_surface.blit(image,(0, 0))                     #insert the image with(blit)  with the nae var of image and start coordinate
        pygame.display.flip()
    pygame.quit()
p()