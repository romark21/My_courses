import time


def get_time(func):
    def wrapper():
        start = time.time()
        func()
        stop = time.time()
        print(f'Время выполнения функции: {func}, заняло {stop - start}')

    return wrapper


@get_time
def get_req():
    r = requests.get('https://www.youtube.com/')
    print(r.status_code)


get_req()