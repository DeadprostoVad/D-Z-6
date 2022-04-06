def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}')
        result = func(*args, **kwargs)
        print(f'Выполнено {func.__name__}')
        return result
    return wrapper


@ log_decorator
def hello(name: str):
   print(f'Hello, {name}')


hello(str('Vadim'))


