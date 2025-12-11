import pytest

from src.decorators import *


def test_log_file(capsys):
    @log()
    def my_function(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        my_function(20, 0)

    result = capsys.readouterr()
    assert (
        "Ошибка в функции: my_function Ошибка: division by zero. Аргументы: (20, 0), {}\n"
        in result.out
    )


def test_log_success(capsys):  # Тест на успешное выполнение функции
    @log()
    def my_function(x, y):
        return x / y

    my_function(20, 5)

    captured = capsys.readouterr()
    assert "Функция: my_function Результат: 4.0" in captured.out


def test_log_to_file(tmp_path):  # Тест на логирование в файл
    log_file = tmp_path / "test_log.txt"

    @log(log_file)
    def my_function(x, y):
        return x / y

    my_function(10, 2)

    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()
        assert "Функция: my_function Результат: 5.0" in content


def test_log_nan_result(capsys):  # Тест на проверку сообщения об ошибке
    @log()
    def my_function(x, y):
        if y == 0:
            return float("nan")
        return x / y

    my_function(10, 0)

    captured = capsys.readouterr()
    assert "Результат: nan" in captured.out


def my_func_div(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"Ошибка в функции: my_func_div Ошибка: {e}. Аргументы: ({a}, {b})")


def test_log_inf_result(
    capsys,
):  # В этом тесте мы проверяем, что функция возвращает "inf",
    # когда знаменатель равен нулю.
    @log()
    def my_function(x, y):
        if y == 0:
            return float("inf")
        return x / y

    my_function(10, 0)

    captured = capsys.readouterr()
    assert "Результат: inf" in captured.out
