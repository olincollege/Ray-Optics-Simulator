import pytest
from model import Model, IdealLens, LightSource


### Category: New

def test_new_source():
    test_model = Model()
    test_source=LightSource('standard',0,0,.001,4,test_model)
    test_model.new_source(test_source)
    assert test_model._source==test_source

def test_new_lens():
    test_model = Model()
    test_lens = IdealLens()

def test_new_ray():
    pass

def test_new_ray_list():
    pass

def test_new():
    pass

### Category: Class

def test_LightSource():
    pass

def test_IdealLens():
    pass

def test_iterate_rays():
    pass

def test_run_simulation():
    pass