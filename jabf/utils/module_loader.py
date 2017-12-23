import importlib
import importlib.util
import os
import sys


def load_module(module_path, module_name=None):
    """
    Loads a module from given path
    Params:
        module_path - string containing path to the module_path,
        module_name - string containing the name which the loaded module should
                      be given; if it is not provided, file name is taken as
                      module name
    Returns the loaded module object
    """
    if module_name is None:
        module_name = module_path.split(os.path.sep)[-1].strip('.py')
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.modules[module_name] = module
    return module
