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
            self.command_dict[command_arr[0]](command_arr)

            return 'That was correct format'
        else:
            return 'that wasnt the correct format'

    def add_command(self, command_arr):
        print(command_arr)

    def delete_command(self, *args):
        print("in the delete command")

    def load_file(self):
        print("ello")

    def exit_cmd(self):
        self.is_active = False
