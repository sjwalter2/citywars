import json

class Block:
	def __init__(self, x, y):
		self.__x = x
		self.__y = y

	def toJSON(self):
		return {
			'x': self.__x,
			'y': self.__y
		}

class Map:

	def __init__(self, height, width=0):
		self.__height = height
		if width == 0:
			self.__width = height
		else:
			self.__width = width
		self.__blocks = []
		for x in range(self.__height):
			self.__blocks.append([])
			for y in range(self.__width):
				self.__blocks[x].append(Block(x, y))

	def toJSONBlocks(self):
		jsonBlocks = []
		for x in range(self.__height):
			jsonBlocks.append([])
			for y in range(self.__width):
				jsonBlocks[x].append(self.__blocks[x][y].toJSON())
		return jsonBlocks

	def toJSON(self):
		return {
			'height': self.__height,
			'width': self.__width,
			'blocks': self.toJSONBlocks()
		}
