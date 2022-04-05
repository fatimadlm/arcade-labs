
import random
import arcade
import math
import os

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Lab 8:Sprites"


class Navep(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        """ Constructor. """
        # Call the parent class (Sprite) constructor
        super().__init__(filename, sprite_scaling)

        # Current angle in radians
        self.circle_angle = 0

        # How far away from the center to orbit, in pixels
        self.circle_radius = 0

        # How fast to orbit, in radians per frame
        self.circle_speed = 0.008

        # Set the center of the point we will orbit around
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):

        """ Update the ball's position. """
        # Calculate a new x, y
        self.center_x = self.circle_radius * math.sin(self.circle_angle) \
            + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) \
            + self.circle_center_y

        # Increase the angle in prep for the next round.
        self.circle_angle += self.circle_speed

class Meteorito(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        """ Constructor. """
        # Call the parent class (Sprite) constructor
        super().__init__(filename, sprite_scaling)

        # Current angle in radians
        self.circle_angle = 0

        # How far away from the center to orbit, in pixels
        self.circle_radius = 0

        # How fast to orbit, in radians per frame
        self.circle_speed = 0.008

        # Set the center of the point we will orbit around
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):

        """ Update the ball's position. """
        # Calculate a new x, y
        self.center_x = self.circle_radius * math.sin(self.circle_angle) \
            + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) \
            + self.circle_center_y

        # Increase the angle in prep for the next round.
        self.circle_angle += self.circle_speed




class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.all_sprites_list = None
        self.navep_list = None
        self.meteorito_list = None

        # Set up the player
        self.score = 0
        self.player_sprite = None

    def start_new_game(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.navep_list = arcade.SpriteList()
        self.meteorito_list = arcade.SpriteList()


        # Set up the player
        self.score = 0
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("nave.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.all_sprites_list.append(self.player_sprite)

        for i in range(20):

            # Create the coin instance
            # Coin image from kenney.nl
            navep = Navep("navep.png", SPRITE_SCALING / 2)
            meteorito=Meteorito("meteorito.png",SPRITE_SCALING/2)

            # Position the center of the circle the coin will orbit
            navep.circle_center_x = random.randrange(SCREEN_WIDTH)
            navep.circle_center_y = random.randrange(SCREEN_HEIGHT)
            meteorito.circle_center_x = random.randrange(SCREEN_WIDTH)
            meteorito.circle_center_y = random.randrange(SCREEN_HEIGHT)

            # Random radius from 10 to 200
            navep.circle_radius = random.randrange(10, 200)
            meteorito.circle_radius = random.randrange(10, 200)

            # Random start angle from 0 to 2pi
            navep.circle_angle = random.random() * 2 * math.pi
            meteorito.circle_angle = random.random() * 2 * math.pi

            # Add the coin to the lists
            self.all_sprites_list.append(navep)
            self.navep_list.append(navep)
            self.all_sprites_list.append(meteorito)
            self.meteorito_list.append(meteorito)

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Set the background color
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    def on_draw(self):
        self.clear()

        # Draw all the sprites.
        self.all_sprites_list.draw()

        # Put the text on the screen.
        output = "Puntos: " + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 16)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.all_sprites_list.update()

        # Generate a list of all sprites that collided with the player.
        hit1_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.navep_list)
        hit2_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.meteorito_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for navep in hit1_list:
            self.score += 1
            navep.remove_from_sprite_lists()

        for meteorito in hit2_list:
            self.score -= 1
            meteorito.remove_from_sprite_lists()

        if len(self.navep_list) == 0:

            self.set_mouse_visible(True)




def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.start_new_game()
    arcade.run()


if __name__ == "__main__":
    
