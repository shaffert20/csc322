from graphics import graph
import random

#Sets background color to light blue/cyan
def background(gui):
    gui.rectangle( 0, 0, 700, 700, fill = 'cyan')
#random color generator
def random_color(gui):
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return gui.get_color_string(red, green, blue)
#Creates the sun and sets color
def sun(gui):
    x = (gui.mouse_x//-50)+343
    y = (gui.mouse_y//-50)+343
    gui.ellipse(x+150, y-250, 100, 100, 'yellow')
#creates the middle mountain
def middle_mountain(gui, middle_color):
    x = (gui.mouse_x//-35)+338
    y = (gui.mouse_y//-35)+338
    gui.triangle(x-250, y+350, x, y-150, x+250, y+350, middle_color)
#Creates the side mountains
def side_mountains(gui, left_color, right_color):
    x = (gui.mouse_x//-18)+325
    y = (gui.mouse_y//-18)+325
    gui.triangle(x-600, y+412, x-200, y-100, x+200, y+412, left_color)
    gui.triangle(x-200, y+412, x+200, y-100, x+600, y+412, right_color)
#creates the foreground -- Grass and Tree
def foreground(gui):
    x = (gui.mouse_x//-5)+280
    y = (gui.mouse_y//-5)+280
    gui.rectangle(x-500, y+250, 1500, 500, 'spring green3')
    x_grass = -2
    while x_grass < 710:
        gui.line(x_grass, y+220, x_grass, y+250, 'spring green3', 3)
        x_grass += 7
    gui.rectangle(x+130, y+200, 30, 100, 'saddle brown')
    gui.ellipse(x+145, y+175, 100, 150, 'forest green')
#Creates the birds
def birds(gui, x_bird):
    i = 0
    y_bird = (gui.mouse_y//-10)+200
    while i < 5:
        gui.line(x_bird-25, y_bird-10, x_bird, y_bird, 'black', 4)
        gui.line(x_bird+25, y_bird-10, x_bird, y_bird, 'black', 4)
        i += 1
        x_bird -= 100
        y_bird -= 25
#main() function
def main():
    gui = graph(700, 700, 'Motion Parallax')
    middle_color = random_color(gui)
    left_color = random_color(gui)
    right_color = random_color(gui)
    x_bird = 450
#implements the functions to create the landscape
    while True:
        gui.clear()
        background(gui)
        sun(gui)
        middle_mountain(gui, middle_color)
        side_mountains(gui, left_color, right_color)
        foreground(gui)
        birds(gui, x_bird)
        x_bird +=2
        #wraps birds
        if x_bird > 1050:
            x_bird = -50
        gui.update_frame(60)

main()