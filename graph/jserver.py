# minimalistic server example from
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket
import json
from node import *
from bsonrpc import JSONRpc
from bsonrpc import request, service_class
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)


# Class providing functions for the client to use:
@service_class
class ServerServices(object):
  decryptedTree = ""
  @request
  def swapper(self, txt):
    return ''.join(reversed(list(txt)))

  @request
  def obtainJSON(self,txt):
    global decryptedTree
    decryptedTree = jsonDecrypt(txt)
    decryptedTree.show(0)
    # return decryptedTree

  @request
  def incrementMe(self):
      global decryptedTree
      print ("incrementing ")
      increment(decryptedTree)
      print ("After incrementing:")
      decryptedTree.show(0)

  @request
  def nop(self, txt):
    print(txt)
    return txt

# Quick-and-dirty TCP Server:
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('localhost', 50001))
ss.listen(10)

while True:
  s, _ = ss.accept()
  # JSONRpc object spawns internal thread to serve the connection.
  JSONRpc(s, ServerServices(),framing_cls=JSONFramingNone)
