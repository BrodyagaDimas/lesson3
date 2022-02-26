numbers_seq_1 = input("Введите первый список цифр через ',', или';', или'/' ").replace(';', ',').replace('/', ',').split(',')
number_list_1 = [int(elem) for elem in numbers_seq_1]

numbers_seq_2 = input("Введите второй список цифр через ',', или';', или'/' ").replace(';', ',').replace('/', ',').split(',')
number_list_2 = [int(elem) for elem in numbers_seq_2]

for num in number_list_1[::-1]:
    if num in number_list_2:
        number_list_1.remove(num)

print(f'Результат: {number_list_1}')