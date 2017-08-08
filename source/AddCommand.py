class GenericCommand(object):
    def __init__(self, in_options):
        self.my_options = in_options
        print(in_options)


class AddCommand(GenericCommand):
    def __init__(self, in_options):
        print(in_options)
        super(AddCommand, self).__init__(in_options)

    def run(self):
        print(self.my_options)
