import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Game board as a list
board = [' ' for _ in range(9)]
current_player = 'X'

# Button references
buttons = []

def check_victory(icon):
    return (
        (board[0] == board[1] == board[2] == icon) or
        (board[3] == board[4] == board[5] == icon) or
        (board[6] == board[7] == board[8] == icon) or
        (board[0] == board[3] == board[6] == icon) or
        (board[1] == board[4] == board[7] == icon) or
        (board[2] == board[5] == board[8] == icon) or
        (board[0] == board[4] == board[8] == icon) or
        (board[2] == board[4] == board[6] == icon)
    )

def is_draw():
    return ' ' not in board

def on_click(index):
    global current_player

    if board[index] == ' ':
        board[index] = current_player
        buttons[index].config(text=current_player)

        if check_victory(current_player):
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            root.quit()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            root.quit()
        else:
            current_player = 'O' if current_player == 'X' else 'X'
    else:
        messagebox.showwarning("Invalid Move", "That space is already taken!")

# Create 3x3 grid of buttons
for i in range(9):
    button = tk.Button(root, text=' ', font=('Arial', 24), height=2, width=5,command=lambda i=i: on_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Start the GUI event loop
root.mainloop()
