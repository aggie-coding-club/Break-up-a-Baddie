import pygame
import sys


# Initialize pygame
pygame.init()


# Set up the screen dimensions
screen_width = 1400
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
#set player
playerimg = pygame.image.load('picture/down.png')
pygame.display.set_icon(playerimg)
square_size = 50
player_x = (screen_width - square_size) // 2  # Center horizontally
player_y = (screen_height - square_size) // 2  # Center vertically




#title page area
game_started = False
title_image = pygame.image.load('picture/logo.png') 
title_image = pygame.transform.scale(title_image, (1200, 600))  # Resize to width 400, height 200




#font section
font = pygame.font.Font(None, 74)
text_color = (255, 255, 255)
small_font = pygame.font.Font(None, 50)  # Smaller font for the "Click anywhere" text






def player():
   screen.blit(playerimg,(player_x,player_y))


def title_screen():
   screen.fill((0, 0, 0))  # Fill the background with black


  
   # Display the title
   title_image_rect = title_image.get_rect(center=(screen_width // 2+100, screen_height // 2))  # Center the image
   screen.blit(title_image, title_image_rect)
  
   # Update the
   click_text = small_font.render("Click anywhere to start", True, text_color)
   click_text_rect = click_text.get_rect(center=(screen_width // 2, screen_height // 2 + 200))  # Position below the logo
   screen.blit(click_text, click_text_rect)


   pygame.display.update()






pygame.display.set_caption("Break up a Baddie")


# Define square properties


square_color = (255, 0, 0)  # Red color for the square


square_speed = 5  # Speed of movement


# Set the clock for controlling the frame rate
clock = pygame.time.Clock()


# Game loop
while True:
       # Title screen loop
   while not game_started:
       title_screen()
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
           if event.type == pygame.MOUSEBUTTONDOWN:
               game_started = True




   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()


   # Get key states for movement
   keys = pygame.key.get_pressed()


   # Move the square based on WASD keys
   if keys[pygame.K_w]:  # Move up
       player_y -= square_speed
       playerimg = pygame.image.load('picture/up.png')
   if keys[pygame.K_s]:  # Move down
       player_y += square_speed
       playerimg = pygame.image.load('picture/down.png')


   if keys[pygame.K_a]:  # Move left
       player_x -= square_speed
       playerimg = pygame.image.load('picture/left.png')


   if keys[pygame.K_d]:  # Move right
       player_x += square_speed
       playerimg = pygame.image.load('picture/right.png')


   # Keep the square within the screen bounds
   if player_x < 0:
       player_x = 0
   if player_x + square_size > screen_width:
       player_x = screen_width - square_size
   if player_y < 0:
       player_y = 0
   if player_y + square_size > screen_height:
       player_y = screen_height - square_size


   # Fill the background with black
   screen.fill((0, 0, 0))


   # Draw the square
   player()


   # Update the display
   pygame.display.update()


   # Cap the frame rate to 60 FPS
   clock.tick(60)

