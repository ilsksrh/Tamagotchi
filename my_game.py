from pygame import *
from hello import Player
init()
DISPLAY_W, DISPLAY_H = 800, 500
canvas = Surface((DISPLAY_W,DISPLAY_H))
window = display.set_mode(((DISPLAY_W,DISPLAY_H)))
display.set_caption("Tamagotchi | made in China")
running = True
clock = time.Clock()
bg = image.load('image/sand.jpg').convert()
cat = Player()
while running:
	clock.tick(60)
	for i in event.get():
		if i.type == QUIT:
			running = False
		if i.type == KEYDOWN:
			if i.key == K_LEFT:
				cat.LEFT_KEY, cat.FACING_LEFT = True, True
			elif i.key == K_RIGHT:
				cat.RIGHT_KEY, cat.FACING_LEFT = True, False
			'''elif event.key == pygame.K_SPACE:
				cat.jump()'''
		if i.type == KEYUP:
			if i.key == K_LEFT:
				cat.LEFT_KEY = False
			elif i.key == K_RIGHT:
				cat.RIGHT_KEY = False
	cat.update()
	#canvas.fill((255,255,255))
	canvas.blit(bg, (0,0))
	cat.draw(canvas)
	window.blit(canvas, (0,0))
	display.update()
