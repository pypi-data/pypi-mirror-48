
class Driver:
	def __init__(self):
		pass

	def readProc(self, path):
		raise NotImplementedError()

	def sh(self, cmd):
		raise NotImplementedError()

	def getHost(self):
		raise NotImplementedError()