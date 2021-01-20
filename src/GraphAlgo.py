import json
import math
import random
import sys
from typing import List
import queue
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.Node import Node
import numpy as np
import matplotlib.pyplot as plt



class GraphAlgo(GraphAlgoInterface):
    """This abstract class represents an interface of a graph."""

    def __init__(self, g=DiGraph()):
        self.graph = g


    def get_graph(self) -> GraphInterface:
        return self.graph


    def load_from_json(self, file_name: str) -> bool:
        try:
            with open (file_name,'r') as file:
               g= json.load(file)
               nodes = g["Nodes"]
               edges = g["Edges"]
               for n in nodes:
                   key =n["id"]
                   # self.graph.add_node(key)
                   if len(n) > 1:
                       p= n['pos'].split(",")
                       pos = (float(p[0]), float(p[1]))
                       self.graph.add_node(key,pos)
                   else:
                       self.graph.add_node(key)


               for e in edges:
                   self.graph.add_edge(e['src'], e['dest'], e['w'])
        except IOError as e:
            print(e)

    def save_to_json(self, file_name: str) -> bool:
        my_json={'Edges':[],'Nodes':[]}
        for key in self.graph.edges_out:
            for dest in self.graph.edges_out[key]:
                newdict={}
                newdict['src'] = key
                newdict['dest']= dest
                newdict['w']= self.graph.edges_out[key][dest]
                my_json['Edges'].append(newdict)
        for id in self.graph.nodes:
            newdict ={}
            if self.graph.nodes[id].pos !=None:
                newdict['pos']=','.join(str(x) for x in self.graph.nodes[id].pos)
            newdict['id']=self.graph.nodes[id].key
            my_json['Nodes'].append(newdict)
        try:
            with open (file_name,'w') as file:
                json.dump(my_json, default=lambda n: n.__dict__, indent= 4 ,fp= file)
        except IOError as e:
            print(e)

    # ','.join(str(x) for x in id)
    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if id1 in self.graph.nodes and id2 in self.graph.nodes:
            if id1 ==id2:
                return (0,[id1])
            self.DJ(id1)
            return self.the_shortest_path(id2)

    def connected_component(self, id1: int) -> list:
        if id1 not in self.graph.nodes:
            return None
        c1= self.DJ(id1)
        g= self.reverse_graph()
        Rgraph = GraphAlgo(g)
        c2=Rgraph.DJ(id1)
        connect =[]
        for n in c1:
            if n in c2:
                connect.append(n)
        return connect

    def connected_components(self) -> List[list]:
        connected=[]
        for n in self.graph.nodes:
            flag = False
            c=self.connected_component(n)
            c.sort()
            for n in connected:
                n.sort()
                if n==c:
                    flag=True
            if flag != True:
                connected.append(c)

        return connected


    def plot_graph(self) -> None:
        nodes = self.graph.get_all_v()
        lim = self.Limits()
        positions =dict()
        main_slant = np.math.dist([lim[0],lim[2]], [lim[1],lim[3]])

        for k, v in nodes.items():
            node_p = self.getPos(v , lim)
            plt.text(node_p[0], node_p[1], k, color='blue')
            plt.plot(node_p[0], node_p[1], 'o', color='green')
            positions[k] =node_p

        for src in nodes.keys():
            edges = self.graph.all_out_edges_of_node(src)
            x1 = positions[src][0]
            y1 = positions[src][1]
            for dest in edges.keys():
                x2 = positions[dest][0]
                y2 = positions[dest][1]
                slant_edge= np.math.dist([x1,y1],[x2,y2])
                plt.arrow(x1,y1,x2-x1,y2-y1, head_width =slant_edge/20, width=(slant_edge/main_slant)/10000, color="black",
                          length_includes_head=True)
        plt.show()



    def Limits(self):
        nodes = self.graph.nodes
        x = []
        y = []
        for key, value in nodes.items():
            if value.pos is not None:
                x.append(value.pos[0])
                y.append(value.pos[1])
        if len(x) == 0:
            x_max = 10
            x_min = 0
        else:
            x_max = max(x)
            x_min = min(x)
        if len(y) == 0:
            y_max = 10
            y_min = 0
        else:
            y_max = max(y)
            y_min = min(y)
        return x_min, x_max, y_min, y_max


    def getPos(self, v: Node, limit):
        if v.pos is not None:
            t_x = v.pos[0]
            t_y = v.pos[1]
        else:
            t_x = random.randint(limit[0], limit[1])
            t_y = random.randint(limit[2], limit[3])
        return t_x, t_y


    def DJ (self, src:int ):
        connected =[]
        connected.append(src)
        for i in self.graph.nodes:
            self.graph.nodes[i].weight = math.inf
            self.graph.nodes[i].info = "unvisited"
            self.graph.nodes[i].perent= None
        pryorty_q = queue.PriorityQueue()
        self.graph.nodes[src].weight = 0
        pryorty_q.put((self.graph.nodes[src].weight, src))
        while pryorty_q.empty() !=True:
            current = pryorty_q.get()[1]
            self.graph.nodes[current].info = "visited"
            if len (self.graph.all_out_edges_of_node(current)) > 0:
                for n in self.graph.all_out_edges_of_node(current).keys():
                    if n not in connected:
                        connected.append(n)
                    if self.graph.nodes[n].info != "visited":
                        d= self.graph.edges_in[n][current]+ self.graph.nodes[current].weight
                        if d < self.graph.nodes[n].weight:
                            self.graph.nodes[n].weight = d
                            pryorty_q._put((d,n))
                            self.graph.nodes[n].perent = current
        return connected

    def the_shortest_path (self, dest:int):
        short_list=[]
        if self.graph.nodes[dest].weight ==math.inf:
            return (self.graph.nodes[dest].weight, short_list)
        short_list.append(dest)
        current =self.graph.nodes[dest]
        while current.perent !=None:
            short_list.append(current.perent)
            current=self.graph.nodes[current.perent]
        short_list.reverse()
        return (self.graph.nodes[dest].weight , short_list)


    def reverse_graph (self):
        new_edges_out =self.graph.edges_in
        new_edges_in =self.graph.edges_out
        g= DiGraph()
        g.nodes = self.graph.nodes
        g.edges_out=new_edges_out
        g.edges_in=new_edges_in
        g.edges_size= self.graph.edges_size
        return g

    def __str__(self):
        return  "nodes are %s, edges are %s" % (self.graph.nodes,self.graph.edges_out)
