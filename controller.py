def create_function(id):
    """
    Returns a pre-made function based on a given ID, for testing purposes

    Args:
        id, int to choose which function to return
    """
    match id:
        case 1:
            def temp_function():
                print('hello world')
        case 2:
            def temp_function():
                print('pong')
    return temp_function



class CommandLine():
    """
    Creates an instance of a command line to interact with the model
    """
    commands={}
    quit_var=0
    
    def __init__(self):
        self.commands['quit']=self._quit_func
        self.commands['help']=self._help

    def _quit_func(self):
        self.quit_var=1
    
    def _help(self):
        print(f'Command List: {list(self.commands)}')

    def main_loop(self):
        """
        Main loop for grabbing and using user inputs
        """
        while self.quit_var==0:
            user_input = input('Enter a command: ').split(' ')
            for i,element in enumerate(user_input):
                try:
                    user_input[i]=int(element)
                except ValueError:
                    pass
            try:
                self.commands[user_input[0]]()
            except KeyError: 
                print('Invalid Command!')
            except TypeError: 
                try:
                    self.commands[user_input[0]](user_input[1:])
                except TypeError:
                    try: self.commands[user_input[0]][user_input[1]](user_input[2:])
                    except TypeError:
                        try: self.commands[user_input[0]][user_input[1]][user_input[2]](user_input[3:])
                        except IndexError: 
                            print('Not enough parameters!')
            


class test_model():

    def __init__(self):
        self.lens_list=[]
        self.laser_list=[]
        self.function_dict={}
        self.function_dict['help']=self._help
        self.function_dict['create']={'lens':self.new_lens,'laser':self.new_laser}
        self.function_dict['edit']={'lens':self.edit_lens,'laser':self.edit_laser}
        self.function_dict['print']={'lens':self.print_lens,'laser':self.print_laser}
        self.id=0

    def _help(self, _=None):
        print(f'Model Command List: {list(self.function_dict)}')

    def print_lens(self, _=None):
        print(self.lens_list)
    
    def print_laser(self,_=None):
        print(self.laser_list)

    def edit_lens(self,commands):
        self.lens_list[commands.pop(0)].function_dict[commands[0]](commands[1:])
    
    def edit_laser(self,commands):
        self.laser_list[commands.pop(0)].function_dict[commands[0]](commands[1:])
    
    def new_lens(self,commands):
        self.lens_list.append(self.test_class(commands[0],commands[1]))
    
    def new_laser(self,commands):
        self.laser_list.append(self.test_class(commands[0],commands[1]))
    
    class test_class():
        """
        Test class for debugging command line
        """
        
        def __init__(self,x,y):
            self.x=x; self.y=y
            self.function_dict={'add':self.add, 'x':self.x, 'y':self.y}

        def add(self,commands):
            self.x+=commands[0]; self.y+=commands[1]

        def view(self):
            print(self)

        def __repr__(self):
            return(f'I really like {self.x} but NOT {self.y}.')

main_test=test_model()
app=CommandLine()

app.commands['hello']=create_function(1)
app.commands['ping']=create_function(2)
app.commands['model']=main_test.function_dict

app.main_loop()

