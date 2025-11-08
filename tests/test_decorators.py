from src.decorators import log
from functools import wraps


def test_log_file(capsys):
    @log()
    def my_function(x, y) -> float:
        return x / y

    my_function(20, 0)
    result = capsys.readouterr()
    assert (
        str(result.out)
        == "Ошибка в функции: my_function Ошибка: division by zero. Аргументы: (20, 0), {}\n"
    )


def log_1():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(
                    f"Ошибка в функции: {func.__name__} Ошибка: {str(e)}. Аргументы: {args}, {kwargs}"
                )

        return wrapper

    return decorator
