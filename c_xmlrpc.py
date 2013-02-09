import xmlrpclib

ipHm = '192.168.x.x'
portHm = '2001'
# IP & port of homematic ccu
# portHM depends on access, BidCos-Wired = 2000, BidCos-RF = 2001, Internal = 2002

ipXmlRpcServer = '192.168.x.x'
portXmlRpcServer = '5544'

idHm = ''
# To register an xmlrpc server with Homematic set an ID 
# To unregister leave it blank

proxy = xmlrpclib.ServerProxy('http://'+ipHm+':'+portHm)
print proxy.init(ipXmlRpcServer+':'+portXmlRpcServer,idHm)
