import yaml
from yaml import FullLoader


def read_style_yaml(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as file:
        return yaml.load(file, FullLoader)


if __name__ == '__main__':
    group: dict = read_style_yaml("../config/default_style.yaml")

    if group.get("title"):
        print(group.get("99"))
