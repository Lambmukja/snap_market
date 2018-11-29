from configparser import ConfigParser()


def config(filename:str = 'config.ini', section: str = 'weight'):
    """Read scoring configuration file

    :param filename: (optional) File name with parameter related to scoring
    :param section: (optional) section name
    :return: :dict: scoring config paramter
    :rtype: dict
    """
    parser = ConfigParser().read(filename)
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        if debug:
            raise Exception(f'Section {section} not found in the {filename} file')
    return config


if __name__ == '__main__':
    pass
