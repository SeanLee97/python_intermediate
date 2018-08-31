# -*- coding: utf-8 -*-

class Container(object):
	def __init__(self):
		self.name = None
		self.age = None

	def __setattr__(self, key, val):
		self.__dict__[key] = val

	def __getattr__(self, key):
		return "key %s not found" % key

	def __contains__(self, key):
		return key in self.__dict__

if __name__ == '__main__':
	c = Container()
	print(c.attr)
	print('attr' in c)  # call __contains__
	print('name' in c)  # call __contains__
	c.attr = 'attr'     # call __setattr__
	print(c.attr)
	print('attr' in c)