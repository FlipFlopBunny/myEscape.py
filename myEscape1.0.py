# Space Walk
# by Sean McManus
# www.sean.co.uk / www.nostarch.com
# gigi's version
# open me by typing cmd at the folder bar where I'm at

# These are constants:
WIDTH = 800
HEIGHT = 600
# These are variables:
player_x = 500
player_y = 550

# def >> defines a function
# screen.blit(images.imageName , (x-coord , y-coord)) is a Pygame Zero instructions that draws an image
# you don't need to write the extension (.jpg) of the file in Pygame Zero
# (0,0) is the top-left corner of the screen
# x goes from 0 at the left to far right (799 as WIDTH=800)
# y goes from 0 at the top to the very bottom (599 as HEIGHT=600)
# (0, 0) is called a tuple
def draw():
    screen.blit(images.backdrop, (0, 0))
    screen.blit(images.mars, (50, 50))
    screen.blit(images.ship, (130, 150))
    
