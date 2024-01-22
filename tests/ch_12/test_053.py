import pytest

import importlib


from tests.utils.check import check_integrity, DummyRequest


@pytest.fixture(name="module")
def setup_module(user_id, func):
    path = func(__file__, user_id)

    return importlib.import_module(path)


@pytest.fixture(name="integrity_module")
def setup_integrity(func):
    path = func(__file__, "dremdeveloper")

    return importlib.import_module(name=path)


@pytest.fixture(
    name="test_input",
    params=[
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2], 5),
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2], 4),
        ([[1, 1, 1, 1, 1]], [0, 0], [0, 4], 4),
        ([[1]], [0, 0], [0, 0], 0),
    ],
)
def setup(request, integrity_module):
    check_integrity(
        DummyRequest(request.param, request.param_index),
        integrity_module.solution,
    )
    return request.param


@pytest.mark.ch_12
def test(module, test_input):
    # given
    *args, excepted = test_input

    # when
    result = module.solution(*args)

    # then
    assert result == excepted
