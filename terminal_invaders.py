import os
# Left arrow is 68, right arrow is 67, space is 32
import getch

# Terminal Invaders
#
# A terminal-based clone of Space Invaders.
#  Eric Matthes
#  @ehmatthes

ship_string = '|-/\-|'

def draw_ship(x_pos):
    y_spacing = '\n\n\n'
    x_spacing = ''
    for x in range(0, x_pos):
        x_spacing += ' '
    print(y_spacing + x_spacing + ship_string)

    # Move cursor down, out of the way
    print("\n\n\n\n\n")


x_ship = 0

os.system('clear')
print("Terminal Invaders - press 'q' to quit")
draw_ship(x_ship)

input = 'y'
while input != 'q':
    os.system('clear')
    print("Terminal Invaders - press 'q' to quit")

    if ord(input) == 67:
        x_ship += 1
    elif ord(input) == 68:
        x_ship -= 1

    draw_ship(x_ship)

    input = getch.getch()
