#!/usr/bin/python3

from jabf.config import config_read
from jabf.search_strategy import SearchStrategy
from jabf.dictionary import DictionaryRegister
from jabf.class_register import ClassRegister
import os
import argparse


parser = argparse.ArgumentParser(
    description='Just Another BruteForcer is a modular tool for finding '
                'specific values according to search strategies.')
parser.add_argument(
    '-c',
    '--config',
    help='path to jabf config file',
    metavar='CONFIG_FILE',
    default=os.path.join(os.path.dirname(os.path.realpath(__file__)),
                         'jabf', 'config', 'config.json'))
parser.add_argument(
    '-s',
    '--search-strategies',
    help='path to folder containing modules with search strategies',
    metavar='STRATEGIES_FOLDER',
    default=os.path.join(os.path.dirname(os.path.realpath(__file__)),
                         'jabf', 'search_strategy_modules'))
parser.add_argument(
    '-d',
    '--dictionaries',
    help='path to folder containing dictionaries',
    metavar='DICTIONARIES_FOLDER',
    default=os.path.join(os.path.dirname(os.path.realpath(__file__)),
                         'jabf', 'dictionaries'))


def main():
    args = parser.parse_args()
    config = config_read(args.config)
    dictionary_register = DictionaryRegister()
    dictionary_register.register_dictionaries(args.dictionaries)
    strategy_register = ClassRegister(SearchStrategy)
    strategy_register.load_classes_from_folder(args.search_strategies)

    strategy_class = strategy_register[config['search strategy']['name']]
    strategy = strategy_class(
        config['search strategy']['params'], dictionary_register)
    data_gen = strategy.get_generator()


if __name__ == '__main__':
    main()
