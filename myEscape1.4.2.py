# Space Walk
# by Sean McManus
# www.sean.co.uk / www.nostarch.com
# gigi's version
# open me by typing cmd at the folder bar where I'm at
# close me with Ctrl + C

# These are constants:
WIDTH = 800
HEIGHT = 600
# These are global variables:
player_x = 500
player_y = 550

# def >> defines a function
# screen.blit(images.imageName , (x-coord , y-coord)) is a Pygame Zero instructions that draws an image
# you don't need to write the extension (.jpg) of the file in Pygame Zero
# (0,0) is the top-left corner of the screen
# x goes from 0 at the left to far right (799 as WIDTH=800)
# y goes from 0 at the top to the very bottom (599 as HEIGHT=600)
# (0, 0) is called a tuple

# draw is used by PyGame Zero to update the screen
def draw():
    screen.blit(images.backdrop, (0, 0))
    screen.blit(images.mars, (50, 50))
    # we don't need to use the global command here because we are not changing the global variables, just taking in their values
    screen.blit(images.astronaut, (player_x, player_y))
    screen.blit(images.ship, (550, 300))
    #what if I want to rotate an image?

    
def game_loop():
    # global is a command that tells python you want to change variables that are outside of this function
# commands are written in orange
    global player_x, player_y
    if keyboard.right:
        # += increase by
        player_x += 8
    if keyboard.left:
        # -= decrease by
        player_x -= 8
    if keyboard.up:
        player_y -= 8
    if keyboard.down:
        player_y += 8
    #if you use 'if's instead of 'elif's you can move diagonaly!

# this instruction runs the game_loop function at an interval of 0.03 secs:
# python does not follow a linear order, instructions OUTSIDE of functions run BEFORE the functions
clock.schedule_interval(game_loop, 0.03)



# things I don't like right now:
#    I would like to limit the astronauts movements so that it doesn't go beyond the screen limits
#    I would like to see the coordinates somewhere on te screen

    
