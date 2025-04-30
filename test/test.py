import pytest
import pytest_asyncio

from src.main import *
from unittest.mock import patch


@pytest.mark.asyncio
async def test_home():
    result = await home()
    assert result == {"message": "Aqui é o começo"}


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

@pytest.mark.asyncio
async def test_check_status():
    result = await check_status()
    assert result["status"] == "API está funcionando perfeitamente."


@pytest.mark.asyncio
async def test_login():
    test_player = Player(nickname="TesteUser", platform="PC", Active=True)
    result = await login(test_player)
    assert "logado com sucesso" in result["message"]

@pytest.mark.asyncio
async def test_list_platforms():
    result = await list_platforms()
    assert isinstance(result["platforms"], list)
    assert "PC" in result["platforms"]

@pytest.mark.asyncio
async def test_activate_player():
    result = await activate_player("Jogador123")
    assert result["activated"] is True
    assert result["nickname"] == "Jogador123"

@pytest.mark.asyncio
async def test_random_platform():
    result = await random_platform()
    assert result["platform"] in ["PC", "Xbox", "PlayStation", "Switch"]