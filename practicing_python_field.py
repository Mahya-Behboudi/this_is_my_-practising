import pygame
ev.pygame.event.poll()
if ev.type != pygame.NOEVENT:   # Only print if it is interesting!
    print(ev)