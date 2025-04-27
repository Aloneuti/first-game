import pytest

from src.main import *
from unittest.mock import patch

@pytest.mark.asyncio
def test_home():
    assert home() == {"message": "Aqui é o começo"}

def test_number():
    with patch('random.randint', return_value=12345):
        result = number()

    assert result== {"Number": True, "Random_number": 12345}

def test_signuppage():
    nickname_teste = Player(nickname="Fulano", platform="Steam", Active=False)
    assert nickname_teste == signuppage(nickname_teste)


def test_update_player_negative():
    assert not update_player(-5)

def test_update_player_positive():
    assert update_player(10)

def test_delete_player_negative():
    assert not delete_player(-5)

def test_delete_player_positive():
    assert not delete_player(5)
