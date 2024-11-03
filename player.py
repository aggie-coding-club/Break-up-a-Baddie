import pygame
from sprite import Sprite
from input import is_key_pressed
from camera import camera

movement_speed = 2
animation_speed = 10 
class Player(Sprite):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.animation_counter = 0
        self.images = [
            "images/girl1.png",
            "images/girl1leftlegup.png",
            "images/girl1rightlegup.png"
        ]
        self.current_image_index = 0
        
        
    def animate_movement(self):
        # Increment the counter and update image based on the animation speed
        self.animation_counter += 1
        if self.animation_counter >= animation_speed:
            self.animation_counter = 0  # Reset the counter
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.change_image(self.images[self.current_image_index])  # Set the new image
    def change_image(self, new_image_path):
        self.image = pygame.image.load(new_image_path) 
    def update(self):
        if is_key_pressed(pygame.K_w):
            self.y -= movement_speed
            self.animate_movement()
        if is_key_pressed(pygame.K_s):
            self.y += movement_speed
            self.animate_movement()
        if is_key_pressed(pygame.K_a):
            self.x -= movement_speed
            self.animate_movement()

        if is_key_pressed(pygame.K_d):
            self.x += movement_speed
            self.animate_movement()
        
            
        
        camera.x = self.x - camera.width/2 
        camera.y = self.y - camera.height/2 
   