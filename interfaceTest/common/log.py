import os
import logging
from datetime import datetime
import threading

class Log:
    def __init__(self):
        global logPath, resultPath, proDir
        proDir = readConfig.proDir
        resultPath = os.path.join(proDir, "result")
        # create result file if it doesn't exist 如果结果文件不存在，则创建它
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        # defined test result file name by localtime 按localtime定义测试结果文件名
        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        # create test result file if it doesn't exist 如果测试结果文件不存在，则创建测试结果文件
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        # defined logger 定义日志记录器
        self.logger = logging.getLogger()
        # defined log level 定义日志级别
        self.logger.setLevel(logging.INFO)

        # defined handler 定义处理程序
        handler = logging.FileHandler(os.path.join(logPath, "output.log"))
        # defined formatter 定义的格式化程序
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # defined formatter 定义的格式化程序
        handler.setFormatter(formatter)
        # add handler 添加处理程序
        self.logger.addHandler(handler)
