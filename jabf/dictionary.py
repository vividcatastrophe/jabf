import glob
import os


class DictionaryRegister(object):
    """ Register for available dictionaries """

    def __init__(self):
        self.register = {}

    def __repr__(self):
        return str(self.register)

    def __getitem__(self, name):
        return self.register[name]

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
            self.register[dictionary_name] = dictionary_path

    def get_dictionary_generator(self, name):
        """ Returns a generator to get data from dictionary """
        if not os.path.exists(self.register[name]):
            raise FileNotFoundError('Dictionary file is missing: {}'
                                    .format(self.register[name]))
        with open(self.register[name], 'r') as dictionary:
            for line in dictionary:
                yield line.strip('\r\n').strip('\n')
