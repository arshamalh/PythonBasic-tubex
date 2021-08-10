def board_drawer(row, column):
    size = [int(row), int(column)]
    for i in range(size[0]):
        print(' ---' * size[1])
        print('|   ' * size[1] + '|')
    print(' ---' * size[1])

board_drawer(input('Enter the number of rows: '), input('Enter the number of columns: '))
