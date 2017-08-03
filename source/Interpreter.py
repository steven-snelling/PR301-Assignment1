
from AddCommand import AddCommand
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
        if InputValidator.validate_command(command_arr):
            self.command_dict[command_arr[0]](command_arr)
            return 'That was correct format'
        else:
            return 'that wasnt the correct format'

    def add_command(self, command_arr):
        options = self.get_options(command_arr)
        AddCommand(options).run()

    def delete_command(self, *args):
        print("in the delete command")

    def load_file(self):
        print("ello")

    def exit_cmd(self):
        self.is_active = False

    def get_options(self, arr):
        for command_item in arr:
            if '-' in command_item:
                option_arr = list(command_item)
                option_arr.pop(0)
        if len(option_arr) == 0:
            print("no options provided")
            return False
        else:
            return option_arr
