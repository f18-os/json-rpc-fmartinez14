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
  JSONDecryptedTree = ""
  treeToUse={}


  @request
  def obtainJSON(self,EncodeMe):
    global JSONDecryptedTree #Loads a tree and moves it to json decrypted tree.
    JSONDecryptedTree = json.loads(EncodeMe)


  @request
  def obtainDict(self,DictRoot): #Creates all necessary steps for dict.
     global treeToUse
     global JSONDecryptedTree
     treeToUse = json.loads(DictRoot)
     for x,y in treeToUse.items(): #Iterates across tree objects and adds it to a variable.
         temp = json.loads(y)
         treeToUse[x] = node(temp[list(temp.keys())[0]], temp[list(temp.keys())[1]])
     JSONDecryptedTree = parseTree(treeToUse, JSONDecryptedTree)
     JSONDecryptedTree.show(0)

  @request
  def incrementValues(self): #Increments value for the tree.
      global JSONDecryptedTree
      print ("incrementing ")
      increment(JSONDecryptedTree)
      print ("After incrementing:")
      print(JSONDecryptedTree)
      JSONDecryptedTree.show(0)

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
