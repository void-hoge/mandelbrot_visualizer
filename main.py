#!/usr/bin/env python3

import pygame

class mandelbrot:
	def __init__(self):
		self.zoom = (4.0, 4.0)
		self.screen_size = (1000,1000)
		pygame.init()
		self.screen = pygame.display.set_mode(self.screen_size)
		pygame.display.set_caption('mandelbrot')
		self.background = pygame.transform.scale(pygame.image.load('mandelbrot.png'), self.screen_size)

	def diverge_line(self, iter, mousepos):
		z = (0,0)
		c = self.trans_coord2compl(mousepos)
		for i in range(iter):
			p = z
			z = (z[0]**2 - z[1]**2, 2*z[0]*z[1])
			z = (z[0]+c[0], z[1]+c[1])
			if z[0]**2+z[1]**2 > 100000:
				break;
			pygame.draw.aaline(self.screen, (255,255,255), self.trans_compl2coord(p), self.trans_compl2coord(z))

	def trans_compl2coord(self, complex):
		""" convert complex number to coordinate of the screen
		"""
		real = complex[0]
		imag = complex[1]
		# real -> x
		# -imag -> y
		x = real*(self.screen_size[0]/self.zoom[0])+(self.screen_size[0]/2)
		y = -imag*(self.screen_size[1]/self.zoom[1])+(self.screen_size[1]/2)
		return (x,y)

	def trans_coord2compl(self, coord):
		""" convert coordinate of the screen to complex number
		"""
		x = coord[0]
		y = coord[1]
		# x -> real
		# y -> -imag
		real = (x-self.screen_size[0]/2)/(self.screen_size[0]/self.zoom[0])
		imag = -(y-self.screen_size[1]/2)/(self.screen_size[1]/self.zoom[1])
		return (real, imag)

	def draw(self):
		""" main loop function
		"""
		self.screen.blit(self.background, (0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT: return False
		mousepos = pygame.mouse.get_pos()
		self.diverge_line(128, mousepos)
		pygame.display.flip()
		return True

def main():
	hoge = mandelbrot()
	while True: hoge.draw()

if __name__ == '__main__':
	main()
