import glob
import os


class Dictionary(object):
    """ Represents a dicitonary and gives access to its data """
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def get_dictionary_generator(self):
        """ Returns a generator to get data from dictionary """
        if not os.path.exists(self.path):
            raise FileNotFoundError('Dictionary file is missing: {}'
                                    .format(self.path))
        with open(self.path, 'r') as dictionary:
            for line in dictionary:
                yield line.strip('\r\n').strip('\n')


class DictionaryRegister(object):
    """ Register for dictionary objects """

    def __init__(self):
        self.register = {}

    def __repr__(self):
        return str(self.register)

    def __getitem__(self, name):
        return self.register[name]

    def __iter__(self):
        for dictionary_name in self.register.keys():
            yield dictionary_name

    def register_dictionaries(self, dictionaries_folder):
        """
        Adds dictionaries from dictionary files in dictionaries_folder
        to the register
        """
        if not os.path.isdir(dictionaries_folder):
            raise NotADirectoryError(
                'Dictionary folder specified is not a folder.')
        for file_path in glob.glob(os.path.join(dictionaries_folder, '*')):
            self.register_dictionary(file_path)

    def register_dictionary(self, dictionary_path):
        """ Adds dictionary from dictionary_path to the register """
        if not os.access(dictionary_path, os.R_OK):
            raise PermissionError('Dictionary file is not readable: {}'
                                  .format(dictionary_path))
        dictionary_name = dictionary_path.split(os.path.sep)[-1]
        if dictionary_name not in self.register:
            self.register[dictionary_name] = Dictionary(dictionary_name,
                                                        dictionary_path)
