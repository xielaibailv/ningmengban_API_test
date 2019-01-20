import configparser


class ReadConf:

    def __init__(self, conf_file):
        self.cf = configparser.ConfigParser()
        self.cf.read(conf_file, encoding='utf-8')

    def get_value(self, section, option):
        return self.cf.get(section, option)


if __name__ == '__main__':
    print(ReadConf('conf.ini').get_value('HEAD', 'headers'))
