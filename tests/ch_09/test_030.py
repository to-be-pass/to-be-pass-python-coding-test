import pytest

import importlib


@pytest.fixture(name="module")
def setup_module(user_id, func):
    path = func(__file__, user_id)

    return importlib.import_module(path)


@pytest.fixture(
    name="test_input",
    params=[
        (["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"], 16),
        (["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"], -1),
    ],
)
def setup(request):
    return request.param


@pytest.mark.ch_09
def test(module, test_input):
    # given
    *args, excepted = test_input

    # when
    result = module.solution(*args)

    # then
    assert result == excepted
