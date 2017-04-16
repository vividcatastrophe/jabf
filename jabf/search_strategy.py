import glob
import os
import jabf.utils


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


class SearchStrategyRegister(object):
    """ Register for available search strategies """

    def __init__(self):
        self.register = {}

    def __repr__(self):
        return str(self.register)

    def __getitem__(self, name):
        return self.register[name]

    def load_strategies(self, modules_folder):
        """
        Loads search strategies from modules found in the modules_folder
        """
        for file_path in glob.glob(os.path.join(modules_folder, '*.py')):
            self.load_strategy(file_path)

    def load_strategy(self, module_path):
        """
        Loads and registers search strategies found in the module_path file
        """
        module = jabf.utils.load_module(module_path)

        strategy_classes = [getattr(module, cl)
                            for cl in dir(module)
                            if type(getattr(module, cl))
                            .__name__ == 'type']
        for strategy in strategy_classes:
            if self._is_valid_strategy(strategy):
                self.register_strategy(strategy)

    def register_strategy(self, strategy_class):
        """ Puts the search strategy_class into the SearchStrategyRegister """
        self.register[strategy_class.name] = strategy_class

    def _is_valid_strategy(self, strategy_class):
        """
        Verifies whether the provided strategy_class is a valid search strategy
        Returns True or False
        """
        return issubclass(strategy_class, SearchStrategy) and \
            strategy_class != SearchStrategy
