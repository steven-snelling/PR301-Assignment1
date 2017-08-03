class OptionProvider:
    def __init__(self):
        self.add_options = {'l': self.load_file}

    def load_file(self):
        print("in the load file method")

