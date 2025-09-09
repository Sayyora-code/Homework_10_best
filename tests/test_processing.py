import pytest

from src.processing import filter_by_state, sort_by_date

def test_filter_by_state():
    data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELLED"},
    ]
    assert filter_by_state(data) == [{"id": 1, "state": "EXECUTED"}]

if __name__ == "__main__":
    test_filter_by_state()
    print("Все тесты прошли успешно!")


    def test_filter_by_state():
        data = [
            {"id": 1, "state": "EXECUTED"},
            {"id": 2, "state": "CANCELLED"},
        ]
        assert filter_by_state(data) == [{"id": 1, "state": "EXECUTED"}]

@pytest.mark.parametrize("input_data, expected", [
    ([{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "CANCELLED"}], [{"id": 1, "state": "EXECUTED"}]),
    ([{"id": 3, "state": "EXECUTED"}, {"id": 4, "state": "EXECUTED"}], [{"id": 3, "state": "EXECUTED"}, {"id": 4, "state": "EXECUTED"}]),
])
def test_filter_by_state(input_data, expected):
    assert filter_by_state(input_data) == expected
