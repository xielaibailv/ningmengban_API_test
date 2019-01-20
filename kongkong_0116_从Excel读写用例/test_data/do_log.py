import logging
from kongkong_0116_从Excel读写用例.conf_file.read_conf import ReadConf

# 获取配置文件里的日志相关参数
conf_file = '../conf_file/conf.ini'
name = ReadConf(conf_file).get_value('LOG', 'name')
in_level = ReadConf(conf_file).get_value('LOG', 'in_level')
out_level = ReadConf(conf_file).get_value('LOG', 'out_level')
out_file_level = ReadConf(conf_file).get_value('LOG', 'out_file_level')
file_path = ReadConf(conf_file).get_value('LOG', 'file_path')
log_format = ReadConf(conf_file).get_value('LOG', 'log_format')


class DoLog:

    @staticmethod
    def mylog(level, msg):
        # 创建一个日志收集器
        my_logger = logging.getLogger(name)
        # 给日志收集器指定收集的级别
        my_logger.setLevel(in_level)
        # 设置输出格式
        formatter = logging.Formatter(log_format)
        # 输出渠道
        fh = logging.FileHandler(file_path, mode='a', encoding='utf-8')
        # 输出级别
        fh.setLevel(out_file_level)
        # 设置日志输出的格式
        fh.setFormatter(formatter)
        # 对接
        my_logger.addHandler(fh)

        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        else:
            my_logger.critical(msg)

        # 移除日志收集器
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.mylog('DEBUG', msg)

    def info(self, msg):
        self.mylog('INFO', msg)

    def warning(self, msg):
        self.mylog('WARNING', msg)

    def error(self, msg):
        self.mylog('ERROR', msg)

    def critical(self, msg):
        self.mylog('CRITICAL', msg)


if __name__ == '__main__':
    my_logger = DoLog()
    my_logger.debug('debug级别的日志')

