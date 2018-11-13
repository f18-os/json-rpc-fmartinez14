import json,ast
class node:
    def __init__(self, name, children = []):
        self.name = name
        self.children = children
        self.val = 0
    def show(self, level):
        print (str(level) + " ", self.name + " ", str(self.val) + " ")
        for c in self.children:
            c.show(level + 1)



def increment(graph): #Increases value of nodes.
    graph.val += 1;
    for c in graph.children:
        increment(c)


def jsonEncode(currentNode): #Converts tree to a json list.
    listChildren = []
    myNode = {}
    if(currentNode != ""):
        for c in currentNode.children: #Get children as lists instead of objects for encoding.
            listChildren.append(jsonEncode(c))
        currentNode.children = listChildren
        myNode[id(currentNode)] =  json.dumps(currentNode.__dict__)
        return myNode

def parseTree(treeStruct , currentNode):
    listChildren = [] #Parses subtree and appends it to the new tree.
    currentNode= treeStruct[list(currentNode.keys())[0]]
    print(str(id(currentNode)) + " " + currentNode.name)
    if(currentNode != ""):
        for c in currentNode.children:
            listChildren.append(parseTree(treeStruct, c))
        currentNode.children = listChildren
        return currentNode

def createDict(currentNode):
    dictStruc = {} #This method creates a dictionary that contains references and nodes.
    dictStruc[id(currentNode)] = json.dumps(currentNode.__dict__)
    for y in currentNode.children:
        coolNode = list(y.keys())[0]
        coolNodeChildren = list(y.values())[0]
        dictStruc[coolNode] = coolNodeChildren
    return dictStruc
