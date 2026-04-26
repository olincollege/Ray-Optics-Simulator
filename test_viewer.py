# pylint: skip-file
import pytest
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from view import Viewer
from model import Model, IdealLens, LightSource


def test_single_lens():
    """
    Test that the viewer can plot a single lens
    """
    test_viewer = Viewer()
    test_model = Model()
    # (xpos, ypos, axis1, axis2, radius, index_of_refraction, model_object))
    test_lens = IdealLens(1, 0, 0.05, 0.5, 1, 1, test_model)
    # (type_of_source, init_x, init_y, step_size, angle_step_size, model_object)
    test_source = LightSource("standard", 0, 0, 0.001, 4, test_model)
    test_data = test_model.run_simulation(1)
    print(test_data[0])
    try:
        test_viewer.generate_sim_view(test_data)
    except:
        raise Exception("Viewer failed to plot single lens")


def test_multi_lens():
    """
    Test that the viewer can plot 3 seperate lenses with different locations and parameters
    """
    test_viewer = Viewer()
    test_model = Model()
    # (xpos, ypos, axis1, axis2, radius, index_of_refraction, model_object))
    test_lens = IdealLens(1, 0.2, 0.08, 0.5, 1, 1, test_model)
    test_lens = IdealLens(1.5, -0.5, 0.5, 0.2, 1, 1, test_model)
    test_lens = IdealLens(0.4, 0.6, 0.2, 1.2, 0.5, 1, test_model)
    # (type_of_source, init_x, init_y, step_size, angle_step_size, model_object)
    test_source = LightSource("standard", 0, 0, 0.001, 4, test_model)
    test_data = test_model.run_simulation(1)
    print(test_data[0])
    try:
        test_viewer.generate_sim_view(test_data)
    except:
        raise Exception("Viewer failed to plot multiple lenses")


def test_many_rays():
    """
    Test that the viewer can plot extremely dense rays
    """
    test_viewer = Viewer()
    test_model = Model()
    # (xpos, ypos, axis1, axis2, radius, index_of_refraction, model_object))
    test_lens = IdealLens(
        100, 0, 1, 1, 1, 1, test_model
    )  # Far away to not effect simulation
    # (type_of_source, init_x, init_y, step_size, angle_step_size, model_object)
    test_source = LightSource("standard", 1, 0, 0.001, 1, test_model)
    test_data = test_model.run_simulation(1000)
    print(test_data[0])
    try:
        test_viewer.generate_sim_view(test_data)
    except:
        raise Exception("Viewer failed plot light rays")
