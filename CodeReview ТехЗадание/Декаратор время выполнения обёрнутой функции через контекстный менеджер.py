from contextlib import contextmanager
import time


@contextmanager
def timer():
    start_time = time.time()
    try:
        yield

    raise BaseException()
        print(f'Во время выполнения функции: {timer()}, возникло исключение.'
              f' Проверьте правильость введённых данных!')


    else:
        finish_time = time.time() - start_time
        print(f'Время выполнения функции: {finish_time}')

    # finally:
    #     finish_time = time.time() - start_time
    #     print(f'Время выполнения функции: {finish_time}')


'''
  - Контекстный менеджер. Можно ли сделать так, чтобы с любым исключением работало (выводило информацию)?
  Сейчас исключения "проглатываются" (кроме принта в консоли не узнаем, что было), можно ли сделать так,
   чтобы менеджер работал "прозрачно" (выводил информацию в консоль, а дальше исключение шло как обычно)?
   
   - Если я правильно понял задание, нам нужно убрать все EXCEPT, а оставить только FINALLY. 
   Тогда информация выводится в консоль, а затем выдаётся исключение.
'''


def get_list(num):
    result = [i ** 2 for i in range(num)]
    return result


with timer():
    get_list()
# print(get_list(1000))
