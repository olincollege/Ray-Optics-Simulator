"""
Defines class 'Viewer' which is used to visualize the simulation results in 
the Ray Optics Simulator Project
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

# from controller import controller


class Viewer:
    """
    A class used to plot simulation results of light rays
    """
    def __init__(self):
        """
        Sets up variables. This involves the internal colormap used and 
        the function dictionary.
        """
        self._colormap = {
            "light": "gold",
            "Empty": "lightcyan",
            "LENS_TYPE_2": "mistyrose",
        }
        self.function_dict = {}
        self.function_dict["help"] = self._help
        self.function_dict["generate"] = self.generate_sim_view

    def _help(self, _=None):
        print(f"Model Command List: {list(self.function_dict)}")

    def generate_sim_view(self, model_data):
        """
        This method is called by the controller to render a plot of the simulation. 
        It is provided simulation data via the variable model_data. The plot is saved 
        to the file sim_result.png
        """
        fig, ax = plt.subplots()
        #model_data[1]=[model_data[1][0]]
        #print(model_data[1][0].pos_list)
        for light_ray in model_data[1]:
            #x_list, y_list = zip(
            #    *light_ray.pos_list
            #)  # single_ray_coord_list format: [(x1,y1),(x2,y2),(x3,y3)]
            ax.plot(light_ray.pos_list, color=self._colormap["light"])

        # ASSUMING ONLY 1 LENS
        #lens_list=model_data[0]
        #lens_coords = (
        #    lens_list[0].xpos,
        #    lens_list[0].ypos
        #)
        #lens_ellipse = Ellipse(
        #    lens_coords,
        #    model_data[0][1][4]*model_data[0][1][5],
        #    model_data[0][1][3]*model_data[0][1][5],
        #    facecolor=self._colormap[model_data[0][1][0]]
        #)
        #ax.add_patch(lens_ellipse)

        ax.set_title("Simulation Results")
        ax.set_xlabel("X Axis (meters)")
        ax.set_ylabel("Y Axis (meters)")
        fig.savefig("sim_result.png")
