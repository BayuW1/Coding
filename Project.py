import tkinter #tk-interface (graphical user interface library)
import tkinter as tk

def set_tile(row, column):
    global curr_player

    if (game_over):
        return

    if board[row][column]["text"] != "":
        #already taken spot
        return
    
    board[row][column]["text"] = curr_player #mark the board

    if curr_player == playerO: #switch player
        curr_player = playerX
    else:
        curr_player = playerO
    
    label["text"] = curr_player+"'s turn"

    #check winner
    check_winner()

def check_winner():
    global turns, game_over
    turns += 1

    #horizontally, check 3 rows
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"]+" is the winner!", foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
            game_over = True
            return
    
    #vertically, check 3 columns
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"]+" is the winner!", foreground=color_yellow)
            # label.config(text=board[0][column]["text"]+"thank you for playing", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
            game_over = True
            return
    
    #diagonally
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"]+" is the winner!", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return

    #anti-diagionally
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"]+" is the winner!", foreground=color_yellow)
        board[0][2].config(foreground=color_yellow, background=color_light_gray)
        board[1][1].config(foreground=color_yellow, background=color_light_gray)
        board[2][0].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return
    
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"]+" is the winner!", foreground=color_yellow)
        board[0][2].config(foreground=color_black, background=color_light_gray)
        board[1][1].config(foreground=color_black, background=color_light_gray)
        board[2][0].config(foreground=color_black, background=color_light_gray)
        game_over = True
        return
    
    #tie
    if (turns == 9):
        game_over = True
        label.config(text="DRAW", foreground=color_yellow)
        

def new_game():
    global turns, game_over

    turns = 0
    game_over = False

    label.config(text=curr_player+"'s turn", foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_blue, background=color_gray)


#game setup
playerX = "O"
playerO = "X"
curr_player = playerX
board = [[0, 0, 0], 
         [0, 0, 0], 
         [0, 0, 0]]

color_blue = "#399918"
color_yellow = "#49FF00"
color_gray = "#40A2E3"
color_light_gray = "#11B850"
color_black = "#212121"


turns = 0
game_over = False

#window setup
window = tkinter.Tk() #create the game window
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player+"'s turn", font=("Consolas", 20), background=color_gray,
                      foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                            background=color_gray, foreground=color_blue, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text="restart", font=("Consolas", 20), background=color_gray,
                        foreground="black", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

#center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()


window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window2 = tkinter.Tk() #create the game window
window2.title("Opening word")
window2.geometry("760x230")
label1 = tk.Label(window2, text="🎮Tic Tac Toe Game From Madrasah Internasional TechnoNatura StudentStudent🧑‍💻\n\n From Team Enderp3\n➤ Leader: Fauzan\n➤ Programmer: Arya R, Bayu, Zaki\n\nGood Luck🍀\nClose this Window before play the game", font=("Arial", 20))
label1.pack(pady=20)
window.mainloop()

root = tk.Tk()

root.title("Tic Tac Toe")

# Create a label to display the message
label = tk.Label(root, text="Thank you for playing Tic Tac Toe\n\n🫰", font=("Helvetica", 20))
label.pack(pady=20)
root.geometry("420x205")


# Start the main event loop
root.mainloop()