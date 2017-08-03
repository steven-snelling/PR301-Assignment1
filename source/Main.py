from InterpreterController import *
from CommandLineView import *
from Interpreter import *


if __name__ == '__main__':
    InterpreterController(CommandLineView(), Interpreter()).go()

