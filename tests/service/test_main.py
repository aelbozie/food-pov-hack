import pytest

from service.main import root


@pytest.mark.asyncio
async def test_root():
    n = await root()
    assert len(n) == 1
