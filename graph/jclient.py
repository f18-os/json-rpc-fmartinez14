# minimalistic client example from
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket
import json
from bsonrpc import JSONRpc
from node import *
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)

# Cut-the-corners TCP Client:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50001))

rpc = JSONRpc(s,framing_cls=JSONFramingNone)
server = rpc.get_peer_proxy()

def forwardTree():
    currentTree = jsonEncode(root) #Generates JSON string and sends it to server.
    currentTree = json.dumps(currentTree)
    server.obtainJSON(currentTree)





leaf1 = node("firstLeaf")
leaf2 = node("secondLeaf") #Creates tree.
root = node("root", [leaf1, leaf2])

print ("Forwarding tree to server.")
forwardTree()

ReferenceDict = createDict(root) #Send commands to server
ReferenceDict = json.dumps(ReferenceDict)

print("Sending references")

server.obtainDict(ReferenceDict)

print ("Incrementing tree.")

server.incrementValues()


print(server.nop({1:[2,3]}))

rpc.close() # Closes the socket 's' also
