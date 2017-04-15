#!/usr/bin/python3

from jabf.config import config_read
from jabf.search_strategy import load_strategies
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


def main():
    args = parser.parse_args()
    config = config_read(args.config)
    load_strategies(args.search_strategies)


if __name__ == '__main__':
    main()
