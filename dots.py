import pygame as p
import random as r
from random import choice
import sys

p.init()
screen = p.display.set_mode((1200, 800))
p.display.set_caption('Lots of Dots')

white = 255, 255, 255
red = 255, 0, 0
blue = 0, 0, 255
#green = 0, 255, 0
yellow = 255, 255, 0
black = 0, 0, 0

col = [red, blue, yellow]
clock = p.time.Clock()
rate = 0

check = 0
while 1:
	for event in p.event.get():
		if event.type == p.QUIT: sys.exit()
		
	p.draw.circle(screen, choice(col), (r.randint(1, 1200), r.randint(1, 800)), r.randint(30, 50))
	p.display.flip()
	clock.tick(rate)
	rate += 0.5
	check += 1
	if check > 5000:
		screen.fill(black)
		check = 0
		rate = 1
