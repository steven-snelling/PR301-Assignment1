class InputValidator:
    @staticmethod
    def validate_command(command_arr):

        # TODO Input Validation
        # This is where the input from the user is washed and made sure to work with the program.
        # it currently takes an array from the Interpreter.interpret function and checks if
        # there are 3 elements in that array and returns the corresponding boolean value.

        # When this code is finished it will return either true or false depending on if the input
        #  values are how they should be entered.
        print(command_arr)

        if len(command_arr) == 3:
            if InputValidator.command_isaplha(command_arr[0]):
                return True
            else: False
        else:
            return False

    def command_isaplha(command):
        if command.isalpha():
            return True
        else:
            return False
