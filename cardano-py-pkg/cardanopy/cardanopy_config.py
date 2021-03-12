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

        # if not target_config.is_file():
        #     raise ValueError(f"Target config '{target_config}' is not a file. e.g., 'cardanopy.yaml'")
        #
        # if not target_config.exists():
        #     raise ValueError(f"Target file '{target_config}' does not exist.")

        try:
            with open(target_config, "w") as file:
                yaml.dump(self.target_config_yaml, file)
        except Exception as ex:
            raise ValueError(f"Failed to create. Unable to copy config to '{target_config_dir}'. {type(ex).__name__} {ex.args}")

    def get_api_version(self):
        return self.target_config_yaml['apiVersion']

    apiVersion = property(get_api_version)

    def get_substitutions(self):
        return self.target_config_yaml['substitutions']

    substitutions = property(get_substitutions)

    def get_network(self):
        return self.target_config_yaml['network']

    network = property(get_network)

    def get_config_path(self):
        return self.target_config_yaml['configPath']

    configPath = property(get_config_path)

    def get_topology_path(self):
        return self.target_config_yaml['topologyPath']

    topologyPath = property(get_topology_path)

    def get_topology(self):
        return self.target_config_yaml['topology']

    topology = property(get_topology)

    def get_database_path(self):
        return self.target_config_yaml['databasePath']

    databasePath = property(get_database_path)

    def get_host_addr(self):
        return self.target_config_yaml['hostAddr']

    hostAddr = property(get_host_addr)

    def get_port(self):
        return self.target_config_yaml['port']

    port = property(get_port)

    def get_socket_path(self):
        return self.target_config_yaml['socketPath']

    socketPath = property(get_socket_path)

    def get_docker(self):
        return DockerConfig(self.target_config_yaml['docker'])

    docker = property(get_docker)

    def get_kubernetes(self):
        return KubernetesConfig(self.target_config_yaml['kubernetes'])

    kubernetes = property(get_kubernetes)


class DockerConfig(object):
    config = None

    def __init__(self, config):
        self.config = config

    def get_name(self):
        return self.config['name']

    name = property(get_name)

    def get_image(self):
        return self.config['image']

    image = property(get_image)

    def get_root_volume(self):
        return self.config['rootVolume']

    rootVolume = property(get_root_volume)


class KubernetesConfig(object):
    config = None

    def __init__(self, config):
        self.config = config

    def get_namespace(self):
        return self.config['namespace']

    namespace = property(get_namespace)