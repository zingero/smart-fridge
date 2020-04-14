import logging
import threading
import signal

from smartfridge import SmartFridge


class Main:
	def __init__(self):
		signal.signal(signal.SIGTERM, self.__stop)
		signal.signal(signal.SIGINT, self.__stop)
		self.__event = threading.Event()
		self.__initLogging()
		self.__smart_fridge = SmartFridge(self.__event.is_set)

	def run(self):
		self.__smart_fridge.start()
		self.__smart_fridge.stop()
		logging.info("Process terminated")

	def __initLogging(self):
		logging.basicConfig(format = '%(asctime)s %(levelname)s %(message)s', level = logging.INFO)
		logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)

	def __stop(self, signalNumber, frame):
		signal.signal(signalNumber, signal.SIG_IGN)
		self.__event.set()


if __name__ == "__main__":
	Main().run()
