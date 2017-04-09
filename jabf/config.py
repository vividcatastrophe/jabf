import json
import sys, traceback


def config_read(config_path):
    """
    Reads a file with json config
    Params:
        config_path - string with path to config file
    Returns a dictionary with config
    """
    with open(config_path) as config_file:
        try:
            config = json.load(config_file)
        except json.decoder.JSONDecodeError:
            traceback.print_exc(limit=0)
            sys.exit("Config file is inconsistent")
    _config_validate(config)
    return config


class InvalidConfigError(Exception):
    pass


config_sections = ["search strategy", "target module", "output method"]


def _config_validate(config):
    """
    Validates the config against the supposed config scheme. Raises
    InvalidConfigError if any issues are found.
    Params:
        config - dictionary with configuration
    """
    issues = []
    for section in config_sections:
        if section not in config.keys():
            issues.append("Config doesn't contain {} section".format(section))
        elif "name" not in config[section]:
            issues.append("Config section '{}' has no 'name'".format(section))
        elif "params" not in config[section]:
            issues.append("Config section '{}' has no 'params'".format(section))

    if len(issues) > 0:
        raise InvalidConfigError('\n'.join(issues))
