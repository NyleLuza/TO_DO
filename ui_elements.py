import pygame

class Button:
    def __init__(self, rect, bg_color):
        self.rect = rect
        self.bg_color = bg_color
        self.clicked = False
    
    def draw(self, screen, text_surface, text_rect):
        pygame.draw.rect(screen, self.bg_color, self.rect) # draw rectangle
        screen.blit(text_surface, text_rect) # Renders text and attaches to the rectangle
    
    def is_clicked(self, text, bool):
        self.clicked = bool
        print(f"{text} button clicked!")
        return self.clicked