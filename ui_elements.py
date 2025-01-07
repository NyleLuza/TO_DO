import pygame

class Button:
    def __init__(self, rect, text, font, text_color, bg_color):
        self.rect = rect
        self.text = text
        self.font = font
        self.text_color = text_color
        self.bg_color = bg_color
        self.text_surface = font.render(text, True, text_color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect) # draw rectangle
        screen.blit(self.text_surface, self.text_rect) # Renders text and attaches to the rectangle