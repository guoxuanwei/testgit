import configparser
import os


def read_conf(path):
    conf = configparser.ConfigParser()
    conf.read(path)
    # config_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config")
    # print(config_dir)
    config_dir = os.path.dirname(__file__)
    print(config_dir)
    data = conf.get('showapi', 'SECRET_ID')
    return data


if __name__ == '__main__':
    reult = read_conf('conf.ini')
    print(reult)