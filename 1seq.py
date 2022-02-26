n = int(input("Введите количество элементов: "))
my_list = []
for i in range(1, n+1):
     x = input(f"Введите {i} элемент: ")
     my_list.append(x)

print(my_list)
