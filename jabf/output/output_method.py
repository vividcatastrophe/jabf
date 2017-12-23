from abc import ABCMeta, abstractmethod


class OutputMethod(object, metaclass=ABCMeta):
    """ Basic output class to inherit from """
    name = 'output'
    output_params = []

    @abstractmethod
    def __init__(self, output_config):
        raise NotImplementedError(
                'Method __init__ is not implemented')

    @abstractmethod
    def write(self, data):
        raise NotImplementedError(
                'Method write is not implemented')

    def _validate_output_config_params(self, output_config):
        for param in self.output_params:
            if param not in output_config:
                raise ValueError('Error in output config: parameter {}'
                                 ' is missing'.format(param))
