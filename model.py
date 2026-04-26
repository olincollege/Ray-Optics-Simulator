"""
Model class for a ray optics simulation. 
Implement model logic and functionality.
"""

import math

class Model():
    """
    Implement the Model class. 

    A class to utilize above defined helper classes. 
    Implement functions to run the ray optics simulation. 
    """
    _source = None
    _lens_list = []
    _ray_list = []

    def __init__(self):
        self.function_dict = {}
        self.function_dict['help'] = self._help
        self.function_dict['create'] = {'source':LightSource,'lens':IdealLens}
        #self.function_dict['run'] = self.run_simulation
        self.function_dict['debug'] = self._print

    def _print(self):
        print(f'lens list: {self._lens_list}')
        print(f'ray list: {self._ray_list}')
        print(f'source: {self._source}')

    def _help(self, command=None):
        print(
                "\nTo run the model it is necessary to specify light source parameters"
                " and lens parameters\nThis is done through 'model create source' and"
                " 'model create lens'\n\nSource expects a 5 inputs after the command: "
                "lens_type, x_position, y_position, ray_step_size, ray_angle_step_size\n"
                "   lens_type currently only supports 'standard' which represents an ideal lens.\n"
                "   x_position is in meters and should ideally be between -1 and 1\n"
                "   y_position is in meters and should ideally be between 0 and 2\n"
                "   Ray_step_size represents how far to step each light ray in the simulation (meters).\n"
                "   Ray_angle_step_size represents the rotation between each light ray sent out (degrees)\n"
                "Example light source command: 'model create source standard 0 0 0.001 1'\n\n"
                "Lens expects 6 inputs after the command: "
                "x_position, y_position, width, height, radius, refraction_index\n"
                "   x_position and y_position give the coordinates for the center of the lens in meters\n"
                "   width is the horizontal thickness of the lens from the center to the edge (meters)\n"
                "   height is the vertical height of the lens from the center to the edge (meters)\n"
                "   radius acts as a multiplier for the axis, it is reccomended to set this to 1\n"
                "   index_of_refraction represents the index of refraction for the lens\n"
                "Example lens command: 'model create lens 1 0 0.125 0.5 0.25 1.5'"
                )

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

    def new_ray(self, ray_to_add):
        """
        Add a new ray. 

        Args:
            ray_to_add: the ray to add
        """
        self._ray_list.append(ray_to_add)

    def new_ray_list(self, ray_list_to_add):
        """
        Replace the ray list. 

        Args:
            ray_list_to_add: the ray list to add
        """
        self._ray_list = ray_list_to_add

    def iterate_rays(self):
        """
        Simulate all rays for one timestep.
        """
        for ray in self._ray_list:
            ray.take_step(self._lens_list)


    def run_simulation(self, steps_to_take):
        """
        Run the simulation for a defined number of steps. 

        Args:
            steps_to_take: number of steps to take passed as an int
        """
        steps_to_take=abs(steps_to_take)
        current_step = 0
        while current_step < steps_to_take:
            self.iterate_rays()
            current_step += 1
        return [self._lens_list, self._ray_list, self._source]

class IdealLens(Model):
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
    model_data=None

    def __init__(self, xpos, ypos, axis1, axis2, radius, index_of_refraction, model_object):
        """
        Initialize a lens object.

        Args:
            xpos: the x position of the lens
            ypos: the y position of the lens
            axis1: length of the first axis, from center to edge (half of total width)
            axis2: length of the second axis, from center to edge (half of total height)
            radius: parameter controlling the size of the ellipse
            index_of_refraction: index of refraction of the lens
            model_object: the model to add the lens to
        """
        if index_of_refraction<1 or axis1<=0 or axis2<=0 or radius<=0 or xpos <=0 or ypos <=0:
            raise ValueError("INVALID INPUT")
        self.xpos_center = xpos
        self.ypos_center = ypos
        self.axis1 = axis1
        self.axis2 = axis2
        self.radius = radius
        self.index_of_refraction = index_of_refraction
        Model.new_lens(model_object, self)
        self.type='ideal'


class LightSource(Model):
    """
    Implement the LightSource subclass in the Model superclass.

    A class to define source types and help
    generate lists of ray objects in accordance
    with the source type.
    """

    def __init__(self, type_of_source, init_x, init_y, step_size, angle_step_size, model_object):
        """
        Initialize LightSource class and generate a list of rays in accordance
        to source type.

        Args:
            init_x_pos: the initial x position to generate rays at
            init_y_pos: the inital y position to generate rays at
            step_size: the step size to generate rays with
            angle_step_size: the step size of angle to generate rays with
            model_object: the model to add the rays to
        """

        #Set Lightsource Type (currently only supports 'standard')
        if type_of_source != "standard":
            raise ValueError("Invalid Lightsource Type")
        self._type = type_of_source

        if init_x <=0 or init_y <=0 or step_size <=0 or angle_step_size <=0:
            raise ValueError("All parameter values must be above zero")

        #Build Light Ray List
        Model.new_source(model_object, self)
        angle = 0
        ray_list = []
        while angle < 360:
            ray_list.append(LightRay(angle, init_x, init_y, step_size))
            angle += angle_step_size

        #Send Light Ray List to Model and reset
        Model.new_ray_list(model_object, ray_list)
        ray_list = []


class LightRay(Model):
    """
    Implement the LightRay subclass in the Model superclass.

    Implement a class for individual lightrays.
    Contain all relevant information for a lightray
    within the object and methods to simulate them.
    """

    def __init__(self, init_angle, init_x_pos, init_y_pos, step_size):
        """
        Initialize a ray object.

        Args:
            init_angle: initial angle for a ray
            init_x_pos: initial x position for a ray
            init_y_pos: initial y position for a ray
            step_size: how large of step sizes are taken in simulation
        """
        self.pos_list=[]
        self._angle = init_angle
        self._current_x_pos = init_x_pos
        self._current_y_pos = init_y_pos
        self._step_size = step_size
        self._relevant_lens_index = None
        self._current_medium = None
        self._last_medium = None

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

            eq_radius = (
                converted_x_coord ** 2 / (lens.axis1 * lens.radius) ** 2 +
                converted_y_coord ** 2 / (lens.axis2 * lens.radius) ** 2
            )
            if eq_radius <= 1:
                new_medium_index = lens.index_of_refraction
                self._relevant_lens_index = lens_list.index(lens)

        self._last_medium = self._current_medium
        self._current_medium = new_medium_index

    def update_angle(self, lens_list):
        """
        Update ray angle using Snell's Law (vector form).
        """

        # Detect is there is no change in medium
        if self._last_medium in (None, self._current_medium):
            return

        lens = lens_list[self._relevant_lens_index]

        #Ray direction vector
        dx = math.cos(math.radians(self._angle))
        dy = math.sin(math.radians(self._angle))

        #Surface normal (gradient of ellipse)
        x = self._current_x_pos - lens.xpos_center
        y = self._current_y_pos - lens.ypos_center

        nx = x / (lens.axis1 * lens.radius) ** 2
        ny = y / (lens.axis2 * lens.radius) ** 2

        # Normalize normal
        norm_mag = math.sqrt(nx**2 + ny**2)
        if norm_mag == 0:
            return  # avoid division by zero

        nx /= norm_mag
        ny /= norm_mag

        #Ensure normal points against ray
        dot = dx * nx + dy * ny
        if dot > 0:
            nx = -nx
            ny = -ny
            dot = dx * nx + dy * ny

        #Snell’s Law
        n1 = self._last_medium
        n2 = self._current_medium
        ratio = n1 / n2

        k = 1 - ratio**2 * (1 - dot**2)

        #Total Internal Reflection
        if k < 0:
            # Reflect: R = D - 2(D·N)N
            rx = dx - 2 * dot * nx
            ry = dy - 2 * dot * ny
        else:
            # Refract
            rx = ratio * dx - (ratio * dot + math.sqrt(k)) * nx
            ry = ratio * dy - (ratio * dot + math.sqrt(k)) * ny

        #Convert back to angle
        self._angle = math.degrees(math.atan2(ry, rx)) % 360


    def take_step(self, lens_list):
        """
        Simulate a ray for a single step.

        Args:
            lens_list: a list of lenses in the simulation
        """
        self.pos_list.append((self._current_x_pos, self._current_y_pos))
        self.update_medium(lens_list)
        self.update_angle(lens_list)
        self._current_x_pos += self._step_size * math.cos(
            math.radians(self._angle)
        )
        self._current_y_pos += self._step_size * math.sin(
            math.radians(self._angle)
        )
