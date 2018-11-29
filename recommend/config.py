import json


def config(filename:str = 'config.json', section: str = 'DEFAULT'):
    """Read scoring configuration file

    :param filename: (optional) File name with parameter related to scoring
    :param section: (optional) section name
    :return: :dict: scoring config paramter
    :rtype: dict
    """
    with open(filename, 'r') as f:
        parser = json.load(f)
    weights = None
    if section in parser:
        weights = parser[section]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')
    return weights


if __name__ == '__main__':
    pass
