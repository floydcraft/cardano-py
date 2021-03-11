import yaml
from pathlib import Path


class CardanoPyConfig(object):
    target_config_yaml = None

    def load(self, target_config_dir: str):
        target_config_dir = Path(target_config_dir)

        if target_config_dir.is_dir():
            target_config = target_config_dir.joinpath("cardanopy.yaml")
        else:
            target_config = target_config_dir
            target_config_dir = target_config_dir.parent

        if not target_config.is_file():
            raise ValueError(f"Target config '{target_config}' is not a file. e.g., 'cardanopy.yaml'")

        if not target_config.exists():
            raise ValueError(f"Target file '{target_config}' does not exist.")

        try:
            with open(target_config, "r") as file:
                self.target_config_yaml = yaml.full_load(file.read())
        except Exception as ex:
            raise ValueError(f"Failed to create. Unable to copy config to '{target_config_dir}'. {type(ex).__name__} {ex.args}")

    def set(self, property_name: str, property_value):
        self.target_config_yaml[property_name] = property_value

    def get(self, property_name: str):
        return self.target_config_yaml[property_name]

    def save(self, target_config_dir: Path):
        target_config_dir = Path(target_config_dir)

        if target_config_dir.is_dir():
            target_config = target_config_dir.joinpath("cardanopy.yaml")
        else:
            target_config = target_config_dir
            target_config_dir = target_config_dir.parent

        if not target_config.is_file():
            raise ValueError(f"Target config '{target_config}' is not a file. e.g., 'cardanopy.yaml'")

        if not target_config.exists():
            raise ValueError(f"Target file '{target_config}' does not exist.")

        try:
            with open(target_config, "w") as file:
                yaml.dump(self.target_config_yaml, file)
        except Exception as ex:
            raise ValueError(f"Failed to create. Unable to copy config to '{target_config_dir}'. {type(ex).__name__} {ex.args}")

    def get_substitutions(self):
        return self.target_config_yaml['substitutions']

    substitutions = property(get_substitutions)

    def get_name(self):
        return self.target_config_yaml['name']

    name = property(get_name)

    def get_root(self):
        return self.target_config_yaml['root']

    root = property(get_root)

    def get_network(self):
        return self.target_config_yaml['network']

    network = property(get_network)

    def get_config(self):
        return self.target_config_yaml['config']

    config = property(get_config)

    def get_topologyPath(self):
        return self.target_config_yaml['topologyPath']

    topologyPath = property(get_topologyPath)

    def get_topology(self):
        return self.target_config_yaml['topology']

    topology = property(get_topology)

    def get_databasePath(self):
        return self.target_config_yaml['databasePath']

    databasePath = property(get_databasePath)

    def get_hostAddr(self):
        return self.target_config_yaml['hostAddr']

    hostAddr = property(get_hostAddr)

    def get_port(self):
        return self.target_config_yaml['port']

    port = property(get_port)

    def get_socketPath(self):
        return self.target_config_yaml['socketPath']

    socketPath = property(get_socketPath)

    def get_docker(self):
        return DockerConfig(self.target_config_yaml['docker'])

    docker = property(get_docker)


class DockerConfig(object):
    config = None

    def __init__(self, config):
        self.config = config

    def get_image(self):
        return self.config['image']

    image = property(get_image)
