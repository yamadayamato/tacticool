import pygame
""" Das geht ja nich das simon mehr commits hier hat als ich,
also änder ich jetz ganz viele Dateien
-The_Lie0
"""

class Rectangle():
    """A class for rectangles."""
    def __init__(self, game, position, size, color, stroke = 0):
        self.game = game
        self.position = position
        self.size = size
        self.rect = pygame.Rect(self.position, self.size)
        self.color = color
        self.stroke = stroke

    def move(self, x, y):
        self.rect = self.rect.move(x, y)

    def changeColor(self, color):
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, self.stroke)
