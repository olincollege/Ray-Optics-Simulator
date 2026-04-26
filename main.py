from controller import CommandLine
from model import Model
from view import Viewer

# Initialize program to run
viewer = Viewer()
model = Model()
controller = CommandLine()
controller.commands["model"] = model.function_dict
controller.model_instance = model
controller.view_instance = viewer

# Print intro message
print(
    "\nWelcome to the Ray Optics Simulator Program \n"
    "This programs lets you input parameters for an optics"
    " simulation, run a simulation, and plot the results \n"
    "Type 'help' for a list of commands and an explanation of the program!\n"
)

# Run program
controller.main_loop()
