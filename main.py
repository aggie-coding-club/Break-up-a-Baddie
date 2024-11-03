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

tile_kinds = [
    TileKind("dirt", "images/dirt.png", False),
    TileKind("grass", "images/grass.png", False),
    TileKind("water", "images/water.png", False),
    TileKind("wood", "images/wood.png", False)
]
player = Player("images/girl1.png", 32*11, 32*7)
map = Map("maps/start.map", tile_kinds, 32)
button_rect = pygame.Rect(50, 50, 150, 50)
text_box_visible = False


Sprite("images/tree.png", 0 * 32, 0 * 32)
Sprite("images/tree.png", 7 * 32, 2 * 32)
Sprite("images/tree.png", 1 * 32, 10* 32)
Sprite("images/tree.png", 12* 32, -1* 32)
Sprite("images/tree.png", 14* 32, 9 * 32)
Sprite("images/tree.png", 12* 32, -1* 32)
Sprite("images/tree.png", 13* 32, 12* 32)
Sprite("images/tree.png", 20* 32, 9 * 32)
Sprite("images/tree.png", 22* 32, -1* 32)
Sprite("images/tree.png", 24* 32, 12* 32)
Sprite("images/tree.png", 2 * 32, 8 * 32)
Sprite("images/tree.png", 15* 32, 15* 32)
Sprite("images/tree.png", 17 * 32,1 * 32)
Sprite("images/tree.png", 1 * 32, 15 * 32)
Sprite("images/girl1.png", 5 * 32, 15 * 32)
Sprite("images/girl2.png", 7 * 32, 15 * 32)


# Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            keys_down.add(event.key)
            if event.key == pygame.K_SPACE:
                # Toggle the text box visibility when space is pressed
                text_box_visible = not text_box_visible
        elif event.type == pygame.KEYUP:
            keys_down.remove(event.key)

            
    
    # Update Code
    player.update()

    # Draw Code
    screen.fill(clear_color)
    map.draw(screen)
    for s in sprites:
        s.draw(screen)
    pygame.display.flip()
    if text_box_visible:
        pygame.draw.rect(screen, WHITE, (100, 150, 600, 100))
        pygame.draw.rect(screen, BLACK, (100, 150, 600, 100), 2)
        text_surface = font.render("Hello, this is your text box!", True, BLACK)
        screen.blit(text_surface, (120, 180))



    # Cap the frames
    pygame.time.delay(17)


# Break down Pygame
pygame.quit()