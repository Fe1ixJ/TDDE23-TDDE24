import math

def new_board(): 
    return {}

# Initialize an empty board
board = new_board()

# Function to place a piece on the board at the specified (x_cord, y_cord) for a given player.
# If the spot is free, the piece is added to the player's list of coordinates in the board.
def place_piece(board, x_cord, y_cord, player): 
    # Check if the position is free
    free_place = is_free(board, x_cord, y_cord)
    
    # If the place is free, add the piece
    if free_place is True:
        # Get the list of coordinates for the player
        cords = board.get(player, [])
        cords.append((x_cord, y_cord))  # Add the new coordinates
        board[player] = cords  # Update the board with the new coordinates
        return True
    else:
        # If not free, do nothing and return False 
        return False

# Function to move a piece from one position to another
def move_piece(board, x_cord, y_cord, new_x_cord, new_y_cord):  
    # Check if there's a piece at the original position
    player = get_piece(board, x_cord, y_cord)
    # Get player list of cords, find the index of old cords, replaced old cords, update board with new cords
    if player:
        if is_free(board, new_x_cord, new_y_cord):
            cords = board[player]
            index = cords.index((x_cord, y_cord))
            cords[index] = (new_x_cord, new_y_cord)
            board[player] = cords
            return True
    return False

# Function to check if a given position (x_cord, y_cord) is free
def is_free(board, x_cord, y_cord): 
    # Iterate over all players in the board
    for player in board:
        # Check if any player has a piece at the given coordinates
        if (x_cord, y_cord) in board[player]:
            return False  # Position is occupied
    # If no piece was found at that position, return True
    return True

# Function to retrieve the player who owns the piece at the specified position
def get_piece(board, x_cord, y_cord):
    for player, cords in board.items():
        if (x_cord, y_cord) in cords:
            return player
    return False

# Function to remove a piece from the board at the specified position
def remove_piece(board, x_cord, y_cord):  
    # Check if the position is occupied
    player = get_piece(board, x_cord, y_cord)
    # Get player list of cords, find the index of old cords, replaced old cords, update board with new cords
    if player:              
        cords=board[player]
        if (x_cord, y_cord) in cords:
            cords.remove((x_cord,y_cord))
            board[player] = cords
            return True
        else:
            return False
    else:
        return False

# Function to find the nearest piece to a given position
def nearest_piece(board, x_cord, y_cord):
    nearest_coords = None
    nearest_distance = float('inf')  # Initialize to infinity

    for player, cords in board.items():
        for (other_x, other_y) in cords:
            distance = math.sqrt((other_x - x_cord) ** 2 + (other_y - y_cord) ** 2)
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_coords = (other_x, other_y)

    return nearest_coords if nearest_coords else False
# Return coordinates and player



# Function to count how many pieces a player has in a given row/column
def count(board, thing, nr, player):
    player_moves = board.get(player, [])
    res = 0

    if thing == "column":
        for move in player_moves:
            if move[0] == nr:  # Check the column
                res += 1
    elif thing == "row":
        for move in player_moves:
            if move[1] == nr:  # Check the row
                res += 1

    return res

def choose(x, y):
    if y > x:
        return 0
    if y == 0 or y == x:
        return 1
    if x-y == 1:
        return x
    # Recursive call to calculate the binomial coefficient
    return x*choose(x - 1, y - 1)// y


