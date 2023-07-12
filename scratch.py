# scratch.py

# loop comprehensions
loop = [[(num1, num2) for num2 in range(5)] for num1 in range(5)]
print(type(loop))
print(loop)

loop2 = [i for i in range(0, 50)]
print(loop2)


# loop comprehension with mixed list/tuples
movies = [("Gump", 1941), ("Terry", 2001), ("Wind", 1986), ("Gary", 1976),
          ("Tom", 1934), ("Ads", 2010), ("Grim", 2001), ("Gruff", 2019)]
gmovies = [(title, year) for (title, year) in movies if year < 2002 and title.startswith("G")]
print(gmovies)

# importing & creating modules - also see module.py

import module
import sys
import extra.iota as iot
import extra.good.best.sigma as sig


odds = [i for i in range(1, 11, 2)]
evens = [i for i in range(2, 11, 2)]
print(odds)
print(evens)
print(module.prodl(odds))
print(module.prodl(evens))
print(module.suml(odds))
print(module.suml(evens))

for path in sys.path:
    print(path)
print(iot.FunI())
print(sig.FunS())


import pygame

run = True
width = 400
height = 100
pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to PyGame", True, (255, 255, 255))
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
pygame.display.flip()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONUP or event.type == pygame.KEYUP:
            run = False