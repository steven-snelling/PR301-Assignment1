class InputValidator:
    @staticmethod
    def validate_input(command_arr):

        # TODO Input Validation
        # This is where the input from the user is washed and made sure to work with the program.
        # it currently takes an array from the Interpreter.interpret function and checks if
        # there are 3 elements in that array and returns the corresponding boolean value.

        # When this code is finished it will return either true or false depending on if the input
        #  values are how they should be entered.

<<<<<<< HEAD
        # This is different from the inputValidator which will clean the information the user adds to
        # the system via the add command
=======
>>>>>>> c441bcc1755bf461ebe3ecaa1245b074fe0c301e

        if len(command_arr) == 3:
            return True
        else:
            return False
