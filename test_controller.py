# pylint: skip-file
import pytest
from controller import CommandLine

def test_input_splicing():
    test_controller = CommandLine()
    test_command = test_controller.debug_input('model create lens 1 2 3 4 5 6')
    assert test_command == ['model', 'create', 'lens', 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]

def test_function_dict_calling():
    test_controller=CommandLine()
    test_model_function_dict={'create':{'lens':1,'source':2},'help':0}
    test_controller.commands['model'] = test_model_function_dict
    print(test_controller.user_input('model create lens'))
