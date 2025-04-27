import pytest
import pytest_asyncio

from src.main import *
from unittest.mock import patch


@pytest.mark.asyncio
async def test_home():
    result = await home()
    assert home() == {"message": "Aqui é o começo"}


@pytest.mark.asyncio
async def test_number():
    with patch('random.randint', return_value=12345):
        result = await number()

    assert result== {"Number": True, "Random_number": 12345}


@pytest.mark.asyncio
async def test_signuppage():
    nickname_teste = Player(nickname="Fulano", platform="Steam", Active=False)
    result = await signuppage(nickname_teste)
    assert nickname_teste == result

@pytest.mark.asyncio
async def test_update_player_negative():
    result = await update_player(-5)
    assert not result

@pytest.mark.asyncio
async def test_update_player_positive():
    result = await update_player(10)
    assert result

@pytest.mark.asyncio
async def test_delete_player_negative():
    result = await delete_player(-5)
    assert not result

@pytest.mark.asyncio
async def test_delete_player_positive():
    result = await delete_player(5)
    assert result
