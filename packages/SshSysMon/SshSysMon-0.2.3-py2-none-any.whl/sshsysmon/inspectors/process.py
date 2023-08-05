from inspector import Inspector
from fnmatch import fnmatch

"""
Description:
	Find a process by name and inspect its metrics
Constructor:
	- name: The fnmatch'd name of the process
Metrics:
	None if no process was found
	- user:		User the process belongs to
	- pid: 		PID of the process
	- cpu		CPU use of the process
	- mem:		float memory use of the process
	- tty:		TTY of the process (if any)
"""
class Process(Inspector):
	def __init__(self, driver, name = ""):
		self._driver = driver
		self._process = name

	def getMetrics(self):
		data = self._driver.sh("ps -A u")['stdout']

		for line in data.splitlines():
			# User, pid, cpu, mem, vsz, rss, tty, stat, start, time, cmd
			parts = line.split()
			if fnmatch(parts[10], self._process):
				#Found it!
				return {
					"user" : parts[0],
					"pid" : parts[1],
					"cpu" : float(parts[2]),
					"mem" : float(parts[3]),
					"tty" : parts[6]
				}


		return None

	def getName(self):
		return "Process: %s" % self._process

def create(driver, args):
	return Process(driver, **args)