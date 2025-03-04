"""
TODO:
- Figure out hover functionality to show that the rectangle has been selected
- Add the indicator to show that the box is ready for text
- Add the input to be shown on the rectangle
- Figure out where to store the input
"""

import pygame
from ui_elements import Button
from TextInputBox import TextInputBox
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

text_input_active = False
username_input = ""
username_render = text_font.render(username_input, True, (0,0,0))
pw_input = ""
pw_render = text_font.render(pw_input, True, (0,0,0))


def render_text(text, font, color, center):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=center)
    return text_surface, text_rect

# 1st and 2nd param = x, y coordinates
# 3rd and 4th param = size of rect 
title_text, title_rect = render_text("TO-DO List", title_font, TEXT_COLOR, center=(SCREEN_WIDTH // 2, 250))
# static text of field names
user_text, user_text_rect = render_text("Username", text_font, TEXT_COLOR, center=(500, 320))
pw_text, pw_text_rect = render_text("Password", text_font, TEXT_COLOR, center=(500, 380))
login_text, login_text_rect = render_text("Login", text_font, TEXT_COLOR, center=(625, 445))

# init of rect for buttons
user_login = pygame.Rect(700 - 250 // 2, 300, 250, 50)
pw_login = pygame.Rect(700 - 250 // 2, 360, 250, 50)
login_button = pygame.Rect(700 - 250 // 2, 420, 100, 50)

# init of text input boxes and set them to false since they are not active yet
user_text_input_box = TextInputBox(user_login, GRAY, False)  
pw_text_input_box = TextInputBox(pw_login, GRAY, False)

# init buttons
login_box = Button(login_button, GRAY)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if user_text_input_box.rect.collidepoint(event.pos):
                pw_text_input_box.set_active(False)
                user_text_input_box.set_active(True)
                """
                user_text_input_box.is_clicked("user", True)
                pw_text_input_box.is_clicked("pw", False)
                """
            elif pw_text_input_box.rect.collidepoint(event.pos):
                user_text_input_box.set_active(False)
                pw_text_input_box.set_active(True)
            elif login_box.rect.collidepoint(event.pos):
                username_input = ""
                pw_input = ""
            else:
                print("invalid click")
        elif event.type == pygame.KEYDOWN and (user_text_input_box.get_active() == True or pw_text_input_box.get_active() == True):
            if user_text_input_box.get_active() and event.key == pygame.K_RETURN:  # Finalize input on Enter
                print(f"Username Input: {username_input}\nPassword Input: {pw_input}")
                username_input = ""
                pw_input = ""
                # rect_color = GRAY
            elif event.key == pygame.K_BACKSPACE:  # Remove last character
                if user_text_input_box.get_active() == True:
                    username_input = username_input[:-1]
                elif pw_text_input_box.get_active() == True:
                    pw_input = pw_input[:-1]
                
            else:  # Add character to input
                if user_text_input_box.get_active():
                    username_input += event.unicode
                    username_render = text_font.render(username_input, True, (0,0,0))
                    
                elif pw_text_input_box.get_active():
                    pw_input += event.unicode
                    pw_render = text_font.render(pw_input, True, (0,0,0))
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("White")
    screen.blit(title_text, title_rect)

    # drawing buttons to screen
    user_text_input_box.draw(screen, user_text, user_text_rect)
    pw_text_input_box.draw(screen, pw_text, pw_text_rect)
    login_box.draw(screen, login_text, login_text_rect)

    # Displays user input to the screen (needs to be rendered after the text boxes are drawn for the text to be displayed)
    screen.blit(username_render, username_render.get_rect(center = user_login.center))
    screen.blit(pw_render, pw_render.get_rect(center = pw_login.center))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()