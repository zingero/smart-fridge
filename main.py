import logging
import threading
import signal

from smartfridge import SmartFridge


class Main:
	def __init__(self):
		signal.signal(signal.SIGTERM, self.__stop)
		signal.signal(signal.SIGINT, self.__stop)
		self.__event = threading.Event()
		self.__init_logging()
		self.__smart_fridge = SmartFridge(self.__event.is_set)

	def run(self):
		self.__smart_fridge.start()
		self.__smart_fridge.stop()
		logging.info("Process terminated")

	def __init_logging(self):
		logging.basicConfig(format = '%(asctime)s %(levelname)s %(message)s', level = logging.INFO)
		logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)

	def __stop(self, signal_number, _):
		signal.signal(signal_number, signal.SIG_IGN)
		self.__event.set()


if __name__ == "__main__":
	Main().run()
