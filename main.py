from controller import CommandLine
from model import Model
from view import Viewer

viewer = Viewer()
model = Model()
controller = CommandLine()

controller.commands['model'] = model.function_dict
controller.commands['view'] = viewer.function_dict

controller.main_loop()
