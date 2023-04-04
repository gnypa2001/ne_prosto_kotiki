from random import randint
# l = [12,32,23,4,324,32,4]
# try:
#     l.pop(int(input("Enter index: ")))
    
    
# except IndexError:
#     print("iNdex out of range")
# except ValueError:
#     print("entered string not int")


# print("Hello...")



class A(Exception):
    pass

class B(Exception):
    pass

class C(Exception):
    pass



l = [A, B, C]

for ex in l:
    try:
        raise ex
    
    except A:
        print("A")
    except B:
        print("B")
    except C:
        print("C")


symbols = None

def random_password(symbols, pass_len):
    try:
        password = ""
        for symbol in range(pass_len):
            password += symbols[randint(0, len(symbols) - 1)]
            
    except TypeError as te:
            print(te)
    except ValueError as te:
            print(te)
    return password


# Создать функцию генератор паролей, которая принимает список символов, из которых должен состоять пароль, а также его длинна.

# Функция должна вернуть сгенерированный случайный пароль с соответствующей длиной.
# TypeError(int)
# ValueError: empty range for randrange() (0, 0, 0)
# TypeError: can only concatenate str (not "int") to str
# TypeError: 'str' object cannot be interpreted as an integer
# TypeError: 'list' object cannot be interpreted as an integer

# print(random_password(["hsdjhjsfdjkfdj", [1,2,3,4,5,6,]], 13))


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
        if board[y][x] != '*':
            board[y][x] = '*'
            bombs += 1
    
    
    for y in range(height):
        for x in range(width):
            count = 0
            if board[y][x] != '*':
                if y-1 >=0 and x-1>=0: #left up
                    if board[y-1][x-1] == '*':
                        count+=1
                if x-1>=0:#left
                    if board[y][x-1] == '*':
                        count+=1
                if y+1 < height and x-1>=0: #left down
                    if board[y+1][x-1] == '*':
                        count+=1
                if y-1 >=0:#up
                    if board[y-1][x] == '*':
                        count+=1
                if y-1 >=0 and x+1<width:#right up
                    if board[y-1][x+1] == '*':
                        count+=1
                if x+1<width:#right
                    if board[y][x+1] == '*':
                        count+=1
                if y+1 < height and x+1 < width:#right down
                    if board[y+1][x+1] == '*':
                        count+=1
                if y+1 < height:#right down
                    if board[y+1][x] == '*':
                        count+=1
                board[y][x] = count
                
                
    for row in board:
        print(' '.join([str(kletka) for kletka in row]))

    return board

print(field(10, 10, 7))

#https://docs.python.org/3/library/exceptions.html
