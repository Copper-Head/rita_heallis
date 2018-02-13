from datetime import time
import pytest
import rita_heallis as rita


def test_parse_time():
    assert rita.parse_time("1") == time(1)

    with pytest.raises(ValueError):
        rita.parse_time("1.3")

    with pytest.raises(ValueError) as exc_info:
        rita.parse_time("44")

    with pytest.raises(ValueError) as exc_info:
        rita.parse_time("test")


def test_parse_intervals():
    assert rita.parse_intervals('never') == []

    with pytest.raises(rita.RitaInputError):
        rita.parse_intervals("1 2 3")

    assert rita.parse_intervals("10 15") == [(10, 15)]
    assert rita.parse_intervals("10 15 16 20") == [(10, 15), (16, 20)]


def test_parse_exceptions():
    assert rita.parse_exceptions("None") == []

    assert rita.parse_exceptions("1") == [1]
    assert rita.parse_exceptions("1 22") == [1, 22]

    with pytest.raises(ValueError):
        rita.parse_exceptions("test")
