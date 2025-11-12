"""
2024
© Bahda
"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from waitress import serve
import yaml
import boto3
import botocore

from flask_project.app.my_project import create_app

DEVELOPMENT_PORT = 5000
PRODUCTION_PORT = 5000
HOST = "0.0.0.0"
DEVELOPMENT = "development"
PRODUCTION = "production"
FLASK_ENV = "FLASK_ENV"
ADDITIONAL_CONFIG = "ADDITIONAL_CONFIG"


def get_parameter_from_ssm(parameter_name):
    ssm = boto3.client('ssm', region_name="eu-north-1")
    try:
        param = ssm.get_parameter(Name=parameter_name, WithDecryption=True)
        return param["Parameter"]["Value"]
    except botocore.exceptions.ClientError as e:
        print(f"Error fetching parameter {parameter_name} from SSM: {e}")
        return None

if __name__ == '__main__':
    flask_env = os.environ.get(FLASK_ENV, DEVELOPMENT).lower()
    config_yaml_path = os.path.join(os.getcwd(), 'config', 'app.yml')

    with open(config_yaml_path, "r", encoding='utf-8') as yaml_file:
        config_data_dict = yaml.load(yaml_file, Loader=yaml.FullLoader)
        additional_config = config_data_dict[ADDITIONAL_CONFIG]

        env_config = config_data_dict.get(flask_env)

        env_config["SQLALCHEMY_DATABASE_URI"] = get_parameter_from_ssm("database-link")
        additional_config["MYSQL_ROOT_USER"] = get_parameter_from_ssm("database-user")
        additional_config["MYSQL_ROOT_PASSWORD"] = get_parameter_from_ssm("database-password")

        if flask_env == DEVELOPMENT:
            config_data = config_data_dict[DEVELOPMENT]
            print(f"Are you ready, kids?\n"
                    f"Aye, aye, Captain\n"
                    f"I can't hear you\n"
                    f"Aye, aye, Captain\n"
                    f"Oh"
                    f"☠️☠️☠️"
                    f"🧽🧽🧽")
            create_app(config_data, additional_config).run(host="0.0.0.0", port=5000, debug=True)

        elif flask_env == PRODUCTION:
            config_data = config_data_dict[PRODUCTION]
            serve(create_app(config_data, additional_config), host=HOST, port=PRODUCTION_PORT)

        else:
            raise ValueError(f"Check OS environment variable '{FLASK_ENV}'")
