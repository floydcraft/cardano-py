import yaml
from pathlib import Path


class CardanoPyConfig(object):
    def __init__(self):
        pass

    target_config_yaml = None

    def load(self, target_config_file: Path):

        if not target_config_file.is_file():
            print(f"Target config '{target_config_file}' is not a file. e.g., 'cardanopy.yaml'")
            return False

        if not target_config_file.exists():
            print(f"Target config '{target_config_file}' does not exist.")
            return False

        with open(target_config_file, "r") as file:
            self.target_config_yaml = yaml.full_load(file.read())

        return True

    def get_substitutions(self):
        return self.target_config_yaml['substitutions']

    substitutions = property(get_substitutions)

    def get_name(self):
        return self.target_config_yaml['name']

    name = property(get_name)

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

    def get_volumes(self):
        return self.config['volumes']

    volumes = property(get_volumes)
