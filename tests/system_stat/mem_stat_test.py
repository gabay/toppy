import pytest
from toppy.system_stat import MemoryStat


@pytest.fixture
def mem_stat():
    return MemoryStat()

@pytest.fixture
def mem_stat_after_setup(mem_stat):
    mem_stat.setup()
    return mem_stat

@pytest.fixture
def mem_stat_after_update(mem_stat_after_setup):
    mem_stat_after_setup.update()
    return mem_stat_after_setup


def test_empty_after_init(mem_stat):
    assert mem_stat.mem is None
    assert mem_stat.swap is None

def test_has_values_after_setup(mem_stat_after_setup):
    assert mem_stat_after_setup.mem is not None
    assert mem_stat_after_setup.swap is not None

def test_has_values_after_update(mem_stat_after_update):
    assert mem_stat_after_update.mem is not None
    assert mem_stat_after_update.swap is not None
