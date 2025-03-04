import pygame
class TextInputBox:
    def __init__(self, rect, bg_color, input_active):
        self.rect = rect
        self.bg_color = bg_color
        self.input_active = input_active
    
    def draw(self, screen, text_surface, text_rect):
        pygame.draw.rect(screen, self.bg_color, self.rect) # draw rectangle
        screen.blit(text_surface, text_rect) # Renders text and attaches to the rectangle

    def set_active(self, input_active):
        self.input_active = input_active

    def get_active(self):
        return self.input_active
