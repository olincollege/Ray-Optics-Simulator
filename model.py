"""
Docstring Here
"""

import math

class IdealLens():
    """
    Docstring Here
    """
    xpos_center = None
    ypos_center = None
    axis1 = None
    axis2 = None
    radius = None
    index_of_refraction = None

    def __init__(self, xpos, ypos, axis1, axis2, radius, index_of_refraction):
        self.xpos_center = xpos
        self.ypos_center = ypos
        self.axis1 = axis1
        self.axis2 = axis2
        self.radius = radius
        self.index_of_refraction = index_of_refraction

class LightRay():
    """
    Docstring Here
    """
    _current_medium = None
    _last_medium = None
    _current_x_pos = 0
    _current_y_pos = 0
    _pos_list = []
    _step_size = 0.001

    def __init__(self, init_angle, init_x_pos, init_y_pos, step_size):
        self._angle = init_angle
        self._current_x_pos = init_x_pos
        self._current_y_pos = init_y_pos
        self._step_size = step_size

    def update_medium(self, lens_list):
        """
        Docstring Here
        """
        new_medium_index = 1
        for lens in lens_list:
            converted_x_coord = self._current_x_pos - lens.xpos_center
            converted_y_coord = self._current_y_pos - lens.ypos_center
            radius = (converted_x_coord^2 / lens.axis1^2 +
                        converted_y_coord^2 / lens.axis2^2)
            if radius <= lens.radius:
                new_medium_index = lens.index_of_refraction
        self._last_medium = self._current_medium
        self._current_medium = new_medium_index

    def update_angle(self):
        """
        Docstring Here
        """
        if self._last_medium in (None, self._current_medium):
            return
        self._angle = math.degrees(math.asin
                    ((self._last_medium / self._current_medium) *
                    math.sin(math.radians(self._angle))))

    def take_step(self, lens_list):
        """
        Docstring Here
        """
        self._pos_list.append([self._current_x_pos, self._current_y_pos])
        self.update_medium(lens_list)
        self.update_angle()
        self._current_x_pos += (self._step_size *
                                math.cos(math.degrees(self._angle)))
        self._current_y_pos += (self._step_size *
                                math.sin(math.degrees(self._angle)))


class LightSource():
    """
    Docstring Here
    """
    _type = None
    def __init__(self, type_of_source):
        self._type = type_of_source


class Model():
    """
    Docstring Here
    """
    _source = None
    _lens_list = []
    _ray_list = []

    def new_source(self, source_to_add):
        """
        Docstring Here
        """
        self._source = source_to_add

    def new_lens(self, lens_to_add):
        """
        Docstring Here
        """
        self._lens_list.append(lens_to_add)

    def iterate_ray(self):
        """
        Docstring Here
        """
        pass

    def run_simulation(self):
        """
        Docstring Here
        """

        return [self._source, self._lens_list, self._ray_list]


"""
TO DO:
Implement correct angle calculation (tangent plane of lens surface)
Add code to lightsource class to generate list of rays
Add code to model class to be able to make lenses (or otherwise figure it out)
Add code to model class to tie it all together
"""