import time


def log(filename=None):
    """Декоратор для логирования поведения функции"""

    def wrapper(func):
        def inner(*args, **kwargs):
            start_time = time.time()  # Инициализируем здесь
            log_message = ""
            try:
                result = func(*args, **kwargs)
                log_message = f"Функция: {func.__name__} Результат: {result}"
            except Exception as e:
                error_message = (
                    f"Ошибка в функции: {func.__name__} Ошибка: {e}. "
                    f"Аргументы: {args}, {kwargs}"
                )
                log_message = error_message
            if filename:
                with open(
                    filename, "a", encoding="utf-8"
                ) as f:  # Используй 'a' для добавления
                    f.write(f"{start_time} - {log_message}\n")
            else:
                print(f"{start_time} - {log_message}")

        return inner

    return wrapper


@log("mylog.txt")
def my_func_div(x, y) -> float:
    """Функция деления x на y"""
    res_div = x / y
    return res_div


my_func_div(20, 0)
