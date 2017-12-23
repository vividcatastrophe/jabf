#!/usr/bin/python3

from runners.local_runner import LocalRunnerBuilder
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
                         '..', 'config', 'config.json'))
parser.add_argument(
    '-d',
    '--dictionaries',
    help='path to folder containing dictionaries',
    metavar='DICTIONARIES_FOLDER',
    default=os.path.join(os.path.dirname(os.path.realpath(__file__)),
                         '..', 'dictionaries'))
parser.add_argument(
    '-s',
    '--search-strategies',
    help='path to folder containing modules with search strategies',
    metavar='STRATEGIES_FOLDER',
    default=os.path.join(os.path.dirname(os.path.realpath(__file__)),
                         'strategies', 'modules'))
parser.add_argument(
    '-t',
    '--targets',
    help='path to folder containing modules with targets',
    metavar='TARGETS_FOLDER',
    default=os.path.join(os.path.dirname(os.path.realpath(__file__)),
                         'targets', 'modules'))

parser.add_argument(
    '-o',
    '--output',
    help='path to folder containing modules with output methods',
    metavar='OUTPUT_METHODS_FOLDER',
    default=os.path.join(os.path.dirname(os.path.realpath(__file__)),
                         'output', 'modules'))


def main():
    args = parser.parse_args()
    builder = LocalRunnerBuilder()
    builder.register_strategies(args.search_strategies)
    builder.register_dictionaries(args.dictionaries)
    builder.register_targets(args.targets)
    builder.register_outputs(args.output)
    builder.build(args.config)
    if not builder.get_runner().run():
        exit(1)


if __name__ == '__main__':
    main()
