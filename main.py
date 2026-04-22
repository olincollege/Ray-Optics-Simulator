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
controller.commands['model']['create']['lens'](1, 0, .25, 2, .3, 1.05, model)
controller.commands['model']['create']['lens'](-1, 1, .4, 2, .6, 1.05, model)
controller.commands['model']['create']['source']('standard', 0, 0, .001, 20, model)

controller.commands['run'](4000)

controller.main_loop()
