import pytest

from src.main import *
from unittest.mock import patch

@pytest.mark.asyncio
def test_home():
    result = home()
    yield result
    assert home() == {"message": "Aqui é o começo"}

def test_number():
    with patch('random.randint', return_value=12345):
        result = number()
        yield result

    assert result== {"Number": True, "Random_number": 12345}

def test_signuppage():
    nickname_teste = Player(nickname="Fulano", platform="Steam", Active=False)
    result = signuppage(nickname_teste)
    yield result
    assert nickname_teste == result

def test_update_player_negative():
    result = update_player(-5)
    yield result
    assert not result

def test_update_player_positive():
    result = update_player(10)
    yield result
    assert result

def test_delete_player_negative():
    result = delete_player(-5)
    yield result
    assert not result

def test_delete_player_positive():
    result = delete_player(5)
    yield result
    assert result
