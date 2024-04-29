import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ukuran layar
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 400  # Perpanjangan tinggi layar untuk menambahkan area tombol "Play Again"

# Ukuran kotak pada papan Tic-Tac-Toe
BOX_SIZE = 100

# Membuat layar
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Font
font = pygame.font.Font(None, 50)

# Fungsi untuk menggambar garis-garis pada papan Tic-Tac-Toe
def draw_grid():
    # Garis horizontal
    pygame.draw.line(screen, BLACK, (0, 0), (SCREEN_WIDTH, 0), 2)
    pygame.draw.line(screen, BLACK, (0, BOX_SIZE), (SCREEN_WIDTH, BOX_SIZE), 2)
    pygame.draw.line(screen, BLACK, (0, BOX_SIZE * 2), (SCREEN_WIDTH, BOX_SIZE * 2), 2)
    pygame.draw.line(screen, BLACK, (0, BOX_SIZE * 3), (SCREEN_WIDTH, BOX_SIZE * 3), 2)
    
    # Garis vertikal
    pygame.draw.line(screen, BLACK, (0, 0), (0, SCREEN_HEIGHT - BOX_SIZE), 2)
    pygame.draw.line(screen, BLACK, (BOX_SIZE, 0), (BOX_SIZE, SCREEN_HEIGHT - BOX_SIZE), 2)
    pygame.draw.line(screen, BLACK, (BOX_SIZE * 2, 0), (BOX_SIZE * 2, SCREEN_HEIGHT - BOX_SIZE), 2)
    pygame.draw.line(screen, BLACK, (BOX_SIZE * 3 - 2, 0), (BOX_SIZE * 3 - 2, SCREEN_HEIGHT - BOX_SIZE), 2)

# Fungsi untuk menggambar simbol X atau O di kotak yang dipilih
def draw_symbol(row, col, symbol):
    center_x = col * BOX_SIZE + BOX_SIZE // 2
    center_y = row * BOX_SIZE + BOX_SIZE // 2
    if symbol == 'X':
        pygame.draw.line(screen , BLACK, (center_x - 30, center_y - 30), (center_x + 30, center_y + 30), 3)
        pygame.draw.line(screen, BLACK, (center_x + 30, center_y - 30), (center_x - 30, center_y + 30), 3)
    elif symbol == 'O':
        pygame.draw.circle(screen, BLACK, (center_x, center_y), 30, 3)

# Fungsi untuk mengecek apakah ada pemenang
def check_winner(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != ' ':
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

# Fungsi untuk mengecek apakah papan penuh (seri)
def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

# Fungsi untuk mereset permainan
def reset_game():
    # Kembalikan papan ke keadaan awal
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False
    return board, current_player, game_over

# Fungsi utama permainan
def main():
    # Membuat papan Tic-Tac-Toe
    board = [[' ' for _ in range(3)] for _ in range(3)]
    # Pemain pertama (X) akan mulai permainan
    current_player = 'X'
    # Menyimpan apakah permainan masih berlangsung
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                if game_over:
                    # Jika permainan sudah selesai, periksa klik di area tombol "Play Again"
                    if SCREEN_HEIGHT - 100 <= mouseY <= SCREEN_HEIGHT and 0 <= mouseX <= SCREEN_WIDTH:
                        board, current_player, game_over = reset_game()
                else:
                    # Tangani klik pada papan jika permainan belum selesai
                    clicked_row = mouseY // BOX_SIZE
                    clicked_col = mouseX // BOX_SIZE
                    if board[clicked_row][clicked_col] == ' ':
                        board[clicked_row][clicked_col] = current_player
                        winner = check_winner(board)
                        if winner:
                            game_over = True
                        elif check_draw(board):  # Periksa hasil seri
                            game_over = True
                            winner = None
                        else:
                            current_player = 'O' if current_player == 'X' else 'X'

        # Menggambar papan
        screen.fill(WHITE)
        draw_grid()
        for row in range(3):
            for col in range(3):
                if board[row][col] != ' ':
                    draw_symbol(row, col, board[row][col])

        # Menampilkan pemenang (jika ada) atau hasil seri
        if game_over:
            if winner:
                text = f"{winner} wins!"
            else:
                text = "It's a draw!"
            text_render = font.render(text, True, BLACK)
            screen.blit(text_render, (SCREEN_WIDTH // 2 - text_render.get_width() // 2, SCREEN_HEIGHT // 2 - text_render.get_height() // 2))

            # Tampilkan teks "Play Again?" di bagian bawah layar
            play_again_text = font.render("Main Lagi?", True, BLACK)
            screen.blit(play_again_text, (SCREEN_WIDTH // 2 - play_again_text.get_width() // 2, SCREEN_HEIGHT - 70))

        pygame.display.flip()

if __name__=="__main__":
    main()
