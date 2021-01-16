class Node:

    def __init__(self,key):
       self.key =key
       self.weight=0
       self.info=""
       self.location=None
       self.perent=None
    def encoder (self,node):
        return node.__dict__