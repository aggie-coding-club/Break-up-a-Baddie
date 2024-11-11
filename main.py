import pygame
from sprite import sprites, Sprite
from player import Player
from input import keys_down
from map import Map, TileKind
from camera import create_screen

# Set up
pygame.init()

pygame.display.set_caption("Adventure Game")
screen = create_screen(800, 600, "Adventure Game")

clear_color = (30, 150, 50)
running = True
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 36)

# Define tile types
tile_kinds = [
    TileKind("dirt", "images/dirt.png", False),
    TileKind("grass", "images/grass.png", False),
    TileKind("water", "images/water.png", False),
    TileKind("wood", "images/wood.png", False)
]

# Initialize player and map
player = Player("images/girl1.png", 32 * 11, 32 * 7)
map = Map("maps/start.map", tile_kinds, 32)

# Text box state
text_box_visible = False
input_text = ""  # Stores the text that the user types
entered_text = ""  # Stores the text after the user presses Enter

# Add Sprites
Sprite("images/tree.png", 0 * 32, 0 * 32)
Sprite("images/tree.png", 7 * 32, 2 * 32)
Sprite("images/tree.png", 1 * 32, 10 * 32)
Sprite("images/tree.png", 12 * 32, -1 * 32)
Sprite("images/tree.png", 14 * 32, 9 * 32)
Sprite("images/tree.png", 12 * 32, -1 * 32)
Sprite("images/tree.png", 13 * 32, 12 * 32)
Sprite("images/tree.png", 20 * 32, 9 * 32)
Sprite("images/tree.png", 22 * 32, -1 * 32)
Sprite("images/tree.png", 24 * 32, 12 * 32)
Sprite("images/tree.png", 2 * 32, 8 * 32)
Sprite("images/tree.png", 15 * 32, 15 * 32)
Sprite("images/tree.png", 17 * 32, 1 * 32)
Sprite("images/tree.png", 1 * 32, 15 * 32)
Sprite("images/girl1.png", 5 * 32, 15 * 32)
Sprite("images/girl2.png", 7 * 32, 15 * 32)

# Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key != pygame.K_RETURN:  # Don't add Enter to keys_down
                keys_down.add(event.key)

            if event.key == pygame.K_RETURN and not text_box_visible:
                # Toggle the text box visibility when Enter is pressed (when box is not visible)
                text_box_visible = True
                input_text = "Fady: "  # Clear input text when opening the box
                entered_text = ""  # Reset entered text
            elif text_box_visible:  # If text box is visible, capture input
                if event.key == pygame.K_RETURN:
                    # Set entered text when Enter is pressed and close the box
                    entered_text = input_text
                    print(f"Typed text: {entered_text}")  # Return the text (print)
                    input_text = ""  # Reset input text after Enter is pressed
                    text_box_visible = False  # Close the text box
                elif event.key == pygame.K_BACKSPACE:
                    # Remove the last character
                    input_text = input_text[:-1]
                else:
                    # Add the typed character to input_text
                    input_text += event.unicode

        elif event.type == pygame.KEYUP:
            if event.key != pygame.K_RETURN:  # Only remove non-Enter keys
                keys_down.remove(event.key)

    # Update the player (only when text box is not visible)
    if not text_box_visible:
        player.update()

    # Draw everything
    screen.fill(clear_color)
    map.draw(screen)
    for s in sprites:
        s.draw(screen)

    # Check if the text box should be displayed
    if text_box_visible:
        box_width = 600
        box_height = 100
        box_x = 100  # Horizontal offset
        box_y = screen.get_height() - box_height - 50  # Place the box near the bottom
        box_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
        box_surface.set_alpha(180)  # Set trans

        pygame.draw.rect(screen, WHITE, (box_x, box_y, box_width, box_height), border_radius=15)  # Background with rounded corners
        pygame.draw.rect(screen, BLACK, (box_x, box_y, box_width, box_height), 2, border_radius=15)  # Border with rounded corners
        # Display the current input text in the box
        text_surface = font.render(input_text, True, BLACK)
        screen.blit(text_surface, (box_x + 20, box_y + 20))

        # Display the entered text if available
        if entered_text:
            entered_text_surface = font.render(f"{entered_text}", True, BLACK)
            screen.blit(entered_text_surface, (box_x + 20, box_y + 50))  # Show the entered text below

    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.delay(17)

# Quit Pygame
pygame.quit()
