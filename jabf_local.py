#!/usr/bin/python3

from jabf.config import config_read
from jabf.search_strategy import load_strategies


def main():
    config = config_read()
    load_strategies()


if __name__ == '__main__':
    main()
