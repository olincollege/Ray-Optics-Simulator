# pylint: skip-file
import pytest
from controller import CommandLine

def build_print_function(text):
    """
    builds a function to be used in later testing.
    
    Args:
        text, string, the first half of the printed output
    Returns:
        temp_func, function, prints whatever input text (text2) is given.
    """
    def temp_func(text2, _=None):
        print(text+text2)
    return(temp_func)

def test_input_splicing():
    """
    testing that the commands are properly formatted.
    """
    test_controller = CommandLine()
    test_command = test_controller.debug_input('model create lens 1 2 3 4 5 6')
    assert test_command == ['model', 'create', 'lens', 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]

### For function_dict test
@pytest.mark.parametrize("input_val, expected_output", [
    ('model create lens world', 'hello world\n'),
    ('model help now', 'help me! now\n'),
    ('model create source pong', 'ping pong\n'),
    ('model create source source', 'ping source\n'),
    ('model invalid', 'Invalid Command!\n'),
    ('AMERICA create source', 'Invalid Command!\n'),
]   )

def test_function_dict_calling(input_val, expected_output, capsys):
    """
    Tests for calling nested dictionaries, also
    testing for invalid inputs
    """
    test_controller=CommandLine()
    lens_function=build_print_function('hello ')
    source_function=build_print_function('ping ')
    help_function=build_print_function('help me! ')
    test_model_function_dict={'create':{'lens':lens_function,'source':source_function},'help':help_function}
    test_controller.commands['model'] = test_model_function_dict
    test_controller.user_input(input_val)
    captured = capsys.readouterr()
    assert captured.out==expected_output

def test_run_simulation(capsys):
    """
    Testing Controller's run_simulation function with dummy
    viewer and model objects.
    """
    class test_model_class():
        def run_simulation(self,steps):
            return steps * 2
    
    class test_viewer_class():
        def generate_sim_view(self, model_data):
            print(model_data)
    
    test_model=test_model_class()
    test_viewer=test_viewer_class()
    test_controller=CommandLine()
    test_controller.view_instance,test_controller.model_instance=test_viewer,test_model
    test_controller.user_input('run 1500')
    captured=capsys.readouterr()
    assert captured.out=='STARTING SIMULATION\nSIMULATION FINISHED\n3000.0\nSIMULATION RENDERED\n'

def test_quit():
    """
    Test that the controller quit function
    changes the controller's quit_var
    """
    test_controller=CommandLine()
    test_controller.user_input('quit')
    assert test_controller.quit_var == 1