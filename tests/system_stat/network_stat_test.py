import pytest
from toppy.system_stat import NetworkStat


@pytest.fixture
def network_stat():
    return NetworkStat()

@pytest.fixture
def network_stat_after_setup(network_stat):
    network_stat.setup()
    return network_stat

@pytest.fixture
def network_stat_after_update(network_stat_after_setup):
    network_stat_after_setup.update()
    return network_stat_after_setup


def test_empty_after_init(network_stat):
    assert network_stat.keys is None
    assert network_stat.stats is None

def test_has_values_after_setup(network_stat_after_setup):
    assert network_stat_after_setup.keys is not None
    assert network_stat_after_setup.stats is None

def test_has_values_after_update(network_stat_after_update):
    assert network_stat_after_update.keys is not None
    assert network_stat_after_update.stats is not None
