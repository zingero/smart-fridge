import abc


class AbstractClient(abc.ABC):
	def __init__(self):
		self._login()

	@abc.abstractmethod
	def _login(self):
		pass

	@abc.abstractmethod
	def upload_file(self, file_path):
		pass

	def stop(self):
		pass
