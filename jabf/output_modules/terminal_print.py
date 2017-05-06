from jabf.output_method import OutputMethod


class TerminalPrint(OutputMethod):
    name = 'terminalprint'

    def __init__(self, output_config):
        pass

    def write(self, data):
        print('Data found: {}'.format(data))
