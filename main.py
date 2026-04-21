from controller import CommandLine
from model import Model
from view import Viewer

viewer = Viewer()
model = Model()
controller = CommandLine()

controller.commands['model'] = model.function_dict
controller.commands['view'] = viewer.function_dict
controller.model_instance=model
controller.view_instance=viewer

# CODE TO TEST FULL PIPELINE
controller.commands['model']['create']['lens'](100, 0, 1, 1, 1, 1, model)
controller.commands['model']['create']['source']('standard', 0, 0, .01, 1, model)
controller.commands['run'](400)

controller.main_loop()
