import glob
import os
from inspect import isabstract
import jabf.utils


class ClassRegister(object):
    """ Register for specific class """

    def __init__(self, reg_class):
        self.register = {}
        self.reg_class = reg_class

    def __repr__(self):
        return str(self.register)

    def __getitem__(self, name):
        return self.register[name]

    def load_classes_from_folder(self, modules_folder):
        """
        Loads classes from modules found in the modules_folder
        """
        for file_path in glob.glob(os.path.join(modules_folder, '*.py')):
            self.load_classes_from_module(file_path)

    def load_classes_from_module(self, module_path):
        """
        Loads and registers classes found in the module_path file
        """
        module = jabf.utils.load_module(module_path)

        classes = [getattr(module, cl)
                   for cl in dir(module)
                   if type(getattr(module, cl))
                   .__name__ in ['type', 'ABCMeta']]
        for cl in classes:
            if self._is_valid_class(cl):
                self.register_class(cl)

    def register_class(self, loaded_class):
        """ Puts the loaded_class into the register """
        if loaded_class.name not in self.register:
            self.register[loaded_class.name] = loaded_class
        else:
            raise KeyError('Class {} is already registered'
                           .format(loaded_class.name))

    def _is_valid_class(self, loaded_class):
        """
        Verifies whether the provided loaded_class is a valid class
        for register
        Returns True or False
        """
        return issubclass(loaded_class, self.reg_class) and \
            loaded_class != self.reg_class and \
            not isabstract(loaded_class)
