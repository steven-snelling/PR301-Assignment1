
class CommandLineView:

    def request_command(self):
        command = input("> ")
        return command

    def command_response(self,command_str, command_result):
        if not command_result:
            print('The command "' + command_str + '" wasn`t recognized' )
        else:
            print(command_result)

    def wrong_command_format(self):
        print("ay")