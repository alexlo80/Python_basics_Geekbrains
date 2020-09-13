"""6. * Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей. 
Каждый кортеж хранит информацию об отдельном товаре. 
В кортеже должно быть два элемента — номер товара и словарь с параметрами 
(характеристиками товара: название, цена, количество, единица измерения). 
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]"""


while True:
    user_input = input("Сколько товаров будем вводить,число? ")
    if user_input.isdigit():
        qty = int(user_input)
        break
    else:
        print("Введите число!")
        
count = 1
catalog = []

for _ in range(qty):
    prod_dict = {}
    user_product = input('Введи название товара:')
    prod_dict["название"] = user_product
    user_product = input('Введи цену товара:')
    prod_dict["цена"] = user_product
    user_product = input('Введи количество товара:')
    prod_dict["количество"] = user_product
    user_product = input('Введи eд товара:')
    prod_dict["eд"] = user_product
    catalog_page = (count, prod_dict)
    count += 1
    catalog.append(catalog_page)
    print()
print(catalog) 
print()

"""Необходимо собрать аналитику о товарах. 
Реализовать словарь, в котором каждый ключ — характеристика товара, 
например название, а значение — список значений-характеристик, например список названий товаров.

Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}"""

new_dict_name = []
new_dict_price = []
new_dict_qty = []
new_dict_um = []
list_of_list = [new_dict_name, new_dict_price, new_dict_qty, new_dict_um]
database = ["название", 'цена', 'количество', 'eд']
new_dict_all = {}
z = 1
xx = 0

for k in database:
    for i in range(len(catalog)):
        list_of_list[xx].append(catalog[i][z][k])
#         new_dict_all [k] = list(set(list_of_list[xx])) # усли нужны только уникальные значения
        new_dict_all[k] = list_of_list[xx]  # вариант с не уникальными значениями
    xx += 1    
print(new_dict_all) 