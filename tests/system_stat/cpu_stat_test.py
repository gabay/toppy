import pytest
from toppy.system_stat import CPUStat


@pytest.fixture
def cpu_stat():
    return CPUStat()

@pytest.fixture
def cpu_stat_after_setup(cpu_stat):
    cpu_stat.setup()
    return cpu_stat

@pytest.fixture
def cpu_stat_after_update(cpu_stat_after_setup):
    cpu_stat_after_setup.update()
    return cpu_stat_after_setup


def test_empty_after_init(cpu_stat):
    assert cpu_stat.utilization is None

def test_has_value_after_setup(cpu_stat_after_setup):
    assert cpu_stat_after_setup.utilization is not None

def test_has_value_after_update(cpu_stat_after_update):
    assert cpu_stat_after_update.utilization is not None
