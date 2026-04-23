import pytest
from model import Model, IdealLens, LightSource, LightRay


def test_new_source():
    test_model = Model()
    test_source = LightSource()
    tester.new_source(test_model,)
    assert ASSERTION_HERE