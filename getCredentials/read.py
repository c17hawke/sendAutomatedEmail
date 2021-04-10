import configparser
import os

CURREN_FOLDER = "getCredentials"
CONFIG_FILE = "config.ini"
CONFIG_FILE_PATH = os.path.join(CURREN_FOLDER, CONFIG_FILE)

class ConfigReader:
    def __init__(self):
        self.configFileName = CONFIG_FILE_PATH

    def read_config(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.configFileName)
        self.configuration = self.config["DEFAULT"]
        self.eMAILsender = self.configuration["eMAILsender"]
        self.ePASSKEY = self.configuration["ePASSKEY"]
        return self.configuration



