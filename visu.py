import pygame, sys, os

class SlidePuzzle:
	def __init__(self, gs, ts, ms):
		self.gs = gs
		self.ts = ts
		self.ms = ms
		self.tiles_len = gs[0] * gs[1] - 1
		self.tiles = [(x,y) for y in range(gs[1]) for x in range(gs[0])]
		self.tilespos = {(x,y):(x*(ts+ms)+ms,y*(ts+ms)+ms) for y in range(gs[1]) for x in range(gs[0])}
		self.font = pygame.font.Font(None, 120)
		self.images = []
		for i in range(self.tiles_len):
			image = pygame.Surface((ts, ts))
			image.fill((0, 255, 0))
			text = self.font.render(str(i + 1), 2, (0, 0, 0))
			w,h = text.get_size()
			image.blit(text, ((ts - w) / 2, (ts - h) / 2))
			self.images += [image]

	def switch(self, tiles):
		pass

	def update(self, dt):
		pass

	def draw(self, screen):
		for i in range(self.tiles_len):
			x,y = self.tilespos[self.tiles[i]]
			screen.blit(self.images[i], (x, y))

def main(size):
	pygame.init()
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pygame.display.set_caption("NPuzzle")
	screen = pygame.display.set_mode((800, 600))
	fpsclock = pygame.time.Clock()
	program = SlidePuzzle((size, size), 140, 5)
	while True:
		dt = fpsclock.tick() / 1000
		screen.fill((0, 0, 0))
		program.draw(screen)
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
		program.update(dt)

if __name__ == '__main__':
	main(3)