"""
Model class for a ray optics simulation. 
Implement model logic and functionality.
"""

import math

class IdealLens():
    """
    Implement the ideal lens subclass in the Model superclass.

    Implement lenses as elliptical 2D objects with
    uniform indicies of refraction throuought.
    """
    xpos_center = None
    ypos_center = None
    axis1 = None
    axis2 = None
    radius = None
    index_of_refraction = None

    def __init__(self, xpos, ypos, axis1, axis2, radius, index_of_refraction):
        """
        Initialize a lens object. 

        Args:
            xpos: the x position of the lens
            ypos: the y position of the lens
            axis1: length of the first axis
            axis2: length of the second axis
            radius: parameter controlling the size of the ellipse
            index_of_refraction: index of refraction of the lens
        """
        self.xpos_center = xpos
        self.ypos_center = ypos
        self.axis1 = axis1
        self.axis2 = axis2
        self.radius = radius
        self.index_of_refraction = index_of_refraction

class LightRay():
    """
    Implement the lightray subclass. 

    Implement a class for individual lightrays.
    Contain all relevant information for a lightray
    within the object and methods to simulate them.
    """
    _current_medium = None
    _last_medium = None
    _current_x_pos = 0
    _current_y_pos = 0
    _pos_list = []
    _step_size = 0.001
    _relevant_lens_index = None

    def __init__(self, init_angle, init_x_pos, init_y_pos, step_size):
        """
        Initialize a ray object. 

        Args:
            init_angle: initial angle for a ray 
            init_x_pos: initial x position for a ray
            init_y_pos: initial y position for a ray
            step_size: how large of step sizes are taken in simulation
        """
        self._angle = init_angle
        self._current_x_pos = init_x_pos
        self._current_y_pos = init_y_pos
        self._step_size = step_size

    def update_medium(self, lens_list):
        """
        Detect if a ray is within a lens or 
        outside and update medium accordingly.

        Args:
            lens_list: a list of lenses in the simulation
        """
        new_medium_index = 1
        for lens in lens_list:
            converted_x_coord = self._current_x_pos - lens.xpos_center
            converted_y_coord = self._current_y_pos - lens.ypos_center
            radius = (converted_x_coord^2 / lens.axis1^2 +
                        converted_y_coord^2 / lens.axis2^2)
            if radius <= lens.radius:
                new_medium_index = lens.index_of_refraction
                self._relevant_lens_index = lens_list.index(lens)
        self._last_medium = self._current_medium
        self._current_medium = new_medium_index

    def update_angle(self, lens_list):
        """
        Update a ray's angle according to Snell's law. 

        Args:
            lens_list: a list of lenses in the simulation
        """
        if self._last_medium in (None, self._current_medium):
            return

        relevant_lens = lens_list(self._relevant_lens_index)
        converted_x_coord = self._current_x_pos - relevant_lens.xpos_center
        converted_y_coord = self._current_y_pos - relevant_lens.ypos_center
        angle_to_center = math.atan(converted_y_coord / converted_x_coord)

        self._angle = (math.degrees(angle_to_center) + 90
                    + math.degrees(math.asin
                    ((self._last_medium / self._current_medium) *
                    math.sin(math.radians(self._angle))))) % 360

    def take_step(self, lens_list):
        """
        Simulate a ray for a single step. 

        Args:
            lens_list: a list of lenses in the simulation
        """
        self._pos_list.append([self._current_x_pos, self._current_y_pos])
        self.update_medium(lens_list)
        self.update_angle(lens_list)
        self._current_x_pos += (self._step_size *
                                math.cos(math.degrees(self._angle)))
        self._current_y_pos += (self._step_size *
                                math.sin(math.degrees(self._angle)))


class LightSource():
    """
    Implement the LightSource class. 

    A class to define source types and help
    generate lists of ray objects in accordance
    with the source type. 
    """
    _type = None
    def __init__(self, type_of_source):
        self._type = type_of_source

    def generate_ray_list(self, init_x_pos, init_y_pos, step_size):
        """
        Generate a list of rays in accordance
        to source type. 

        Args:
            init_x_pos: the initial x position to generate rays at
            init_y_pos: the inital y position to generate rays at
            step_size: the step size to generate rays with
        """
        if self._type != "standard":
            return
        angle = 0
        ray_list = []
        while angle <= 360:
            ray_list.append(LightRay(angle, init_x_pos, init_y_pos, step_size))
            angle += 10



class Model():
    """
    Implement the Model class. 

    A class to utilize above defined helper classes. 
    Implement functions to run the ray optics simulation. 
    """
    _source = None
    _lens_list = []
    _ray_list = []

    def new_source(self, source_to_add):
        """
        Add a new source. 

        Args:
            source_to_add: the source to add
        """
        self._source = source_to_add

    def new_lens(self, lens_to_add):
        """
        Add a new lens. 

        Args:
            lens_to_add: the lens to add
        """
        self._lens_list.append(lens_to_add)

    def iterate_rays(self):
        """
        Simulate all rays for one timestep.
        """
        for ray in self._ray_list:
            ray.take_step()

    def run_simulation(self, steps_to_take):
        """
        Run the simulation for a defined number of steps. 

        Args:
            steps_to_take: number of steps to take passed as an int
        """
        current_step = 0
        while current_step < steps_to_take:
            self.iterate_rays()
            current_step += 1
        return [self._source, self._lens_list, self._ray_list]


"""
TO DO:
Add code to model class to tie it all together
- Add code to model class to pass neccessary arguments to subclasses to create lenses and whatnot (esp positions and such)
"""