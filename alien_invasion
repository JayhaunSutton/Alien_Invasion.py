import sys

import pygame

from ship import Ship

from settings import Settings

class AlienInvasion:
    """Overall game class"""

    def __init__(self):
        """Initialize the game, and creating the resources to run it"""


        pygame.init()


        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230, 230, 230) 

        self.ship = Ship(self)
    
    def run_game(self):
        """Start of the main loop of the game"""
        while True:
            self._check_events()
            self._Update_screen()
            self.ship.update()
            self.clock.tick(60)
    
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                    self.ship.rect.y += 1
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
    def _Update_screen(self):
        """Update images on the screen, adn flip to a new screen."""
        
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    
    ai = AlienInvasion()
    ai.run_game()
