import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\configurations\\config.ini')

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = (config.get('commonInfo','baseUrl'))
        return url

    @staticmethod
    def getUserEmail():
        email = (config.get('commonInfo','email'))
        return email

    @staticmethod
    def getPassword():
        password = (config.get('commonInfo','password'))
        return password
