import abc


class AbstractClient(abc.ABC):
	def __init__(self):
		self._login()

	@abc.abstractmethod
	def _login(self):
		pass

	@abc.abstractmethod
	def uploadFile(self, filePath):
		pass

	def stop(self):
		pass
