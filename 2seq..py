unique_numbers_list = []

numbers_sequence = input("Введите цифры через ',' либо ';' либо '/': ").replace(";", ",").replace("/", ",").split(",")
numbers_list = [int(elem) for elem in numbers_sequence]

for elem in numbers_list:
    if numbers_list.count(elem) == 1:
        unique_numbers_list.append(elem)

print(unique_numbers_list)