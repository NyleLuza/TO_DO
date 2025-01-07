"""
TODO:
- Figure out how to create buttons
- Figure out how to add user text input
- Figure out where to store the input
"""

import pygame
from ui_elements import Button
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
GRAY = (200, 200, 200)
WHITE = (255, 255, 255)
TEXT_COLOR = (100, 100, 100)

title_font = pygame.font.Font(None, 36)
text_font = pygame.font.Font(None, 24)

def render_text(text, font, color, center):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=center)
    return text_surface, text_rect


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("White")

    
    # 1st and 2nd param = x, y coordinates
    # 3rd and 4th param = size of rect 
    title_font = pygame.font.Font(None, 36)
    title_text, title_rect = render_text("Login", title_font, TEXT_COLOR, center=(SCREEN_WIDTH // 2, 250))

    screen.blit(title_text, title_rect)

    user_login = pygame.Rect(700 - 250 // 2, 300, 250, 50)
    user_text_font = pygame.font.Font(None, 24)
    user_text, user_text_rect = render_text("Username", text_font, TEXT_COLOR, center=(520, 320))

    pw_login = pygame.Rect(700 - 250 // 2, 360, 250, 50)
    pw_text_font = pygame.font.Font(None, 24)
    pw_text, pw_text_rect = render_text("Password", text_font, TEXT_COLOR, center=(520, 380))

    login_button = pygame.Rect(700 - 250 // 2, 420, 100, 50)
    login_text_font = pygame.font.Font(None, 24)
    login_text, login_text_rect = render_text("Login", text_font, TEXT_COLOR, center=login_button.center)

    user_login_box = Button(user_login, GRAY)

    password_login_box = Button(pw_login, GRAY)

    login_box = Button(login_button, GRAY)

    user_login_box.draw(screen, user_text, user_text_rect)
    password_login_box.draw(screen, pw_text, pw_text_rect)
    login_box.draw(screen, login_text, login_text_rect)

    """
    
    screen.blit(user_text, user_text_rect)
    screen.blit(pw_text, pw_text_rect)
    screen.blit(login_text, login_text_rect)
    """
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()