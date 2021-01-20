class Node:

    def __init__(self,key,pos):
       self.key =key
       self.weight=0
       self.info=""
       self.pos=pos
       self.perent=None
       self.edges_in = dict()
       self.edges_out = dict()

    def encoder (self,node):
        return node.__dict__

    # {0: 0: |edges out| 1 |edges in| 1, 1: 1: |edges out| 3 |edges in| 1, 2: 2: |edges out| 1 |edges in| 1, 3: 3: |edges out| 0 |edges in| 2}

    def __repr__(self):
        return "%s: |edges out|=%s , |edges in|=%s" % (self.key,len(self.edges_out), len(self.edges_in))