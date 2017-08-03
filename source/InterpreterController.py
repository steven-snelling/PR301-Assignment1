class InterpreterController:
    def __init__(self, in_view, in_interpreter):
        self.my_view = in_view
        self.my_interpreter = in_interpreter

    def go(self):
        while self.my_interpreter.is_active:
            command = self.my_view.request_command()
            self.my_view.command_response(command, self.my_interpreter.interpret(command))
