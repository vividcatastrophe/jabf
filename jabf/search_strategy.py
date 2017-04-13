import glob
import os
from jabf.utils import load_module

SearchStrategyRegister = {}

default_modules_folder = os.path.join(
                                   os.path.dirname(os.path.realpath(__file__)),
                                   "search_strategy_modules")


def load_strategies(modules_folder=default_modules_folder):
    """ Loads search strategies from modules found in the modules_folder """
    for file_path in glob.glob(os.path.join(modules_folder, "*.py")):
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
    Checks if it contains the obligatory search strategy methods and attributes
    Returns True or False
    """
    attributes = ["name", "strategy_params"]
    methods = ["get_combination_count", "get_generator"]
    is_valid = True
    for attr in attributes:
        if not hasattr(strategy_class, attr):
            is_valid = False
    for method in methods:
        if not hasattr(strategy_class, method) or \
                not type(getattr(strategy_class, method)) \
                .__name__ == "function":
            is_valid = False
    return is_valid
