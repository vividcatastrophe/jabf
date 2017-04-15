import glob
import os
from jabf.utils import load_module

SearchStrategyRegister = {}


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


def load_strategies(modules_folder):
    """ Loads search strategies from modules found in the modules_folder """
    for file_path in glob.glob(os.path.join(modules_folder, '*.py')):
        load_strategy(file_path)


def load_strategy(module_path):
    """ Loads and registers search strategies found in the module_path file """
    module = load_module(module_path)

    strategy_classes = [getattr(module, cl)
                        for cl in dir(module)
                        if type(getattr(module, cl))
                        .__name__ == 'type']
    for strategy in strategy_classes:
        if is_valid_strategy(strategy):
            register_strategy(strategy)


def register_strategy(strategy_class):
    """ Puts the search strategy_class into the SearchStrategyRegister """
    SearchStrategyRegister[strategy_class.name] = strategy_class


def is_valid_strategy(strategy_class):
    """
    Verifies whether the provided strategy_class is a valid search strategy
    Returns True or False
    """
    return issubclass(strategy_class, SearchStrategy) and \
        strategy_class != SearchStrategy
