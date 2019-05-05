import os
import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")

class ReadConfig():
    def __init__(self):
        fd = open(configPath)
        data = fd.read()

        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_email(self, host):
        value = self.cf.get("EMAIL", host)
        return value

    def get_http(self, baseurl):
        value = self.cf.get("HTTP", baseurl)
        return value

    def get_db(self, testuser):
        value = self.cf.get("DATABASE", testuser)
        return value

a = ReadConfig()

print(a.get_email())
print(a.get_http())
print(a.get_db())