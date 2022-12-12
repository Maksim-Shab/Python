# Напишите программу, удаляющую из текста все слова,
# содержащие ""абв"".

# some_list = input('Напишите текст: ').split(' ')
# a, b, v = 'а', 'б', 'в'
# new_list = list(filter(lambda i: a not in i and b not in i and v not in i, some_list))
# # for i in range(len(some_list)):
# #     if a in some_list[i] or b in some_list[i] or v in some_list[i]:
# #         continue
# #     else:
# #         new_list.append(some_list[i])
# print(new_list)



# Создайте программу для игры в ""Крестики-нолики"".

# board = list(range(1,10))

# def draw_board(board):
#     print('-'*12)
#     for i in range(3):
#         print('|', board[-3-i*3],'|', board[-2-i*3], '|', board[-1-i*3], '|')
#         print('-'*12)

# def take_input(revers):
#     valid = False
#     while not valid:
#         player_index = input('Выберите ячейку ' + revers + ' --> ')
#         try:
#             player_index =int(player_index)
#         except:
#             print('Вы уверены, что ввели число?')
#             continue
#         if player_index >= 1 and player_index <= 9:
#             if(str(board[player_index-1]) not in 'XO'):
#                 board[player_index-1] = revers
#                 valid = True
#             else:
#                 print('Ячейка занята.')
#         else:
#             print('Попробуйте ещё раз.')

# def win(board):
#     victory = ((0,1,2),(3,4,5),(6,7,8),
#                (0,3,6),(1,4,7),(2,5,8),
#                (0,4,8),(2,4,6))
#     for i in victory:
#         if board[i[0]] == board[i[1]] == board[i[2]]:
#             return board[i[0]]
#     return False

# def main(board):
#     counter =0
#     vic = False
#     while not vic:
#         draw_board(board)
#         if counter % 2 == 0:
#             take_input('X')
#         else:
#             take_input('O')
#         counter +=1
#         if counter > 4:
#             tmp = win(board)
#             if tmp:
#                 print(tmp,'Победа')
#                 vic = True
#                 break
#             if counter == 9:
#                 print('Ходы закончились. Ничья!)')
# main(board)


# Реализуйте RLE алгоритм:
# реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def press(file, new_str):
    with open(file, 'r', encoding='utf-8') as text:
        with open(new_str, 'w', encoding='utf-8') as new_str:
            some_list = text.readline()
            count = 1
            for i in range(len(some_list) - 1):
                if some_list[i] == some_list[i + 1]:
                    count += 1
                else:
                    new_str.write(str(count) + some_list[i])
                    count = 1
            new_str.write(str(count) + some_list[i + 1])
            
def depress(file, res_str):
    with open(file, 'r', encoding='utf-8') as text:
        with open(res_str, 'w', encoding='utf-8') as res_str:
            some_list = text.readline()
            for i in range(0, len(some_list), 2):
                res_str.write(int(some_list[i]) * some_list[i + 1])

press('file_hw_5.txt', 'new_str_hw_5.txt')
depress('new_str_hw_5.txt', 'res_str_hw_5.txt')