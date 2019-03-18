import pytest
from pool_object.pool_obj import DriversPool
from pool_object import pool_container


@pytest.fixture(scope='session')
def decoration():
    pool_container.pool = DriversPool()
    yield
    pool_container.pool.fin()
