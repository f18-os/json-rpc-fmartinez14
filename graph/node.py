import json
class node:
    def __init__(self, name, children = []):
        self.name = name
        self.children = children
        self.val = 0
    def show(self, level):
        print (str(level) + " ", self.name + " ", str(self.val) + " ")
        for c in self.children:
            c.show(level + 1)



def increment(graph): #Adds 1 to the value of every node in the tree.
    graph.val += 1;
    for c in graph.children:
        increment(c)

def jsonEncode(currentNode): #Encodes the tree into a JSON string.
    currNodeChildren = []
    if(currentNode != ""):
        for c in currentNode.children:
            currNodeChildren.append(jsonEncode(c))
        currentNode.children = currNodeChildren
        return json.dumps(currentNode.__dict__)

def jsonDecrypt(currentNode):
    currNodeChildren = []
    if(currentNode != ""):
        tempNode = json.loads(currentNode)
        returnNode = node(list(tempNode.values())[0] , list(tempNode.values())[1])
        for c in returnNode.children:
            currNodeChildren.append(jsonDecrypt(c))
        returnNode.children = currNodeChildren
        return returnNode
