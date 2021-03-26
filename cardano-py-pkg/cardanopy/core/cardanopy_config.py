import yaml
from pathlib import Path
import jsonschema
import json


class CardanoPyConfig(object):
    config = None
    config_resolved = None

    @staticmethod
    def try_get_valid_config_dir(target_config_dir_or_file):
        if isinstance(target_config_dir_or_file, str):
            target_config_dir_or_file = Path(target_config_dir_or_file)

        if target_config_dir_or_file.is_dir():
            target_config = target_config_dir_or_file.joinpath("cardanopy.yaml")
            target_config_dir = target_config_dir_or_file
        else:
            target_config = target_config_dir_or_file
            target_config_dir = target_config_dir_or_file.parent

        if not target_config.is_file():
            raise ValueError(f"Target config '{target_config}' is not a file. e.g., 'cardanopy.yaml'")

        if not target_config.exists():
            raise ValueError(f"Target file '{target_config}' does not exist.")

        return target_config_dir

    @staticmethod
    def try_get_valid_config_file(target_config_dir_or_file):
        if isinstance(target_config_dir_or_file, str):
            target_config_dir_or_file = Path(target_config_dir_or_file)

        if target_config_dir_or_file.is_dir():
            target_config = target_config_dir_or_file.joinpath("cardanopy.yaml")
        else:
            target_config = target_config_dir_or_file

        if not target_config.is_file():
            raise ValueError(f"Target config '{target_config}' is not a file. e.g., 'cardanopy.yaml'")

        if not target_config.exists():
            raise ValueError(f"Target file '{target_config}' does not exist.")

        return target_config

    def substitute(self, config_str, subs: tuple):
        substitutions = self.config.get('substitutions')
        if not substitutions or not config_str:
            return config_str

        for sub in subs:
            if "=" in sub:
                sub_split = sub.split("=")
                sub_key = sub_split[0] if len(sub_split) > 0 else None
                sub_value = sub_split[1] if len(sub_split) > 1 else None
                sub_key = sub_key.strip()
                sub_value = sub_value.strip()
                if sub_value and (sub_value.endswith('\'') or sub_value.endswith('\"')):
                    sub_value = sub_value[:-1]
                if sub_value and (sub_value.startswith('\'') or sub_value.startswith('\"')):
                    sub_value = sub_value[1:]

                if sub_key and not sub_key.startswith('_'):
                    raise ValueError(f"Substitutions invalid format: prefix of underscore is required.\n"
                                     f"sub_key='{sub_key}' and  sub_value='{sub_value}'\n"
                                     f"Should be: --sub _KEY_EXAMPLE='value_example'.")

                if sub_key:
                    config_str = config_str.replace(f"${sub_key}", f"{sub_value}")
                else:
                    raise ValueError(f"Substitutions invalid format: key shouldn't be None/null or Empty\n"
                                     f"sub_key='{sub_key}' and  sub_value='{sub_value}'\n"
                                     f"Should be: --sub _KEY_EXAMPLE='value_example'")
            else:
                raise ValueError(f"Substitutions invalid format: key=value should be seperated with an equal sign\n"
                                 f"sub='{sub}'\n"
                                 f"Should be: --sub _KEY_EXAMPLE='value_example'")

        for sub_key, sub_value in substitutions.items():
            # print(f"before\n{config_str}")
            config_str = config_str.replace(f"${sub_key}", f"{sub_value}")
            # print(f"after\n{config_str}")

        return config_str

    def load(self, target_config_file, subs: tuple = tuple()):
        if isinstance(target_config_file, str):
            target_config_file = Path(target_config_file)

        if not target_config_file.is_file():
            raise ValueError(f"Target config '{target_config_file}' is not a file. e.g., 'cardanopy.yaml'")

        if not target_config_file.exists():
            raise ValueError(f"Target file '{target_config_file}' does not exist.")

        try:
            with open(target_config_file, "r") as file:
                config_str = file.read()
                self.config = yaml.full_load(config_str)
                config_resolved_str = self.substitute(config_str, subs)
                self.config_resolved = yaml.full_load(config_resolved_str)
        except Exception as ex:
            raise ValueError(f"Failed to load config. '{target_config_file}'. {type(ex).__name__} {ex.args}")

        schema_file = Path(__file__).parent.joinpath("../data/schemas").absolute() / f"{self.apiVersion}.json"

        try:
            with open(schema_file, "r") as file:
                schema = json.loads(file.read())
        except Exception as ex:
            raise ValueError(f"Failed to load schema. '{target_config_file}'. {type(ex).__name__} {ex.args}")

        try:
            jsonschema.validate(instance=self.config_resolved, schema=schema)
        except Exception as ex:
            raise ValueError(f"Failed to validate config. '{target_config_file}'. {type(ex).__name__} {ex.args}")

    # def set(self, property_name: str, property_value):
    #     self.config[property_name] = property_value
    #     self.config_resolved[property_name] = copy.deepcopy(self.config[property_name])
    #
    # def get(self, property_name: str):
    #     return self.config_resolved[property_name]

    def save(self, target_config_file):
        if isinstance(target_config_file, str):
            target_config_file = Path(target_config_file)

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
            raise ValueError(f"Failed to load schema. '{target_config_file}'. {type(ex).__name__} {ex.args}")

        try:
            jsonschema.validate(instance=self.config_resolved, schema=schema)
        except Exception as ex:
            raise ValueError(f"Failed to validate config. '{target_config_file}'. {type(ex).__name__} {ex.args}")

        try:
            with open(target_config_file, "w") as file:
                yaml.dump(self.config, file)
        except Exception as ex:
            raise ValueError(f"Failed to save. '{target_config_file}'. {type(ex).__name__} {ex.args}")

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

    def get_shelley_kes_key(self):
        return self.config_resolved.get('shelleyKesKey')

    shelleyKesKey = property(get_shelley_kes_key)

    def get_shelley_vrf_key(self):
        return self.config_resolved.get('shelleyVrfKey')

    shelleyVrfKey = property(get_shelley_vrf_key)

    def get_shelley_operational_certificate(self):
        return self.config_resolved.get('shelleyOperationalCertificate')

    shelleyOperationalCertificate = property(get_shelley_operational_certificate)

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

    def get_mount(self):
        return self.config.get('mount', False)

    mount = property(get_mount)


class KubernetesConfig(object):
    config = None

    def __init__(self, config):
        self.config = config

    def get_namespace(self):
        return self.config.get('namespace')

    namespace = property(get_namespace)