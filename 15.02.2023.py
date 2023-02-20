# # Задача 1 с урока, про товары в корзине
# class ShoppingCart:
#     def __init__(self):
#         self.basket = []
#         self.discounts = [['Молоко', 10], ['Творог', 5]] ## скидка в %
#     def add_item(self, item: str, price: int, quantity: int):
#         for product in self.basket:
#             if product['item'] == item and product['price'] == price:
#                 product['quantity'] += quantity
#                 return print(f'{item} добавлен в корзину')
#         self.basket.append({'item': item, 'price': price, 'quantity': quantity})
#         return print(f'{item} добавлен в корзину')
#
#
#     def remove_item(self, item, quantity):
#         count = 0
#         for product in self.basket:
#             if product['item'] == item:
#                 if product['quantity'] >= quantity:
#                     product['quantity'] -= quantity
#                     if product['quantity'] == 0:
#                         del self.basket[count]
#                         return print(f'{item} удален из корзины')
#             else:
#                 count += 1
#         return print(f'{item} в корзине нет!')
#
#
#
#     def get_total_price(self):
#         sum = 0
#         for product in self.basket:
#             availability = False
#             for discount in self.discounts:
#                 if product['item'] == discount[0]:
#                     sum = sum + (product['price'] * product['quantity']) * ((100 - discount[1]) / 100)
#                     availability = True
#             if availability == False:
#                 sum += (product['price'] * product['quantity'])
#
#         return print(f'Общая стоимость: {sum} рублей')
#
#
#     def list_all_items(self):
#         for product in self.basket:
#             print(f'Продукт: {product["item"]}\t\tКоличество: {product["quantity"]}\t\tЦена: {product["price"]}')
#
#
# my_cart = ShoppingCart()
# my_cart.add_item('Творог', 100, 1)
# my_cart.add_item('Молоко', 50, 2)
# my_cart.add_item('Яйца', 100, 1)
# my_cart.get_total_price()
# my_cart.list_all_items()
# my_cart.add_item('Творог', 100, 10)
# my_cart.remove_item('Молоко', 2)
# my_cart.remove_item('Молоко', 2)
# my_cart.list_all_items()
# my_cart.get_total_price()


# # # #  # # # # #  # # # #  # # # #  # # # #  # # # #  # # # #  # # # #  # # # #  # # # #  # # # #  # # # #  # # # #

# # Задача 2 с урока, про товары в корзине

# class TextProcessor:
#     def __init__(self, name):
#         self.name = name
#         try:
#             with open(name, mode='r', encoding='UTF-8') as r:
#                 self.text = r.readlines()
#                 print('Файл успешно открыт!')
#         except Exception:
#             print('Такого файла нет!')
#
#
#     def read_file(self):
#         for line in self.text:
#             print(line, end='')
#
#
#     def count_words(self):
#         sum = 0
#         for line in self.text:
#             index = line.split(' ')
#             for item in index:
#                 if item != '-':
#                     sum += 1
#         print(f'Количество слов: {sum}')
#
#
#     def count_characters(self):
#         sum = 0
#         for line in self.text:
#             sum += len(line)
#         print(f'Количество символов в тексте: {sum}')
#
#
#     def count_sentences(self):
#         sum = 0
#         for line in self.text:
#             for item in line:
#                 if item == '.' or item == '!' or item == '?':
#                     sum += 1
#         print(f'Количество предложений в тексте: {sum}')
#
#
#     def reverse(self):     ## метод перезаписывает файл с изменениями
#         self.text_str = ''
#         for line in self.text:
#             for item in line:
#                 self.text_str += item
#         self.text = self.text_str[::-1]
#         with open(self.name, 'w', encoding='UTF-8') as w:
#            w.write(self.text)
#
#
#     def replace(self, old_word, new_word):   ## метод перезаписывает файл с изменениями
#         text_array = []
#         for line in self.text:
#             text_array.append([line])
#         for i in range(len(text_array)):
#             text_array[i] = text_array[i][0].split()
#         for i in range(len(text_array)):
#             for j in range(len(text_array[i])):
#                 if text_array[i][j].lower() == old_word.lower():
#                     text_array[i][j] = new_word
#                 elif old_word.lower() in text_array[i][j]:
#                     if len(old_word.lower()) + 1 == len(text_array[i][j]):
#                         if text_array[i][j][-1] in ',.:?!':
#                             tmp = text_array[i][j][-1]
#                             text_array[i][j] = new_word + tmp
#                             del tmp
#         text_str = ''
#         for i in range(len(text_array)):
#             text_str += ' '.join(text_array[i])
#             if i != len(text_array) - 1:
#                 text_str += '\n'
#         with open(self.name, 'w', encoding='UTF-8') as w:
#             w.write(text_str)
#
#
# tp = TextProcessor('text.txt')
# tp.count_words()
# tp.count_characters()
# tp.count_sentences()
# # tp.reverse()
# # tp.replace('время', 'ЧТО-ТО')

# # # #  # # # # #  # # # #  # # # #  # # # #  # # # #  # # # #  # # # #  # # # #  # # # #  # # # #  # # # #  # # # #
# # Домашнее задание 1
# class Phonebook:
#     def __init__(self):
#         print('Телефонная книга создана!')
#         self.db = {}
#
#     def add_contact(self, name:str, phone_number:str):
#         self.db.update({name: phone_number})
#         print(f'{name} добавлен.')
#
#     def remove_contact(self, name:str):
#         if self.db.get(name):
#             self.db.pop(name)
#             print(f'{name} удален!')
#         else:
#             print('Такого пользователя не существует')
#
#     def update_contact(self, name:str, phone_number:str):
#         self.db.update({name: phone_number})
#
#     def get_contact(self, name):
#         if self.db.get(name):
#             print(f'{name} {self.db[name]}')
#         else:
#             print('Такого пользователя не существует')
#
#     def get_all_contacts(self):
#         for key, value in self.db.items():
#             print(f'{key} {value}')
#
# my_book = Phonebook()
# my_book.add_contact('Марат', '+79508383893')
# my_book.add_contact('Расиля', '+79508383000')
# my_book.add_contact('Иван', '253046')
# my_book.get_all_contacts()
# my_book.update_contact('Марат', '534565546')
# my_book.get_contact('Марат')
# my_book.remove_contact('Марат')
# my_book.get_contact('Марат')
# print(my_book.__dict__)


# # # #  # # # # #  # # # #  # # # #  # # # #  # # # #  # # # #  # # # #  # # # #  # # # #  # # # #  # # # #  # # # #
# # Домашнее задание 2
# import time
# class Timer():
#
#     def __init__(self):
#         print('Таймер создан')
#
#     def start(self):
#         self.on = time.time()
#         print('Таймер запущен')
#
#     def stop(self):
#         self.off = time.time()
#         print('Таймер остановлен')
#
#     def reset(self):
#         self.on = 0
#         self.off  = 0
#         print('Таймер сброшен')
#
#     def elapsed_time(self):
#         print(f'Прошло {round((self.off - self.on), 1)} секунды')
#
#
#
# my_timer = Timer()
# my_timer.start()
# print('Ожидание 3 секунды...')
# time.sleep(3)
# my_timer.stop()
# my_timer.elapsed_time()
# my_timer.reset()
# print(my_timer.__dict__)





