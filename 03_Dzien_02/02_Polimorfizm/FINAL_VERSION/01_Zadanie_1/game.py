import chess

cb = chess.Chessboard()
cb.setup()

result = None

while True:
    chess.show(cb)
    coords = input('Enter the move, as xyXY [xy-from, XY-to, ex. 0103]: ')
    try:
        from_x = int(coords[0])
        from_y = int(coords[1])
        to_x = int(coords[2])
        to_y = int(coords[3])
    except:
        print('Invalid move!')
    try:
        result = cb.move(from_x, from_y, to_x, to_y)
    except ValueError as err:
        print('Invalid move:', str(err))
    except IndexError:
        print('Invalid move - outside the board!')
    if result:
        print()
        print(result)
        print()
        break
