from time import sleep
n = 3
matrix = [['-']*n for _ in range(n)]


def show_matrix():
    '''ФУНКЦИЯ, КОТОРАЯ ПОКАЗЫВАЕТ МАТРИЦУ'''
    print('  0 1 2')
    for e in range(len(matrix)):
        print(e, end=' ')
        print(*matrix[e])


def insert_x():
    '''ФУНКЦИЯ, КОТОРАЯ СТАВИТ "х" '''
    try:
        print('Ход первого игрока (ставит x)')
        row = int(input('Введите номер строки: '))
        col = int(input('Введите номер столбца: '))
        if matrix[row][col] != '-':
            print()
            print('Эта клетка уже занята. Попробуй ещё раз.')
            print()
            show_matrix()
            insert_x()
        matrix[row][col] = 'x'
        show_matrix()
        print()
    except (ValueError, IndexError):
        print()
        print('Неправильный ввод. Попробуй ещё раз.')
        print()
        show_matrix()
        insert_x()


def insert_o():
    '''ФУНКЦИЯ, КОТОРАЯ СТАВИТ "o" '''
    try:
        print('Ход второго игрока (ставит o)')
        row = int(input('Введите номер строки: '))
        col = int(input('Введите номер столбца: '))
        if matrix[row][col] != '-':
            print()
            print('Эта клетка уже занята. Попробуй ещё раз ')
            print()
            show_matrix()
            insert_x()
        matrix[row][col] = 'o'
        show_matrix()
        print()
    except (ValueError, IndexError):
        print()
        print('Неправильный ввод. Попробуй ещё раз.')
        print()
        show_matrix()
        insert_o()


def check_x():
    '''ФУНКЦИЯ, КОТОРАЯ ПРОВЕРЯЕТ ВЫИГРЫШНЫЕ КОМБИНАЦИИ "x" '''
    if matrix[0][0] == 'x' and matrix[0][0] == matrix[0][1] == matrix[0][2] \
        or matrix[1][0] == 'x' and matrix[1][0] == matrix[1][1] == matrix[1][2] \
        or matrix[2][0] == 'x' and matrix[2][0] == matrix[2][1] == matrix[2][2] \
        or matrix[0][0] == 'x' and matrix[0][0] == matrix[1][0] == matrix[2][0] \
        or matrix[0][1] == 'x' and matrix[0][1] == matrix[1][1] == matrix[2][1] \
        or matrix[0][2] == 'x' and matrix[0][2] == matrix[1][2] == matrix[2][2] \
        or matrix[0][0] == 'x' and matrix[0][0] == matrix[1][1] == matrix[2][2] \
        or matrix[0][2] == 'x' and matrix[0][2] == matrix[1][1] == matrix[2][0]:
        return 'Первый выиграл'


def check_o():
    '''ФУНКЦИЯ, КОТОРАЯ ПРОВЕРЯЕТ ВЫИГРЫШНЫЕ КОМБИНАЦИИ "o" '''
    if matrix[0][0] == 'o' and matrix[0][0] == matrix[0][1] == matrix[0][2] \
        or matrix[1][0] == 'o' and matrix[1][0] == matrix[1][1] == matrix[1][2] \
        or matrix[2][0] == 'o' and matrix[2][0] == matrix[2][1] == matrix[2][2] \
        or matrix[0][0] == 'o' and matrix[0][0] == matrix[1][0] == matrix[2][0] \
        or matrix[0][1] == 'o' and matrix[0][1] == matrix[1][1] == matrix[2][1] \
        or matrix[0][2] == 'o' and matrix[0][2] == matrix[1][2] == matrix[2][2] \
        or matrix[0][0] == 'o' and matrix[0][0] == matrix[1][1] == matrix[2][2] \
        or matrix[0][2] == 'o' and matrix[0][2] == matrix[1][1] == matrix[2][0]:
        return 'Второй выиграл'


def empty_matrix():
    '''ФУНКЦИЯ, КОТОРАЯ ПРОВЕРЯЕТ НАЛИЧИЕ "-"(ТИРЕ) В МАТРИЦЕ'''
    for e in range(len(matrix)):
        if '-' in matrix[e]:
            return f'Да есть тире "-"'


def cross_zero():
    '''САМА ИГРА'''
    print()
    print('''---------------------------------
|      "КРЕСТИКИ-НОЛИКИ"        |
---------------------------------''')
    print()
    print('''Пояснение:    
1) 3 цифры слева - это строки
2) 3 цифры сверху - это столбцы
3) символы "-" это место куда ставить (x/o)''')
    print('Погнали!')
    print()
    show_matrix()
    while empty_matrix():
        insert_x()
        if check_x():
            print('Первый выиграл! (который ставил х)')
            question = input('Хочешь сыграть ещё раз? (y-yes/n-no): ')
            if question == 'y' or question == 'yes':
                cross_zero()
            else:
                print('Выход из программы...')
                sleep(3)
                break

        if not empty_matrix():
            print('Ничья!')
            question = input('Хочешь сыграть ещё раз? (y-yes/n-no): ')
            if question == 'y' or question == 'yes':
                cross_zero()
            else:
                print('Выход из программы...')
                sleep(3)
                break
        insert_o()
        if check_o():
            print('Второй выиграл! (который ставил o)')
            question = input('Хочешь сыграть ещё раз? (y-yes/n-no): ')
            if question == 'y' or question == 'yes':
                cross_zero()
            else:
                print('Выход из программы...')
                sleep(3)
                break


cross_zero()