# Contains configuration settings for the Alien Invasion game.

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 7

        # Bullet settings
        self.bullet_speed = 15
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (90, 60, 60)