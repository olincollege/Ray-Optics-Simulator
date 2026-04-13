
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
            #hprint(f'User Input: {user_input}') # just for debugging
            try:
                self.commands[user_input[0]]()
            except KeyError: 
                print('Invalid Command!')
            except TypeError: 
                self.commands[user_input[0]](user_input)
    
class test_class():
    """
    Test class for debugging command line
    """
    
    def __init__(self,x,y):
        self.x=x; self.y=y
        self.function_dict={'add':self.add, 'x':self.x, 'y':self.y}
    
    def add(self,commands):
        self.x+=commands[1]; self.y+=commands[2]
    
    def view(self):
        print(self)

    def __repr__(self):
        return(f'I really like {self.x} but NOT {self.y}.')

debug_a=test_class(0,0)
debug_b=test_class(0,0)

app=CommandLine()

app.commands['hello']=create_function(1)
app.commands['ping']=create_function(2)
app.commands['add']=debug_a.function_dict['add']
app.commands['print']=debug_a.view
app.main_loop()

