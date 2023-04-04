from random import randint


def field(width, height, num_bombs):
    try:
        if width <= 0 or height <= 0 or num_bombs <= 0:
            raise ValueError("Все параметры должны быть положительными числами.")
        if num_bombs >= width * height:
            raise ValueError("Количество бомб не может превышать размер игрового поля.")
    except ValueError as e:
        print("Ошибка:", e)
        return None
    except TypeError as te:
        print(te)
        return None

    board = [[0 for i in range(width)] for j in range(height)]

    bombs = 0
    while bombs < num_bombs:
        x = randint(0, width - 1)
        y = randint(0, height - 1)
        if board[y][x] != '128163;':
            board[y][x] = '128163;'
            bombs += 1
    
    
    for y in range(height):
        for x in range(width):
            count = 0
            if board[y][x] != '128163;':
                if y-1 >=0 and x-1>=0: #left up
                    if board[y-1][x-1] == '128163;':
                        count+=1
                if x-1>=0:#left
                    if board[y][x-1] == '128163;':
                        count+=1
                if y+1 < height and x-1>=0: #left down
                    if board[y+1][x-1] == '128163;':
                        count+=1
                if y-1 >=0:#up
                    if board[y-1][x] == '128163;':
                        count+=1
                if y-1 >=0 and x+1<width:#right up
                    if board[y-1][x+1] == '128163;':
                        count+=1
                if x+1<width:#right
                    if board[y][x+1] == '128163;':
                        count+=1
                if y+1 < height and x+1 < width:#right down
                    if board[y+1][x+1] == '128163;':
                        count+=1
                if y+1 < height:#right down
                    if board[y+1][x] == '128163;':
                        count+=1
                board[y][x] = count
                
                
    # for row in board:
    #     print(' '.join([str(kletka) for kletka in row]))

    return board
