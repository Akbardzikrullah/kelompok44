import time

def is_safe(board, row, col, n):
    """Cek apakah ratu bisa ditempatkan di (row, col)."""
    for r in range(row):
        c = board[r]
        if c == col or \
           r - c == row - col or \
           r + c == row + col:
            return False
    return True

def print_board(board, n):
    """Cetak papan catur berdasarkan posisi ratu."""
    for r in range(n):
        row = ["."] * n
        if board[r] != -1:
            row[board[r]] = "Q"
        print(" ".join(row))
    print("\n")

def check_victory(board, n):
    """Periksa apakah semua ratu telah ditempatkan."""
    return -1 not in board

def n_queens_game_single_player(n, time_limit):
    """Permainan N-Queens untuk satu pemain dengan batas waktu."""
    board = [-1] * n
    start_time = time.time()

    while time.time() - start_time < time_limit:
        print("Giliran Anda.")
        print_board(board, n)

        try:
            row = int(input(f"Pilih baris (1-{n}): ")) - 1
            col = int(input(f"Pilih kolom (1-{n}): ")) - 1
        except ValueError:
            print("Masukkan angka valid!")
            continue

        if row < 0 or row >= n or col < 0 or col >= n:
            print("Baris atau kolom di luar jangkauan! Coba lagi.")
            continue

        if board[row] != -1:
            print("Baris ini sudah ditempati! Coba lagi.")
            continue

        if not is_safe(board, row, col, n):
            print("Posisi ini tidak aman! Coba lagi.")
            continue

        # Tempatkan ratu di posisi yang valid
        board[row] = col

        if check_victory(board, n):
            print_board(board, n)
            print("Selamat! Anda menang dengan menyelesaikan papan!")
            return

    print("Waktu habis! Tidak ada pemenang.")
    print_board(board, n)

if __name__ == "__main__":
    print("Permainan N-Queens - Single Player")
    N = int(input("Masukkan ukuran papan (N): "))
    time_limit = int(input("Masukkan batas waktu permainan (detik): "))
    n_queens_game_single_player(N, time_limit)
