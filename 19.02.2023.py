# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # Задача с урока с определением скорости функций с использованием декоратора # #
#
# import time
#
# def test_speed(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f'время выполнения функции {func.__name__}: {end - start}')
#         return result
#     return wrapper
#
# a = [num for num in range(10000)]
# @test_speed
# def sum_args_gen():
#     return sum(number for number in range(100000000))
#
# @test_speed
# def sum_args_list():
#     return sum([number for number in range(100000000)])
#
# print(sum_args_gen())
# print(sum_args_list())

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # Задача с урока с добавлением в кэш результатов с использованием декоратора # #
#
# def catch_decorator(func):
#     values = {}
#     def wrapper(*args, **kwargs):
#         if values.get((args)) != None:
#             print(values)
#             return values.get((args))
#         result = func(*args, **kwargs)
#         values[(args)] = result
#         print(values)
#         return f'Результат функции {func.__name__}: {result}'
#     return wrapper
#
#
# @catch_decorator
# def sum_args(*args):
#     return sum(args)
#
# print(sum_args(2, 3, 7))
# print(sum_args(4, 5, 22))
# print(sum_args(2, 3, 7))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # Задача с урока с превышением количества раз функции с использованием декоратора # #
#
# def limit_counts(num):
#     def inner_decorator(func):
#         count = 0
#         def wrapper(*args, **kwargs):
#             nonlocal count
#             count += 1
#             if count > num:
#                 raise ValueError('Превышено число вызова функции')
#             result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return inner_decorator
#
# @limit_counts(2)
# def sum_args(*args):
#     return sum(args)
#
#
# res = sum_args(2,3,4)
# print(res)
# res2 = sum_args(2,3,5)
# print(res2)
# res3 = sum_args(25,3,5)
# print(res3)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # Задача с урока с проверкой типов введенных аргументов в аргументы декоратора # #
#
# def validate_args(*args):
#     arr = args
#     def inner_decorator(func):
#         def wrapper(*args):
#             for tip, value in zip(arr, args):
#                 if type(value) != tip:
#                     raise TypeError(f'Ошибка типов! переменная: {value} не относчится к типу: {tip}')
#             return func(*args)
#         return wrapper
#     return inner_decorator
#
#
# @validate_args(str, int)
# def my_func(*args):
#     return f'My name is {args[0]}. I am {args[1]} years old.'
#
# print(my_func('Marat', 33))
# print(my_func('Marat', '33'))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # Домашнее Задание №1 # # # #
#
# def positive_numbers(func):
#     def wrapper(*args):
#         result = func(*args)
#         if result > 0:
#             return result
#         return 0
#     return wrapper
# @ positive_numbers
# def sub(a, b):
#     return a - b
#
#
# print(sub(1, 5))
# print(sub(5, 1))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # Домашнее Задание №2 # # # #
#
# import requests
# import time
#
# def retry(num):
#     count = 0
#     def inner_wrapper(func):
#         def wrapper(*args):
#             nonlocal count
#             count += 1
#             while count <= num:
#                 try:
#                     result = func(*args)
#                     return result
#                 except: Exception
#                 print('Ожидание ответа...')
#                 time.sleep(2)
#                 print('Произошла ошибка.')
#                 time.sleep(1)
#                 print('Повторная попытка отправки запроса...')
#                 time.sleep(1)
#                 count += 1
#             time.sleep(2)
#             return 'Сервер не отвечает'
#
#
#         return wrapper
#     return inner_wrapper
#
#
# @retry(3)
# def get_url_url(url):
#     response = requests.get(url)
#     response.raise_for_status()
#     return response.content
#
# url = "http://numbersapi.com/25/trivia"
# content = get_url_url(url)
# print(content)
# url2 = "http://numbersapi.com/25/tiva"
# content2 = get_url_url(url2)
# print(content2)
#