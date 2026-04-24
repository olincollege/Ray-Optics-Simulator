class CommandLine():
    """
    Creates an instance of a command line to interact with the model
    """
    commands={}
    quit_var=0
    model_instance=None
    view_instance=None

    def __init__(self):
        """
        Initializes basic commands: quit, help, and run
        """
        self.commands['quit'] = self._quit_func
        self.commands['help'] = self._help
        self.commands['run'] = self._run_simulation

    def _quit_func(self):
        self.quit_var=1

    def _help(self, command):
        match command:
            case 'model':
                self.commands['model']['help']()
            case 'run':
                print("Syntax: 'run <timesteps>'")
            case _:
                print(
                    "help\nYou first need to specify model parameters using the 'model'"
                    " command.\nThe program lets you specify light source parameters"
                    " like position and ray density and lens parameters\nlike refractivity"
                    " and size (use 'help model' for more precise information on inputs)\n"
                    "You can then use the 'run' command to run the simulation and plot the"
                    " results ('help run' can give more info on how to run the model)\n"
                    "As a reminder here is the command list:"
                )
                print(f"Command List: {list(self.commands)}")

    def _run_simulation(self, steps=40):
        """
        Runs the current simulation and displays the data with the viewer

        Args: 
            steps: int, representing the amount of steps to run the simulation for
        """
        print('STARTING SIMULATION')
        model_data = self.model_instance.run_simulation(steps)
        print('SIMULATION FINISHED')
        self.view_instance.generate_sim_view(model_data)
        print('SIMULATION RENDERED')

    def user_input(self, _input=None):
        """
        Takes in and formats user input.
        """
        if _input is None:
            _input=input('Enter a command: ')
        self._cmd_to_func(_input.split(' '))
    
    def debug_input(self, _input):
        """
        takes input text to use in testing environment.
        """
        _cmd = _input.split(' ')
        for i,element in enumerate(_cmd):
            try:
                _cmd[i]=float(element)
            except ValueError:
                pass
        return(_cmd)

    def _cmd_to_func(self, _cmd):
        # Clean up user input, unstring floats
        for i,element in enumerate(_cmd):
            try:
                _cmd[i]=abs(float(element))
            except ValueError:
                pass
        # ['model', 'create', 'lens', 1, 0, .125, .25, 2]
        if len(_cmd)>1:
            if _cmd[1]=='create':
                _cmd.append(self.model_instance)
        elif _cmd[0]=='help':
            _cmd.append(None)
        # ['model', 'create', 'lens', 1, 0, .125, .25, 2, model]
        try:
            self.commands[_cmd[0]]()
        except KeyError:
            print('Invalid Command!')
        except TypeError:
            try:
                self.commands[_cmd[0]](*_cmd[1:])
                # self.commands['model'](['create', 'lens', 1, 0, .125, .25, 2, model])
                # model.function_dict(['create', 'lens', 1, 0, .125, .25, 2, model])
            except KeyError:
                print('Invalid Command!')
            except TypeError:
                try:
                    self.commands[_cmd[0]][_cmd[1]](*_cmd[2:])
                    # model.function_dict['create'](['lens', 1, 0, .125, .25, 2, model])
                    # {'source':LightSource,'lens':IdealLens}(['lens', 1, 0, .125, .25, 2, model])
                except KeyError:
                    print('Invalid Command!')
                except TypeError:
                    try:
                        self.commands[_cmd[0]][_cmd[1]][_cmd[2]](*_cmd[3:])
                    # IdealLens([1, 0, .125, .25, 2, model])
                    # This is the call of IdealLens with the provided parameters
                    except KeyError:
                        print('Invalid Command!')
                    except TypeError:
                        try:
                            self.commands[_cmd[0]][_cmd[1]][_cmd[2]][_cmd[3]](*_cmd[4:])
                        except IndexError:
                            print('Not enough parameters!')
                        except (TypeError,KeyError):
                            print(_cmd)
                            print('Invalid Command, Please Try Again!')

    def main_loop(self):
        """
        Main loop for grabbing and using user inputs
        """
        while self.quit_var==0:
            self.user_input()
