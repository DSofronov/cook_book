# Задача № 1, 2

from pprint import pprint


def get_cook_book():
    with open('recipes.txt', 'r', encoding='utf-8') as f:
        cook_book = {}
        cook_book_keys = ['ingredient_name', 'quantity', 'measure']
        for line in f:
            dishes = line.strip()
            num_ingredients = int(f.readline())
            ingr_list = []
            for _ in range(num_ingredients):
                ingredients = f.readline().strip().split('|')
                ingredients = dict(zip(cook_book_keys, ingredients))
                ingr_list.append(ingredients)
            f.readline()
            cook_book[dishes] = ingr_list

    return cook_book


cook_book = get_cook_book()


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingr_name = ingredient['ingredient_name']
            new_quantity = int(ingredient['quantity']) * person_count
            if ingr_name not in shop_list:
                shop_list[ingr_name] = {'measure': ingredient['measure'], 'quantity': new_quantity}
            else:
                shop_list[ingr_name]['quantity'] += new_quantity
    return shop_list


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Салат'], 2))

# Задача № 3

files = ['1.txt', '2.txt', '3.txt']
file_filling = []

for file_name in files:
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file_filling.append((file_name, len(lines), lines))

file_filling.sort(key=lambda x: x[1])

with open('Common_file.txt', 'w', encoding='utf-8') as new_file:
    for file_name, num_lines, lines in file_filling:
        new_file.write(f'{file_name}\n{num_lines}\n')
        new_file.writelines(lines)
        new_file.write('\n')
