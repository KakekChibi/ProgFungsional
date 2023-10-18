import random

# Inisialisasi ukuran board
width = int(input("Enter the board width: "))
height = int(input("Enter the board height: "))

# Inisialisasi board matrix
board = [[' ' for _ in range(width)] for _ in range(height)]

# Generate random positions for 'A' and 'O'
a_position = (random.randint(0, height-1), random.randint(0, width-1))
o_position = (random.randint(0, height-1), random.randint(0, width-1))

# Fungsi untuk menampilkan board
def display_board():
    for i in range(height):
        print('|'.join(board[i]))
        print('-' * (width * 2 - 1))

# Fungsi untuk memeriksa apakah posisi valid
def is_valid_move(x, y):
    return 0 <= x < height and 0 <= y < width

# Set posisi awal 'A'
a_x, a_y = a_position
board[a_x][a_y] = 'A'

# Set posisi goal 'O'
o_x, o_y = o_position
board[o_x][o_y] = 'O'

# Menampilkan preview game
print("Preview of the game:")
display_board()

# Inisialisasi input pemain
moves = input("Your moves: ")

# Lakukan gerakan pemain
for move in moves:
    if move == 'w':
        new_a_x, new_a_y = a_x - 1, a_y
    elif move == 's':
        new_a_x, new_a_y = a_x + 1, a_y
    elif move == 'a':
        new_a_x, new_a_y = a_x, a_y - 1
    elif move == 'd':
        new_a_x, new_a_y = a_x, a_y + 1

    if is_valid_move(new_a_x, new_a_y):
        # Hapus 'A' dari posisi sebelumnya
        board[a_x][a_y] = ' '

        # Update posisi 'A'
        a_x, a_y = new_a_x, new_a_y

        # Periksa apakah mencapai goal
        if (a_x, a_y) == (o_x, o_y):
            print("You win!")
            display_board()
            break

        # Letakkan 'A' di posisi baru
        board[a_x][a_y] = 'A'
        display_board()
    else:
        print("Invalid move. You lose!")
        break

print("Game over. Thanks for playing!")
