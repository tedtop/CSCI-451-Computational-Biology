# Ted Toporkov
# 10/4/2024
# knight_moves.py - shows knight moves on a cross-shaped chessboard

import sys
import stddraw
import time
import math

# Board coordinates for each position (centers of squares)
BOARD_COORDS = {
    1: (-15, 15),  2: (15, 15),
    3: (-45, -15), 4: (-15, -15), 5: (15, -15), 6: (45, -15),
    7: (-45, -45), 8: (-15, -45), 9: (15, -45), 10: (45, -45),
    11: (-15, -75), 12: (15, -75)
}

# Shaded squares
SHADED_SQUARES = [2, 4, 6, 7, 9, 11]

# Declare valid_moves as a global variable
valid_moves = {}

def calculate_valid_moves():
    """
    Calculate all valid knight moves for each position on the board.
    A knight moves in an L-shape: 2 squares in one direction and 1 square perpendicular.
    """
    global valid_moves  # Access the global valid_moves

    # Define the layout of the board as a 2D grid
    board_layout = [
        [0,  1,  2,  0],
        [3,  4,  5,  6],
        [7,  8,  9,  10],
        [0,  11, 12, 0]
    ]

    # Knight's potential move patterns
    knight_patterns = [
        (-2, -1), (-2, 1), (2, -1), (2, 1),
        (-1, -2), (-1, 2), (1, -2), (1, 2)
    ]

    def get_position(row, col):
        if 0 <= row < 4 and 0 <= col < 4:
            return board_layout[row][col]
        return 0

    def get_row_col(position):
        for row in range(4):
            for col in range(4):
                if board_layout[row][col] == position:
                    return row, col
        return None

    # Calculate valid moves for each position
    for start_pos in range(1, 13):
        valid_moves[start_pos] = []
        start_coord = get_row_col(start_pos)

        if start_coord:
            start_row, start_col = start_coord
            print(f"\nAnalyzing moves from position {start_pos}:")

            for pattern in knight_patterns:
                end_row = start_row + pattern[0]
                end_col = start_col + pattern[1]
                end_pos = get_position(end_row, end_col)

                print(f"  Trying pattern {pattern}: ", end="")

                if end_pos != 0:
                    print(f"Lands on position {end_pos}")
                    if end_pos not in valid_moves[start_pos]:
                        valid_moves[start_pos].append(end_pos)
                else:
                    print("Invalid - off board or in cut corner")

def setup_canvas():
    """Initialize the drawing canvas"""
    stddraw.setXscale(-70, 70)
    stddraw.setYscale(-100, 40)

def draw_arrow(x1, y1, x2, y2):
    """Draw an arrow from (x1,y1) to (x2,y2)"""
    stddraw.line(x1, y1, x2, y2)

    angle = math.atan2(y2 - y1, x2 - x1)
    arrow_length = 3
    arrow_angle = math.pi / 6

    ax1 = x2 - arrow_length * math.cos(angle - arrow_angle)
    ay1 = y2 - arrow_length * math.sin(angle - arrow_angle)
    ax2 = x2 - arrow_length * math.cos(angle + arrow_angle)
    ay2 = y2 - arrow_length * math.sin(angle + arrow_angle)

    stddraw.line(x2, y2, ax1, ay1)
    stddraw.line(x2, y2, ax2, ay2)

def draw_board():
    """Draw the cross-shaped chessboard exactly matching the provided image"""
    square_size = 30

    # Draw shaded squares first
    stddraw.setPenColor(stddraw.LIGHT_GRAY)
    for pos in SHADED_SQUARES:
        x, y = BOARD_COORDS[pos]
        stddraw.filledSquare(x, y, square_size/2)

    # Draw outer border only
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setPenRadius(0.005)

    # Define the outline of the cross shape
    outline = [
        (-30, 30), (30, 30), (30, 0), (60, 0),
        (60, -60), (30, -60), (30, -90), (-30, -90),
        (-30, -60), (-60, -60), (-60, 0), (-30, 0), (-30, 30)
    ]

    # Draw the outline
    for i in range(len(outline)):
        x1, y1 = outline[i]
        x2, y2 = outline[(i + 1) % len(outline)]
        stddraw.line(x1, y1, x2, y2)

    # Draw numbers
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setFontSize(24)
    for pos, (x, y) in BOARD_COORDS.items():
        stddraw.text(x, y, str(pos))

def draw_move(start_pos, end_pos):
    """Draw a knight's move with an arrow"""
    stddraw.setPenColor(stddraw.RED)
    stddraw.setPenRadius(0.666)

    start_x, start_y = BOARD_COORDS[start_pos]
    end_x, end_y = BOARD_COORDS[end_pos]

    if abs(start_x - end_x) > abs(start_y - end_y):
        mid_x = end_x
        mid_y = start_y
    else:
        mid_x = start_x
        mid_y = end_y

    draw_arrow(start_x, start_y, mid_x, mid_y)
    draw_arrow(mid_x, mid_y, end_x, end_y)

def show_moves():
    """Show all possible knight moves one by one"""
    global valid_moves  # Access global valid_moves
    for start_pos in range(1, 13):
        print(f"\nShowing moves from position {start_pos}")

        for end_pos in valid_moves[start_pos]:
            stddraw.clear()  # Clear the canvas before each move
            draw_board()  # Redraw the board

            print(f"  Drawing move from {start_pos} to {end_pos}")
            draw_move(start_pos, end_pos)

            stddraw.show(1000)  # Show the move for 1 second
            time.sleep(0.5)  # Small pause before moving to the next move

        time.sleep(1)  # Pause between positions

def find_intermediate_position(start_pos, end_pos):
    """Example of using global valid_moves in another function"""
    global valid_moves  # Access global valid_moves
    # Some logic that uses valid_moves...
    pass

def main():
    setup_canvas()
    calculate_valid_moves()  # valid_moves is filled in this function

    while True:
        show_moves()  # valid_moves is accessed in show_moves
        time.sleep(1)

if __name__ == '__main__':
    main()
