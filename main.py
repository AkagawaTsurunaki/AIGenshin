import kleecker as kl
import yaml

config_path = "./config"

def init_kleecker():

    kleeker_config_path = config_path + "/config.yaml"

    # 读取连点器的配置文件
    with open(kleeker_config_path, 'r', encoding='utf-8') as kleecker_config_file:

        config = yaml.load(kleecker_config_file.read(), Loader=yaml.FullLoader)
        config = config['kleecker']

    kl.start(config['is-instruction-output'], config['is-log-output'])

init_kleecker()