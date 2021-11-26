import yaml


def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    return data


if __name__ == '__main__':
    data = load_yaml('data1.json')
    print(data)
