import time
from .api import app
from .getter import Getter
from .tester import Tester
from multiprocessing import Process

TESTER_CYCLE = 20
GETTER_CYCLE = 20
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True


class Scheduler(object):
    def schedule_tester(self, cycle=TESTER_CYCLE):
        """
        定时测试代理
        :param cycle:
        :return:
        """
        tester = Tester()
        while True:
            print('测试器开始运行...')
            tester.run()
            time.sleep(cycle)

    def schedule_getter(self, cycle=GETTER_CYCLE):
        """
        定时抓取代理
        :param cycle:
        :return:
        """
        getter = Getter()
        while True:
            print('开始抓取代理...')
            getter.run()
            time.sleep(cycle)

    def schedule_api(self):
        """
        开启api
        :return:
        """
        app.run()

    def run(self):
        """
        run
        :return:
        """
        print('代理池开始运行....')
        if TESTER_ENABLED:
            tester_process = Process(target=self.schedule_tester())
            tester_process.start()

        if GETTER_ENABLED:
            tester_process = Process(target=self.schedule_getter())
            tester_process.start()

        if API_ENABLED:
            tester_process = Process(target=self.schedule_api())
            tester_process.start()
