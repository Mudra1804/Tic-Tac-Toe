import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = 'X'
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", font=('normal', 40), width=5, height=2,
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def on_button_click(self, i, j):
        if self.buttons[i][j]['text'] == "" and self.check_winner() is False:
            self.buttons[i][j]['text'] = self.current_player
            self.board[i][j] = self.current_player
            if self.check_winner():
                self.display_winner(self.current_player)
            elif self.check_draw():
                self.display_draw()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] is not None:
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] is not None:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return True
        return False

    def check_draw(self):
        for row in self.board:
            if None in row:
                return False
        return True

    def display_winner(self, player):
        messagebox.showinfo("Tic Tac Toe", f"Player {player} wins!")
        self.reset_board()

    def display_draw(self):
        messagebox.showinfo("Tic Tac Toe", "It's a draw!")
        self.reset_board()

    def reset_board(self):
        self.current_player = 'X'
        self.board = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ""

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
