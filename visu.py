import sys, os, time
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import numpy as np
import generator, utility

class SlidePuzzle:
	def __init__(self, gs, ts, ms, grid, size_font):
		self.gs, self.ts, self.ms = gs, ts, gs
		self.tiles_len = gs[0] * gs[1] - 1
		self.tiles = [(x,y) for y in range(gs[1]) for x in range(gs[0])]
		self.tiles_v = [x for x in grid]
		self.tilespos = [(x*(ts+ms)+ms,y*(ts+ms)+ms) for y in range(gs[1]) for x in range(gs[0])] #actual
		self.tilesPOS = {(x,y):(x*(ts+ms)+ms,y*(ts+ms)+ms) for y in range(gs[1]) for x in range(gs[0])} #new pos
		self.prev = None
		self.font = pygame.font.Font(None, size_font)
		self.images = []
		self.resolution = 0
		self.speed, self.speed_slide = 1.0, 240
		for i in grid:
			image = pygame.Surface((ts, ts))
			image.fill((0, 255, 0))
			text = self.font.render(str(int(i)), 2, (0, 0, 0))
			w,h = text.get_size()
			image.blit(text, ((ts - w) / 2, (ts - h) / 2))
			self.images += [image]

	def getBlank(self):
		for i in range(len(self.tiles_v)):
			if self.tiles_v[i] == 0:
				return self.tiles[i]

	def setBlank(self, pos):
		for i in range(len(self.tiles_v)):
			if self.tiles_v[i] == 0:
				self.tiles[i] = pos

	opentile = property(getBlank, setBlank)

	def sliding(self) :
		for i in range(self.tiles_len):
			x, y = self.tilespos[i]
			X, Y = self.tilesPOS[self.tiles[i]]
			if x != X or y != Y:
				return True

	def switch(self, tile):
		if self.sliding() == True:
			return 
		self.tiles[self.tiles.index(tile)], self.opentile, self.prev = self.opentile, tile, self.opentile

	def update(self, dt):
		if self.resolution == 1:
			time.sleep(self.speed)
			print("sleep")
		s = self.speed_slide * dt
		for i in range(self.tiles_len):
			x,y = self.tilespos[i]
			X,Y = self.tilesPOS[self.tiles[i]]
			dx, dy = X - x, Y- y
			x = X if abs(dx) < s else x + s if dx > 0 else x - s
			y = Y if abs(dy) < s else y + s if dy > 0 else y - s
			self.tilespos[i] = x,y
		#find tiles with solution
		pass

	def draw(self, screen):
		for i in range(self.tiles_len + 1):
			if self.tiles_v[i] != 0:
				x,y = self.tilespos[i]
				screen.blit(self.images[i], (x, y))

	def events(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				exit()
			if event.key == 270:
				if self.speed > 0.21:
					self.speed -= 0.10
				print(f"speed : {self.speed}")
			if event.key == 269:
				if self.speed < 1.49:
					self.speed += 0.10
				print(f"speed : {self.speed}")
			if event.key == pygame.K_SPACE:
				self.switch((1,1))
			if event.key == pygame.K_r and self.resolution == 0:
				self.resolution = 1
			elif event.key == pygame.K_r:
				self.resolution = 0

def main(size, h, w, grid, size_font, size_ts):
	pygame.init()
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pygame.display.set_caption("NPuzzle")
	screen = pygame.display.set_mode((h, w))
	fpsclock = pygame.time.Clock()
	program = SlidePuzzle((size, size), size_ts, 5, grid, size_font)
	while True:
		dt = fpsclock.tick() / 1000
		screen.fill((0, 0, 0))
		program.draw(screen)
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			program.events(event)
		program.update(dt)

if __name__ == '__main__':
	n = 4
	h, w = 800, 600
	size_font = 125
	size_ts = 100
	#grid = np.array([[7, 8, 1],[4, 5, 0],[2, 3, 6]])#
	#grid = generator.gen_puzzle(n, 100)
	print(grid)
	main(n, h, w, np.concatenate(grid), size_font, size_ts)