from OptionProvider import *
from InputValidator import InputValidator

class Interpreter:
    def __init__(self):
        self.is_active = True
        self.next_command = 0
        self.command_dict = {
                                'add': self.add_command,
                                'delete': self.delete_command,
                                'exit': self.exit_cmd
                             }

    def interpret(self, command):
        command_arr = command.split()
        if InputValidator.validate_input(command_arr):
            return 'That was correct format'
        else:
            return 'that wasnt the correct format'

    def add_command(self, *args):
        options = OptionProvider.add_options(self)
        options[args[0]]()

    def delete_command(self, *args):
        print("in the delete command")

    def load_file(self):
        print("ello")

    def exit_cmd(self):
        self.is_active = False
