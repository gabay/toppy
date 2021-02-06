import pytest
from toppy.system_stat import IOStat


@pytest.fixture
def io_stat():
    return IOStat()

@pytest.fixture
def io_stat_after_setup(io_stat):
    io_stat.setup()
    return io_stat

@pytest.fixture
def io_stat_after_update(io_stat_after_setup):
    io_stat_after_setup.update()
    return io_stat_after_setup


def test_empty_after_init(io_stat):
    assert io_stat.keys == []
    assert io_stat.stats == {}

def test_has_keys_after_setup(io_stat_after_setup):
    assert io_stat_after_setup.keys != []
    assert io_stat_after_setup.stats == {}

def test_has_values_after_update(io_stat_after_update):
    assert io_stat_after_update.keys != []
    assert io_stat_after_update.stats != {}
