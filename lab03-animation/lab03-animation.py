import arcade
#dibuja luna
def luna(x,y):
    arcade.draw_point(x, y, arcade.color.DIM_GRAY, 5)
    arcade.draw_circle_filled(100-x, 500-y, 50, arcade.color.DIM_GRAY)
    arcade.draw_circle_filled(130-x, 500-y, 50, arcade.color.BLUE_GRAY)
#dibujar nube
def cloud(x,y):
    arcade.draw_point(x, y, arcade.color.HONEYDEW,5)
    arcade.draw_circle_filled(490 + x, 450 + y, 50, arcade.color.HONEYDEW)
    arcade.draw_circle_filled(530 + x, 450 + y, 50, arcade.color.HONEYDEW)
    arcade.draw_circle_filled(560 + x, 450 + y, 50, arcade.color.HONEYDEW)
    arcade.draw_circle_filled(520 + x, 500 + y, 50, arcade.color.HONEYDEW)
    arcade.draw_circle_filled(580 + x, 500 + y, 50, arcade.color.HONEYDEW)
    arcade.draw_circle_filled(600 + x, 450 + y, 50, arcade.color.HONEYDEW)
    arcade.draw_circle_filled(620 + x, 450 + y, 50, arcade.color.HONEYDEW)
def on_draw(delta_time):
    arcade.start_render()
    # cielo
    arcade.set_background_color(arcade.color.BLUE_GRAY)
    # Suelo
    arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BUD_GREEN)
    # luna
    luna(on_draw.luna1_x, 30)
    on_draw.luna1_x += 1
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
    cloud(on_draw.cloud1_x,30)
    on_draw.cloud1_x +=1

    # Mariposa
    # ALASd
    arcade.draw_circle_filled(600, 300, 50, arcade.color.INDIAN_RED)
    arcade.draw_circle_filled(625, 240, 35, arcade.color.INDIAN_RED)
    arcade.draw_circle_filled(700, 300, 50, arcade.color.INDIAN_RED)
    arcade.draw_circle_filled(675, 240, 35, arcade.color.INDIAN_RED)
    # CUERPO
    arcade.draw_rectangle_filled(650, 260, 20, 120, arcade.color.DEEP_TAUPE)
    # ALASi
    arcade.draw_circle_filled(650, 320, 10, arcade.color.DEEP_TAUPE)
    arcade.draw_circle_filled(650, 200, 10, arcade.color.DEEP_TAUPE)
    # ANTENAS
    arcade.draw_circle_filled(630, 350, 7, arcade.color.BLACK_BEAN)
    arcade.draw_circle_filled(660, 350, 7, arcade.color.BLACK_BEAN)
    arcade.draw_polygon_filled([[658, 350],
                                [661, 350],
                                [654, 322]],
                               arcade.color.BLACK_BEAN)
    arcade.draw_polygon_filled([[628, 350],
                                [631, 350],
                                [643, 320]],
                               arcade.color.BLACK_BEAN)

    arcade.finish_render()
on_draw.cloud1_x = 70
on_draw.luna1_x = 6
def main():
    arcade.open_window(800, 600, "Laboratorio 2")
    arcade.schedule(on_draw, 1 / 60)
    arcade.run()
main()


