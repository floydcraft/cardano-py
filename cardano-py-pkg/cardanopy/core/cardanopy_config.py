import yaml
from pathlib import Path
import jsonschema
import json


class CardanoPyConfig(object):
    config = None
    config_resolved = None

    def substitute(self, config_str):
        substitutions = self.config.get('substitutions')
        if not substitutions or not config_str:
            return config_str

        for sub_key, sub_value in substitutions.items():
            # print(f"before\n{config_str}")
            config_str = config_str.replace(f"${sub_key}", f"{sub_value}")
            # print(f"after\n{config_str}")

        return config_str

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
                config_str = file.read()
                self.config = yaml.full_load(config_str)
                config_resolved_str = self.substitute(config_str)
                self.config_resolved = yaml.full_load(config_resolved_str)
        except Exception as ex:
            raise ValueError(f"Failed to load config. '{target_config_dir}'. {type(ex).__name__} {ex.args}")

        schema_file = Path(__file__).parent.joinpath("../data/schemas").absolute() / f"{self.apiVersion}.json"

        try:
            with open(schema_file, "r") as file:
                schema = json.loads(file.read())
        except Exception as ex:
            raise ValueError(f"Failed to load schema. '{target_config_dir}'. {type(ex).__name__} {ex.args}")

        try:
            jsonschema.validate(instance=self.config_resolved, schema=schema)
        except Exception as ex:
            raise ValueError(f"Failed to validate config. '{target_config_dir}'. {type(ex).__name__} {ex.args}")

    # def set(self, property_name: str, property_value):
    #     self.config[property_name] = property_value
    #     self.config_resolved[property_name] = copy.deepcopy(self.config[property_name])
    #
    # def get(self, property_name: str):
    #     return self.config_resolved[property_name]

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
        schema_file = Path(__file__).parent.joinpath("../data/schemas").absolute() / f"{self.apiVersion}.json"

        try:
            with open(schema_file, "r") as file:
                schema = json.loads(file.read())
        except Exception as ex:
            raise ValueError(f"Failed to load schema. '{target_config_dir}'. {type(ex).__name__} {ex.args}")

        try:
            jsonschema.validate(instance=self.config_resolved, schema=schema)
        except Exception as ex:
            raise ValueError(f"Failed to validate config. '{target_config_dir}'. {type(ex).__name__} {ex.args}")

        try:
            with open(target_config, "w") as file:
                yaml.dump(self.config, file)
        except Exception as ex:
            raise ValueError(f"Failed to save. '{target_config_dir}'. {type(ex).__name__} {ex.args}")

    def get_api_version(self):
        return self.config_resolved.get('apiVersion')

    apiVersion = property(get_api_version)

    def get_substitutions(self):
        return self.config_resolved.get('substitutions')

    substitutions = property(get_substitutions)

    def get_network(self):
        return self.config_resolved.get('network')

    network = property(get_network)

    def get_config_path(self):
        return self.config_resolved.get('configPath')

    configPath = property(get_config_path)

    def get_topology_path(self):
        return self.config_resolved.get('topologyPath')

    topologyPath = property(get_topology_path)

    def get_database_path(self):
        return self.config_resolved.get('databasePath')

    databasePath = property(get_database_path)

    def get_host_addr(self):
        return self.config_resolved.get('hostAddr')

    hostAddr = property(get_host_addr)

    def get_port(self):
        return self.config_resolved.get('port')

    port = property(get_port)

    def get_socket_path(self):
        return self.config_resolved.get('socketPath')

    socketPath = property(get_socket_path)

    def get_docker(self):
        return DockerConfig(self.config_resolved.get('docker'))

    docker = property(get_docker)

    def get_k8s(self):
        return KubernetesConfig(self.config_resolved.get('k8s'))

    k8s = property(get_k8s)


class DockerConfig(object):
    config = None

    def __init__(self, config):
        self.config = config

    def get_name(self):
        return self.config.get('name')

    name = property(get_name)

    def get_image(self):
        return self.config.get('image')

    image = property(get_image)

    def get_root_volume(self):
        return self.config.get('rootVolume')

    rootVolume = property(get_root_volume)


class KubernetesConfig(object):
    config = None

    def __init__(self, config):
        self.config = config

    def get_namespace(self):
        return self.config.get('namespace')

    namespace = property(get_namespace)