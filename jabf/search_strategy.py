class SearchStrategy(object):
    """ Basic search strategy class to inherit from """
    name = "searchstrategy"
    strategy_params = []

    def __init__(self, strategy_config, dictionary_register):
        raise NotImplementedError(
                'Method __init__ is not implemented')

    def get_generator(self):
        raise NotImplementedError(
                'Method get_generator is not implemented')

    def get_combination_count(self):
        raise NotImplementedError(
                'Method get_combination_count is not implemented')

    def _validate_strategy_config_params(self, strategy_config):
        for param in self.strategy_params:
            if param not in strategy_config:
                raise ValueError('Error in strategy config: parameter {}'
                                 ' is missing'.format(param))
