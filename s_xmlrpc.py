from SimpleXMLRPCServer import SimpleXMLRPCServer

port = 5544

srv = SimpleXMLRPCServer(('0.0.0.0',port))

class MyFuncs:

	def event(*args):
		for arg in args:
			print arg
		return ''

	def listDevices(*args):
		for arg in args:
			print arg
		return ''

	def newDevices(*args):
		for arg in args:
			print arg
		return ''

	def newDevice(*args):
		for arg in args:
			print arg
		return ''

srv.register_instance(MyFuncs())
srv.register_multicall_functions()

try:
    print 'Use Control-C to exit'
    print srv.serve_forever()
except KeyboardInterrupt:
    print 'Exiting'


