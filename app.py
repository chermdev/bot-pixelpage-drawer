from time import sleep
from draw import draw
from drawings import (face_eyes_looking_to_left,
                      face_eyes_looking_to_right,
                      face_close_eyes,
                      full_color,
                      image)
from colors import Color


def animate_face(eye_color: str, face_color: str) -> list:
    """ List of instructions to sent requests to draw a face with eyes that
    look to the left, then close, then look to the right, then close again."""
    draw(face_close_eyes(face_color))
    sleep(1)
    draw(face_eyes_looking_to_left(eye_color))
    sleep(1)
    draw(face_close_eyes(face_color))
    sleep(1)
    draw(face_eyes_looking_to_right(eye_color))
    sleep(1)
    draw(face_close_eyes(face_color))


def animate_adios_rgb():
    """ List of requests to draw the word 'adios' in different colors. """
    draw(image('img/adios.png', Color.red, Color.black))
    draw(image('img/adios.png', Color.green))
    draw(image('img/adios.png', Color.blue))
    draw(image('img/adios.png', Color.yellow))
    draw(image('img/adios.png', Color.cyan))
    draw(image('img/adios.png', Color.purple))
    draw(image('img/adios.png', Color.white))
    draw(image('img/adios.png', Color.black))


if __name__ == "__main__":
    draw(full_color(Color.cyan))
    draw(image('img/hola.png',
               color=Color.white))
    draw(image('img/hola.png',
               color=Color.cyan))
    animate_face(eye_color='#000000',
                 face_color=Color.cyan)
    draw(image('img/heart.png',
               bg_color=Color.white))
    draw(image('img/bullet.png',
               bg_color=Color.white))
    draw(image('img/pokeball2.png',
               bg_color=Color.white))
    draw(image('img/ghost.png'))
    draw(image('img/yoshi_egg.png',
               bg_color=Color.white))
    draw(image('img/mushroom.png',
               bg_color=Color.white))
    draw(image('img/coin.png',
               bg_color=Color.white))
    draw(image('img/flower.png'))
    animate_adios_rgb()
    draw(image('img/charlyysh.png'))
    draw(image('img/logo.png'))
