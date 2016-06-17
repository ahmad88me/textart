import sys
import pygame

pygame.init()
pygame.mixer.init()
fname = sys.argv[1]
print fname
#pygame.mixer.music.load(fname)
#pygame.mixer.music.play()
sounda= pygame.mixer.Sound(fname)
channela = sounda.play()
while channela.get_busy():
   pygame.time.delay(100)
