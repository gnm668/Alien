import pygame

class Cloud():
	def __init__(self, screen):
		'''Initialize cloud and set his starting position.'''
		self.screen = screen

		self.image = pygame.image.load('cloud.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery

	def bitme(self):
		'''Draw cloud at his current location'''
		self.screen.blit(self.image, self.rect)
