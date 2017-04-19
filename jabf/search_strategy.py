class SearchStrategy(object):
    """ Basic search strategy class to inherit from """
    name = "searchstrategy"
    strategy_params = []

    def get_generator(self):
        raise NotImplementedError(
                'Method get_generator is not implemented')

    def get_combination_count(self):
        raise NotImplementedError(
                'Method get_combination_count is not implemented')
