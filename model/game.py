import json
from model.map import Map

class GameSetup:
	def __init__(self, height, width, gangs, enableForce = False, enableHeroes = False):
		self.height = height
		self.width = width
		self.gangs = gangs
		self.enableForce = enableForce
		self.enableHeroes = enableHeroes

	def toJSON(self):
		return {
			'height': self.height,
			'width': self.width,
			'gangs': self.gangs,
			'enableForce': self.enableForce,
			'enableHeroes': self.enableHeroes
		}

class GameException (Exception):
	pass

class STATUS:
	STARTED = 'Started'
	PAUSED = 'Paused'
	STOPPED = 'Stopped'

class Game:

	def __init__(self, setup):
		self.__setup = setup
		self.__status = STATUS.STOPPED
		self.__map = Map(setup.height, setup.width)
		self.__logs = []

	def start(self):
		if self.__status == STATUS.STOPPED:
			self.__status = STATUS.STARTED
			return self.__status
		else:
			raise GameException('Unable to start a PAUSED or STARTED game')

	def stop(self):
		if self.__status != STATUS.STOPPED:
			self.__status = STATUS.STOPPED
			return self.__status
		else:
			raise GameException('Unable to stop a STOPPED game')

	def pause(self):
		if self.__status == STATUS.STARTED:
			self.__status = STATUS.PAUSED
			return self.__status
		else:
			raise GameException('Unable to pause a non-STARTED game')

	def resume(self):
		if self.__status == STATUS.PAUSED:
			self.__status = STATUS.STARTED
			return self.__status
		else:
			raise GameException('Unable to resume a non-PAUSED game')

	def getStatus(self):
		return self.__status

	def getMap(self):
		return self.__map

	def toJSON(self):
		return {
			'status': self.__status,
			'setup': self.__setup.toJSON()
		}

	def getLogs(self):
		return map(json.dump, self.__logs)

class Log:
	def __init__(self, message, gang = None, position = None):
		self.message = message
		self.gang = gang
		self.position = position