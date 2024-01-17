import pytest

import importlib


@pytest.fixture(name="module")
def setup_module(user_id, func):
    path = func(__file__, user_id)

    return importlib.import_module(path)


@pytest.fixture(
    name="test_input",
    params=[
        ([1, 3, 2, 5, 4], 9, 3),
        ([2, 2, 3, 3], 10, 4),
    ],
)
def setup(request):
    return request.param


@pytest.mark.ch_16
def test(module, test_input):
    # given
    *args, excepted = test_input

    # when
    result = module.solution(*args)

    # then
    assert result == excepted
