import os
from pprint import pprint


file_name = "recipes.txt"
base_path = os.getcwd()
full_path = os.path.join(base_path, file_name)
print(base_path)
print(full_path)

# # Задача 1
#

def cook_book_reader(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            dish_name = line.strip()
            recipe = []
            qty_ingredients = file.readline()
            for item in range(int(qty_ingredients)):
                ingredient = file.readline().strip()
                ingredient_list = ingredient.split('|')
                ingredients_dict = {}
                ingredients_dict['ingredient_name'] = ingredient_list[0]
                ingredients_dict['quantity'] = ingredient_list[1]
                ingredients_dict['measure'] = ingredient_list[2]
                recipe.append(ingredients_dict)
            file.readline()
            cook_book[dish_name] = recipe
        return cook_book

cook_book = cook_book_reader(full_path)
pprint(cook_book)
print()

#
# # Задача 2
#

def get_shop_list_by_dishes(dishes, person_count):
    order_dishes = {}

    for dish in dishes:
        for key in cook_book.keys():
            if key.upper() == dish.upper():
                for item in cook_book[key]:
                    if item['ingredient_name'] in order_dishes:
                        q = int(item["quantity"]) * person_count + order_dishes[item['ingredient_name']]["quantity"]
                    else:
                        q = int(item["quantity"]) * person_count
                    order_dishes[item['ingredient_name']] = {"quantity": q, "measure": item["measure"]}

    pprint(order_dishes)


get_shop_list_by_dishes(["Омлет", "Фахитос", "Запеченный картофель"], 2)

#__________________________________________________________________
# ЗАДАЧА 3


with open("1.txt", 'r', encoding='utf-8') as file:
    Text_1 = []
    count_lines1 = 0
    for line in file:
        Text_1.append(line.strip())
        count_lines1 += 1

with open("2.txt", 'r', encoding='utf-8') as file:
    Text_2 = []
    count_lines2 = 0
    for line in file:
        Text_2.append(line.strip())
        count_lines2 += 1

with open("3.txt", 'r', encoding='utf-8') as file:
    Text_3 = []
    count_lines3 = 0
    for line in file:
        Text_3.append(line.strip())
        count_lines3 += 1


result = []

min = count_lines1
if count_lines2 < min:
    min = count_lines2
if count_lines3 < min:
    min = count_lines3

if min == count_lines1:
    result.append("1.txt")
    result.append(str(count_lines1))
    result.append(Text_1)
    count_lines1 = 0
elif min == count_lines2:
    result.append("2.txt")
    result.append(str(count_lines2))
    result.append(Text_2)
    count_lines2 = 0
else:
    result.append("3.txt")
    result.append(str(count_lines3))
    result.append(Text_3)
    count_lines3 = 0

if count_lines1 == 0:
    if count_lines2 < count_lines3:
        result.append("2.txt")
        result.append(str(count_lines2))
        result.append(Text_2)
        count_lines2 = 0
    else:
        result.append("3.txt")
        result.append(int(count_lines3))
        result.append(Text_3)
        count_lines3 = 0

elif count_lines2 == 0:
    if count_lines1 < count_lines3:
        result.append("1.txt")
        result.append(str(count_lines1))
        result.append(Text_1)
        count_lines1 = 0
    else:
        result.append("3.txt")
        result.append(str(count_lines3))
        result.append(Text_3)
        count_lines3 = 0

elif count_lines3 == 0:
    if count_lines2 < count_lines1:
        result.append("2.txt")
        result.append(str(count_lines2))
        result.append(Text_2)
        count_lines2 = 0
    else:
        result.append(".txt")
        result.append(str(count_lines1))
        result.append(Text_1)
        count_lines1 = 0

if count_lines1 != 0:
    result.append("1.txt")
    result.append(str(count_lines1))
    result.append(Text_1)
elif count_lines2 != 0:
    result.append("2.txt")
    result.append(str(count_lines2))
    result.append(Text_2)
else:
    result.append("3.txt")
    result.append(str(count_lines3))
    result.append(Text_3)

with open("result", 'w', encoding="utf-8") as file:
    for item in result:
        if type(item) != list:
            file.writelines(item)
            file.writelines('\n')
        else:
            for i in item:
              file.writelines(i)
              file.writelines('\n')

