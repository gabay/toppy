import pytest
from toppy.system_stat import GPUStat


@pytest.fixture
def gpu_stat():
    return GPUStat()

@pytest.fixture
def gpu_stat_after_setup(gpu_stat):
    gpu_stat.setup()
    return gpu_stat

@pytest.fixture
def gpu_stat_after_update(gpu_stat_after_setup):
    gpu_stat_after_setup.update()
    return gpu_stat_after_setup


def test_empty_after_init(gpu_stat):
    assert gpu_stat.gpus == []
    assert gpu_stat.utilizations == []

def test_has_gpus_after_setup(gpu_stat_after_setup):
    assert gpu_stat_after_setup.gpus != []
    assert gpu_stat_after_setup.utilizations == []

def test_has_values_after_update(gpu_stat_after_update):
    assert gpu_stat_after_update.gpus != []
    assert gpu_stat_after_update.utilizations != []
