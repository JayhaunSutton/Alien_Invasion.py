import pygame


class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Movement flag; start with a ship that's not moving.
        self.moving_left = False
        self.moving_right = False
    
        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the center of the left side of the screen.
        self.rect.midleft = self.screen_rect.midleft
        

        #Store a float for the ship's exact horizontal position.
        self.y = float(self.rect.y)
    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_left:
            self.y += self.settings.ship_speed
        if self.moving_right:
            self.y -= self.settings.ship_speed
        
        #Update rect object from self.y.
        self.rect.y = self.y    

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
