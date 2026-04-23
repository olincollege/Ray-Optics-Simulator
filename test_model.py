import pytest
from model import Model, IdealLens, LightSource, LightRay


def test_new_source():
    test_model = Model()
    test_source = LightSource('standard',0,0,0,0,test_model)
    print('test')
    print(test_model)
    assert test_model._source==test_source