from glob import iglob
from itertools import chain
from numpy import isin
import yaml
try:
    from yaml import Loader
except:
    from yaml import CLoader as Loader


def parse_yaml_configs(path_patterns):
    def merge(config, next_config):
        if isinstance(config, dict) and isinstance(next_config, dict):
            for key in next_config:
                if key in config:
                    merge(config[key], next_config[key])
                else:
                    config[key] = next_config[key]
        elif config == next_config:
            pass
        elif isinstance(config, list) and isinstance(next_config, list):
            config.extend(next_config)
        else:
            print(config, next_config)
            raise ValueError('Something wrong with the config')

    config = {}
    for path in chain(*(iglob(pattern) for pattern in path_patterns)):
        with open(path, 'r') as f:
            next_config = yaml.load(f, Loader=Loader)
        merge(config, next_config)
    return config


if __name__ == '__main__':
    a = parse_yaml_configs(
        ['eyeriss_like.yaml', 'components/combined.yaml'])
    b = parse_yaml_configs([
        'eyeriss_like.yaml',
        'components/smartbuffer*.yaml'
    ])
    print(a == b)
