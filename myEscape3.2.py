room_map = [ [ 1, 1, 1, 1, 1],
             [ 1, 0, 0, 0, 1],
             [ 1, 0, 1, 0, 1],
             [ 1, 0, 0, 0, 1],
             [ 1, 0, 0, 0, 1],
             [ 1, 0, 0, 0, 1],
             [ 1, 1, 1, 1, 1]]

WIDTH = 800 #window size
HEIGHT = 800

# where we want to start the drawing:
top_left_x = 100
top_left_y = 150

DEMO_OBJECTS = [images.floor, images.pillar] #constant list
# floors will be displayed at 0's, pillars at 1's

room_height = 7 #room size equivalent to room map
room_width = 5

def draw():
    for y in range(room_height):
        for x in range(room_width):
            image_to_draw = DEMO_OBJECTS[room_map[y][x]]
            # using the values of one list to get elements in another
            screen.blit(image_to_draw,
                (top_left_x + (x*30),
                top_left_y + (y*30) - image_to_draw.get_height()))
            # tiles are 30 square pixels
            # tile is our unit of measure

# one issue I have with the design is that it didn't look 3D until it was explained
# when you are done here add this project to your resume
# and explain in the project section what concepts were explored (i.e. automation)
# as you build your CV website make the project section expandable
# I want to make a game that other people can install and play
# how do I make a PC shortcut to my game
# what about that framework for html that you can use python with?
# how to animate text? can I use different fonts in python?
