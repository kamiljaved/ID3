
class Node(object): 

    # static class variables
    ATTRIBUTE = "Attriute"
    VALUE = "Value"
    LEAF = "Leaf"

    # Constructor 
    def __init__(self, label, nodetype, subs=[]):
        self.label = label
        self.type = nodetype
        self.subnodes = subs.copy()
        
    def getLabel(self):
        return self.label
    
    def getType(self):
        return self.type
        
    def getSubNodes(self):
        return self.subnodes

    def setLabel(self, label):
        self.label = label
    
    def setType(self, nodetype):
        self.type = nodetype
        
    def setSubNodes(self, subnodes):
        self.subnodes = subnodes

    def addSubNode(self, subnode):
        self.subnodes.insert(0, subnode)
        
    def isAttribute(self):
        return self.label == self.ATTRIBUTE
    
    def isValue(self):
        return self.label == self.VALUE

    def isLeaf(self):
        return self.label == self.LEAF

    def PrintTree(self):
        traversal = 0
        td = {}
        PTree(self, traversal, td)

def PTree(node, traversal, td):
    print(node.label +"\n", end = '')
    traversal += 1
    for i in range(len(node.subnodes)):
        td[traversal] = True
        for e in range(traversal-1):
            if td[e+1] == True:
                print(f"│   ", end = '')
            else:
                print(f"    ", end = '')
        if (i + 1) == len(node.subnodes):
            print("└───", end = '')
            td[traversal] = False
        else: 
            print("├───", end = '')
        PTree(node.subnodes[i], traversal, td)
    traversal -= 1



