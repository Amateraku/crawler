import yaml


class Config:
    def __init__(self):
        config_file = open("config.yaml")
        config = yaml.safe_load(config_file)

        self.CRAWLER_INTERVAL = config["crawler"]["interval"]
        self.CRAWLER_TOKEN = config["crawler"]["token"]
        self.CRAWLER_CITY = config["crawler"]["city"]
        self.CRAWLER_SAVE_FILE_NAME = config["crawler"]["save_file_name"]
