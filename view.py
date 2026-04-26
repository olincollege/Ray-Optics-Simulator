"""
Defines class 'Viewer' which is used to visualize the simulation results in
the Ray Optics Simulator Project
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

class Viewer:
    """
    A class used to plot simulation results of light rays
    """

    def __init__(self):
        """
        Sets up variables. This includes the internal colormap used,
        the function dictionary, and the plot axis limits.
        """
        self._colormap = {
            "light": "gold",
            "ideal": "lightcyan",
            "LENS_TYPE_2": "mistyrose",
        }
        self._x_range = [0, 2]
        self._y_range = [-1, 1]
        self.function_dict = {}
        self.function_dict["help"] = self._help
        self.function_dict["generate"] = self.generate_sim_view

    def _help(self, _=None):
        print(f"Model Command List: {list(self.function_dict)}")

    def generate_sim_view(self, model_data):
        """
        This method is called by the controller to render a plot of the 
        simulation. It is provided simulation data via the variable model_data.
        The plot is saved to the file sim_result.png

        Args:
            model_data: A list with three sublists [lens_list, ray_list, source]
                as provided by the model when the run_simulation function is run
        """
        # Initialize plot
        plt.style.use("dark_background")
        fig, ax = plt.subplots()
        ax.set_ylim(self._y_range)
        ax.set_xlim(self._x_range)

        # Plot all the light rays
        for light_ray in model_data[1]:
            x_list, y_list = zip(
                *light_ray.pos_list
            )  # single_ray_coord_list format: [(x1,y1),(x2,y2),(x3,y3)]
            ax.plot(x_list, y_list, color=self._colormap["light"])

        # Plot all the lenses
        lens_list = model_data[0]
        for lens in lens_list:
            lens_ellipse = Ellipse(
                (lens.xpos_center, lens.ypos_center),
                lens.axis1 * lens.radius * 2,
                lens.axis2 * lens.radius * 2,
                facecolor=self._colormap[lens.type],
            )
            ax.add_patch(lens_ellipse)

        # Label and save plot
        ax.set_title("Simulation Results")
        ax.set_xlabel("X Axis (meters)")
        ax.set_ylabel("Y Axis (meters)")
        fig.savefig("sim_result.png")
        plt.close(fig)
