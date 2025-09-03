import configparser
config=configparser.RawConfigParser()   #Creating object for configparser
config.read(".\\Configurations\\Config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url=config.get("common info","baseUrl")
        return url

    @staticmethod
    def getUseremail():
        username = config.get("common info", "useremail")
        return username

    @staticmethod
    def getPassword():
        password = config.get("common info", "password")
        return password