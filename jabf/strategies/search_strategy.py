from abc import ABCMeta, abstractmethod


class SearchStrategy(object, metaclass=ABCMeta):
    """ Basic search strategy class to inherit from """
    name = "searchstrategy"
    strategy_params = []

    @abstractmethod
    def __init__(self, strategy_config, dictionary):
        raise NotImplementedError(
                'Method __init__ is not implemented')

    @abstractmethod
    def get_generator(self):
        raise NotImplementedError(
                'Method get_generator is not implemented')

    @abstractmethod
    def get_combination_count(self):
        raise NotImplementedError(
                'Method get_combination_count is not implemented')

    def _validate_strategy_config_params(self, strategy_config):
        for param in self.strategy_params:
            if param not in strategy_config:
                raise ValueError('Error in strategy config: parameter {}'
                                 ' is missing'.format(param))
