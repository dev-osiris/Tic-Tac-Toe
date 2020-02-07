# TIC TAC TOE GAME
import random


def append_to_row_list(r, c, val, row1_list, row2_list, row3_list):
    # adding to row 1
    if r == '1' and c == '1' and val == 'x':
        row1_list[0] = 'x'
    elif r == '1' and c == '1' and val == 'o':
        row1_list[0] = 'o'
    if r == '1' and c == '2' and val == 'x':
        row1_list[1] = 'x'
    elif r == '1' and c == '2' and val == 'o':
        row1_list[1] = 'o'
    if r == '1' and c == '3' and val == 'x':
        row1_list[2] = 'x'
    elif r == '1' and c == '3' and val == 'o':
        row1_list[2] = 'o'

    # adding to row 2
    if r == '2' and c == '1' and val == 'x':
        row2_list[0] = 'x'
    elif r == '2' and c == '1' and val == 'o':
        row2_list[0] = 'o'
    if r == '2' and c == '2' and val == 'x':
        row2_list[1] = 'x'
    elif r == '2' and c == '2' and val == 'o':
        row2_list[1] = 'o'
    if r == '2' and c == '3' and val == 'x':
        row2_list[2] = 'x'
    elif r == '2' and c == '3' and val == 'o':
        row2_list[2] = 'o'

    # adding to row 3
    if r == '3' and c == '1' and val == 'x':
        row3_list[0] = 'x'
    elif r == '3' and c == '1' and val == 'o':
        row3_list[0] = 'o'
    if r == '3' and c == '2' and val == 'x':
        row3_list[1] = 'x'
    elif r == '3' and c == '2' and val == 'o':
        row3_list[1] = 'o'
    if r == '3' and c == '3' and val == 'x':
        row3_list[2] = 'x'
    elif r == '3' and c == '3' and val == 'o':
        row3_list[2] = 'o'


def vertical_matching(row1_list, row2_list, row3_list):
    if row1_list[0] == row2_list[0] == row3_list[0] == 'x':
        var = 'x'
    elif row1_list[0] == row2_list[0] == row3_list[0] == 'o':
        var = 'o'
    elif row1_list[1] == row2_list[1] == row3_list[1] == 'x':
        var = 'x'
    elif row1_list[1] == row2_list[1] == row3_list[1] == 'o':
        var = 'o'
    elif row1_list[2] == row2_list[2] == row3_list[2] == 'x':
        var = 'x'
    elif row1_list[2] == row2_list[2] == row3_list[2] == 'o':
        var = 'o'
    else:
        var = None
    return var


def horizontal_matching(row1_list, row2_list, row3_list):
    if row1_list[0] == row1_list[1] == row1_list[2] == 'x':
        var = 'x'
    elif row1_list[0] == row1_list[1] == row1_list[2] == 'o':
        var = 'o'
    elif row2_list[0] == row2_list[1] == row2_list[2] == 'x':
        var = 'x'
    elif row2_list[0] == row2_list[1] == row2_list[2] == 'o':
        var = 'o'
    elif row3_list[0] == row3_list[1] == row3_list[2] == 'x':
        var = 'x'
    elif row3_list[0] == row3_list[1] == row3_list[2] == 'o':
        var = 'o'
    else:
        var = None
    return var


def diagnol_matching(row1_list, row2_list, row3_list):
    if row1_list[0] == row2_list[1] == row3_list[2] == 'x':
        var = 'x'
    elif row1_list[0] == row2_list[1] == row3_list[2] == 'o':
        var = 'o'
    elif row3_list[0] == row2_list[1] == row1_list[2] == 'x':
        var = 'x'
    elif row3_list[0] == row2_list[1] == row1_list[2] == 'o':
        var = 'o'
    else:
        var = None
    return var


def print_grid(row1_list, row2_list, row3_list):
    for i in row1_list:
        print(f'| {i} |', end='')
    print('')

    for i in row2_list:
        print(f'| {i} |', end='')
    print('')

    for i in row3_list:
        print(f'| {i} |', end='')
    print('\n')


def main():
    # assigns first move randomly to one of the players
    first_player = random.choice(['x', 'o'])
    if first_player == 'x':
        second_player = 'o'
    else:
        second_player = 'x'
    action_list = []
    row1_list = ['.', '.', '.']
    row2_list = ['.', '.', '.']
    row3_list = ['.', '.', '.']
    count = 0
    print('\t' * 9 + 'TIC TAC TOE\n')

    while True:
        if '.' not in row1_list and '.' not in row2_list and '.' not in row3_list:
            print('MATCH DRAW')
            exit()

        if count % 2 == 0:
            print(f"Turn of player1 mark '{first_player}'\n")
            append_to_row_list('1', '1', '.', row1_list, row2_list, row3_list)
            print_grid(row1_list, row2_list, row3_list)

            try:
                row, column = input('enter row and column number(like 12 or 31)\n>')

            except ValueError:
                print('only valid numerical values accepted.\n'
                      'ex: write 23 for second row and third column\n')
                continue

            if not '1' <= row <= '3':
                print('incorrect input, try again...')
                continue
            if not '1' <= column <= '3':
                print('incorrect input, try again...')
                continue

            if f'{row}{column}' in action_list:
                print('value already entered at that position, give another position.\n')
                continue

            action_list.append(f'{row}{column}')
            append_to_row_list(row, column, first_player, row1_list, row2_list, row3_list)

            count += 1

        else:
            print(f"Turn of player2 mark '{second_player}'\n")
            try:
                row, column = input('enter row and column number(like 12 or 31)\n>')

            except ValueError:
                print('only valid numerical values accepted.\n'
                      'ex: write 23 for second row and third column\n')
                continue

            if not '1' <= row <= '3':
                print('incorrect input, try again...')
                continue
            if not '1' <= column <= '3':
                print('incorrect input, try again...')
                continue

            if f'{row}{column}' in action_list:
                print('value already entered at that position, give another position.\n')
                continue

            action_list.append(f'{row}{column}')
            append_to_row_list(row, column, second_player, row1_list, row2_list, row3_list)

            count += 1

        print_grid(row1_list, row2_list, row3_list)

        var1 = horizontal_matching(row1_list, row2_list, row3_list)
        if var1 == first_player:
            print(f"player '{first_player}' won!")
            exit()
        elif var1 == second_player:
            print(f"player {second_player} won!")
            exit()

        var2 = vertical_matching(row1_list, row2_list, row3_list)
        if var2 == first_player:
            print(f"player '{first_player}' won!")
            exit()
        elif var2 == second_player:
            print(f"player '{second_player}' won!")
            exit()

        var3 = diagnol_matching(row1_list, row2_list, row3_list)
        if var3 == first_player:
            print(f"player '{first_player}' won!")
            exit()
        elif var3 == second_player:
            print(f"player '{second_player}' won!")
            exit()
        else:
            continue


if __name__ == '__main__':
    main()
