import arcade

class mariposa:
    def __init__(self, position_x, position_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        # Alas d
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)
        arcade.draw_circle_filled(self.position_x + 25, self.position_y - 60, self.radius - 15, self.color)
        arcade.draw_circle_filled(self.position_x+100, self.position_y, self.radius, self.color)
        arcade.draw_circle_filled(self.position_x+75, self.position_y-60, self.radius - 15, self.color)
        # cuerpo
        arcade.draw_rectangle_filled(self.position_x + 50, self.position_y - 40, 20, 120, arcade.color.DEEP_TAUPE)
        # Alas i
        arcade.draw_circle_filled(self.position_x + 50, self.position_y + 20,self.radius-40, arcade.color.DEEP_TAUPE)
        arcade.draw_circle_filled(self.position_x + 50, self.position_y-100, self.radius-40, arcade.color.DEEP_TAUPE)
        #antena
        arcade.draw_circle_filled(self.position_x + 30, self.position_y + 50,self.radius-43, arcade.color.BLACK_BEAN)
        arcade.draw_circle_filled(self.position_x + 60, self.position_y+50, self.radius-43, arcade.color.BLACK_BEAN)
        arcade.draw_polygon_filled([[self.position_x+58, self.position_y+50],
                                    [self.position_x+61, self.position_y+50],
                                    [self.position_x+54, self.position_y+22]],
                                   arcade.color.BLACK_BEAN)
        arcade.draw_polygon_filled([[self.position_x + 28, self.position_y+50],
                                    [self.position_x + 31, self.position_y + 50],
                                    [self.position_x + 43, self.position_y + 20]],
                                   arcade.color.BLACK_BEAN)



class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        self.mariposa = mariposa(600, 300, 50, arcade.color.INDIAN_RED)

    def on_draw(self):
        arcade.start_render()
        # cielo
        arcade.set_background_color(arcade.color.BLUE_GRAY)
        # Suelo
        arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BUD_GREEN)
        # luna
        arcade.draw_circle_filled(100, 500, 50, arcade.color.DIM_GRAY)
        arcade.draw_circle_filled(130, 500, 50, arcade.color.BLUE_GRAY)
        # montaña de atras 1
        arcade.draw_polygon_filled([[0, 190],
                                    [100, 300],
                                    [400, 190]],
                                   arcade.color.CELADON_GREEN)
        # Montaña de atras 2
        arcade.draw_polygon_filled([[600, 190],
                                    [700, 300],
                                    [800, 200]],
                                   arcade.color.CELADON_GREEN)
        # sol
        arcade.draw_circle_filled(400, 300, 100, arcade.color.CANARY_YELLOW)
        # Montaña grande
        arcade.draw_polygon_filled([[0, 190],
                                    [300, 400],
                                    [800, 190]],
                                   arcade.color.BUD_GREEN)
        # arbol
        arcade.draw_rectangle_filled(130, 100, 20, 70, arcade.color.DEEP_TAUPE)
        arcade.draw_circle_filled(130, 170, 60, arcade.color.ENGLISH_GREEN)
        arcade.draw_circle_filled(120, 160, 4, arcade.color.FIREBRICK)
        arcade.draw_circle_filled(140, 130, 3, arcade.color.FIREBRICK)
        arcade.draw_circle_filled(110, 120, 4, arcade.color.FIREBRICK)
        arcade.draw_circle_filled(170, 156, 3, arcade.color.FIREBRICK)
        arcade.draw_circle_filled(160, 180, 4, arcade.color.FIREBRICK)
        arcade.draw_circle_filled(110, 170, 4, arcade.color.FIREBRICK)

        # PINO
        arcade.draw_rectangle_filled(200, 50, 20, 70, arcade.color.DEEP_TAUPE)
        arcade.draw_polygon_filled([[160, 45],
                                    [200, 140],
                                    [240, 45]],
                                   arcade.color.ETON_BLUE)
        arcade.draw_polygon_filled([[160, 65],
                                    [200, 160],
                                    [240, 65]],
                                   arcade.color.ETON_BLUE)
        # pino2
        arcade.draw_rectangle_filled(500, 79, 35, 100, arcade.color.DEEP_TAUPE)
        arcade.draw_polygon_filled([[430, 100],
                                    [500, 250],
                                    [570, 100]],
                                   arcade.color.ETON_BLUE)
        arcade.draw_polygon_filled([[430, 69],
                                    [500, 200],
                                    [570, 69]],
                                   arcade.color.ETON_BLUE)
        arcade.draw_polygon_filled([[430, 130],
                                    [500, 270],
                                    [570, 130]],
                                   arcade.color.ETON_BLUE)
        # NUBE
        arcade.draw_circle_filled(490, 450, 50, arcade.color.HONEYDEW)
        arcade.draw_circle_filled(530, 450, 50, arcade.color.HONEYDEW)
        arcade.draw_circle_filled(560, 450, 50, arcade.color.HONEYDEW)
        arcade.draw_circle_filled(520, 500, 50, arcade.color.HONEYDEW)
        arcade.draw_circle_filled(580, 500, 50, arcade.color.HONEYDEW)
        arcade.draw_circle_filled(600, 450, 50, arcade.color.HONEYDEW)
        arcade.draw_circle_filled(620, 450, 50, arcade.color.HONEYDEW)

        self.mariposa.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.mariposa.position_x = x

        self.mariposa.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """

        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Coordenadas con botón izquierdo", x, y)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print("Coordenadas con botón derecho", x, y)


def main():
    window = MyGame(800, 600, "Control")
    arcade.run()


main()
n()