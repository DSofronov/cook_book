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
