import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Define square properties
square_size = 50
square_color = (0, 255, 0)  # Red color for the square
square_x = (screen_width - square_size) // 2  # Center horizontally
square_y = (screen_height - square_size) // 2  # Center vertically
square_speed = 5  # Speed of movement

# Set the clock for controlling the frame rate
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get key states for movement
    keys = pygame.key.get_pressed()

    # Move the square based on WASD keys
    if keys[pygame.K_w]:  # Move up
        square_y -= square_speed
    if keys[pygame.K_s]:  # Move down
        square_y += square_speed
    if keys[pygame.K_a]:  # Move left
        square_x -= square_speed
    if keys[pygame.K_d]:  # Move right
        square_x += square_speed

    # Keep the square within the screen bounds
    if square_x < 0:
        square_x = 0
    if square_x + square_size > screen_width:
        square_x = screen_width - square_size
    if square_y < 0:
        square_y = 0
    if square_y + square_size > screen_height:
        square_y = screen_height - square_size

    # Fill the background with black
    screen.fill((0, 0, 0))

    # Draw the square
    pygame.draw.rect(screen, square_color, (square_x, square_y, square_size, square_size))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate to 60 FPS
    clock.tick(60)