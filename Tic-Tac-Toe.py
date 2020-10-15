lists = [["_" for m in range(j, j + 3)] for j in range(0, 8, 3)]
def board():
    print('---------')
    print(f'''| {lists[0][0]} {lists[0][1]} {lists[0][2]} |
| {lists[1][0]} {lists[1][1]} {lists[1][2]} |
| {lists[2][0]} {lists[2][1]} {lists[2][2]} |''')
    print('---------')

xw = False
ow = False
counter = 0
board()
while counter < 9 and not xw and not ow:
    x, y = input("Enter the coordinates: ").split()
    if not x.isdecimal() or not y.isdecimal():
        print("You should enter numbers!")
    elif x not in "123" or y not in "123":
        print("Coordinates should be from 1 to 3!")
    else:
        x = int(x)
        y = int(y)
        if lists[3-y][x-1] != "_":
            print("This cell is occupied! Choose another one!")
        else:
            if counter % 2:
                lists[3-y][x-1] = "O"
            else:
                lists[3-y][x-1] = "X"
            counter += 1
            board()
            for n in range(3):
                if lists[0][n] == lists[1][n] == lists[2][n]: #  Vertical
                    xw = lists[0][n] == "X" or xw
                    ow = lists[0][n] == "O" or ow

                xw = lists[n].count("X") == 3 or xw #  Horizontal
                ow = lists[n].count("O") == 3 or ow    

            if lists[1][1] == lists[0][0] == lists[2][2] or lists[1][1] == lists[0][2] == lists[2][0]: #  Diagonal
                xw = lists[1][1] == "X" or xw
                ow = lists[1][1] == "O" or ow

if not xw and not ow and counter == 9:
    print("Draw")
elif xw and not ow:
    print("X wins")
elif ow and not xw:
    print("O wins")
