# pylint: skip-file
import pytest
from model import Model, IdealLens, LightSource, LightRay

### Category: New

def test_new_source():
    """
    Test for the model function new_source, makes sure
    a new source is actually assigned correctly.
    """
    test_model = Model()
    test_model_2 = Model()
    test_source=LightSource('standard',0,0,.001,4,test_model_2)
    test_model.new_source(test_source)
    assert test_model._source==test_model_2._source

def test_new_lens():
    # (, xpos, ypos, axis1, axis2, radius, index_of_refraction, model_object)
    """
    Test for the model function new_lens, makes sure
    a new lens is actually assigned corectly.
    """
    test_model = Model()
    test_model_2 = Model()
    test_lens = IdealLens(1, 1, 2, 2, 1, 1.5, test_model_2)
    test_model.new_lens(test_lens)
    assert test_model._lens_list==test_model_2._lens_list

def test_new_ray():
    """
    Test for the model funtion new_ray, makes sure
    a new ray is actually assigned correctly.
    """
    test_model = Model()
    test_model_2 = Model()
    test_ray = LightRay(2, .001, 4, test_model_2)
    test_model.new_ray(test_ray)
    test_model_2.new_ray(test_ray)
    assert test_model._ray_list==test_model_2._ray_list==[test_ray]

def test_new_ray_list():
    """
    Test for the model function new_ray_list, makes sure
    a new ray list is actually assigned correctly.
    """
    test_model = Model()
    test_model_2 = Model()
    test_ray_1 = LightRay(2, .001, 4, test_model_2)
    test_ray_2 = LightRay(4, .001, 4, test_model_2)
    test_ray_list=[test_ray_1,test_ray_2]
    test_model.new_ray_list(test_ray_list)
    assert test_model._ray_list==test_ray_list

### Category: Class

def test_LightSource_lengths():
    test_model = Model(); test_source = LightSource('standard',1,1,.001,360,test_model)
    assert len(test_model._ray_list)==1
    test_model = Model(); test_source = LightSource('standard',1,1,.001,180,test_model)
    assert len(test_model._ray_list)==2
    test_model = Model(); test_source = LightSource('standard',1,1,.001,1,test_model)
    assert len(test_model._ray_list)==360
    test_model = Model(); test_source = LightSource('standard',1,1,.001,4,test_model)
    assert len(test_model._ray_list)==90

def test_IdealLens():
    test_model = Model()
    test_lens = IdealLens(1, 2, 6, 9, 3, 1.5, test_model)
    test_lens = test_model._lens_list[0]
    assert test_lens.xpos_center==1
    assert test_lens.ypos_center==2
    assert test_lens.axis1==6
    assert test_lens.axis2==9
    assert test_lens.radius==3
    assert test_lens.index_of_refraction==1.5

test_IdealLens()
### Category: Model functions

def test_iterate_rays():
    test_model = Model()
    test_lens = IdealLens(1, 2, 4, 4, 2, 1.5, test_model)
    test_source = LightSource('standard', 0, 0, .001, 4, test_model)
    test_model.iterate_rays()
    assert len(test_model._ray_list[0].pos_list)==1

def test_run_simulation():
    test_model = Model()
    test_lens = IdealLens(1, 2, 4, 4, 2, 1.5, test_model)
    test_source = LightSource('standard', 0, 0, .001, 4, test_model)
    test_data = test_model.run_simulation(40)
    assert len(test_model._ray_list[0].pos_list)==40
    assert len(test_model._ray_list[0].pos_list)==40
    assert test_data[2]==test_model._source
    assert test_data[1]==test_model._ray_list
    assert test_data[0]==test_model._lens_list
