from abc import ABCMeta, abstractmethod
import os


class Target(object, metaclass=ABCMeta):
    """ Basic target class to inherit from """
    name = 'target'
    target_params = []

    @abstractmethod
    def __init__(self, target_config):
        raise NotImplementedError(
                'Method __init__ is not implemented')

    @abstractmethod
    def check_data(self, data):
        raise NotImplementedError(
                'Method do is not implemented')

    def _validate_target_config_params(self, target_config):
        for param in self.target_params:
            if param not in target_config:
                raise ValueError('Error in target config: parameter {}'
                                 ' is missing'.format(param))


class FileContainerTarget(Target):
    """
    Target class to inherit from to create targets working with file
    containers
    """
    name = 'filecontainertarget'
    target_params = ['container_path']

    def __init__(self, target_config):
        self._validate_target_config(target_config)
        self.container_path = target_config['container_path']

    def _validate_target_config(self, target_config):
        self._validate_target_config_params(target_config)
        if not os.path.isfile(target_config['container_path']):
            raise FileNotFoundError(
                'Container path specified is invalid: {}'
                .format(target_config['container_path']))
        if not os.access(target_config['container_path'], os.R_OK):
            raise PermissionError('Container file is not readable: {}'
                                  .format(target_config['container_path']))
