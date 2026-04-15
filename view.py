
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
#from controller import controller

class Viewer(
    #controller? maybe not
):

    def __init__(self):
        '''
        Sets up variables. So far just colormap but I think there'll be more
        '''
        self._colormap = {
            'light': 'gold',
            'LENS_TYPE_1': 'lightcyan',
            'LENS_TYPE_2': 'mistyrose',
        }

    def generate_sim_view(self,model_data):
        '''
        This method is called by the controller to render a plot of the simulation. It is provided
        simulation data via the variable model_data. NOT SURE WHAT THE FORMAT IS BUT
        MUST INCLUDE THE PARAMETERS OF THE OBJECTS (LIGHT SOURCES, LENSES) AND ALL OF THE LIGHT RAYS.
        HOW SHOULD THE PLOT BE RETURNED? (NEW FILE,TRY TO MAKE A POPUP, ETC.)
        '''
        #fig, ax = plt.subplots()

        #for single_ray_coord_list in model_data.structure_containing_all_rays
            #x_list,y_list =  zip(*single_ray_coord_list)               #presumable single_ray_coord_list is formatted like: [(x1,y1),(x2,y2),(x3,y3)]
            #ax.plot(x_list,y_list,color = self.colormap['light'])

        #ASSUMING ONLY 1 LENS RN
        #lens_rect = Rectangle( (model_data.lens.position formatted as tuple), model_data.lens.width, model_data.lens.height, facecolor=self.colormap[model_data.lens.type], alpha=0.1)
        #ax.add_patch(lens_rect)

        #ax.set_title('Simulation Results')
        #ax.set_xlabel('X Axis {UNITS}')
        #ax.set_ylabel('Y Axis {UNITS}')
        #plt.show()
        pass