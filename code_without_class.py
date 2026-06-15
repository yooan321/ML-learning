import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

REST = 'green'
SHARER = 'pink'
BORED = 'blue'

#dimension of the 2d lattice network
dimension = 15

#number of times to run the model
nu=20

#function to count the number of a certain color appearing
def count (network , variable ) :
    number=0
    for i in range(sqrt(len(network))) :
        for j in range(sqrt(len(network))) :
            if network.nodes[i, j]['color']== variable :
                number +=1
    return number

#2d square lattice with periodic boundary conditions
def initial_state() :
    global g
    global color_map
    g=nx.grid_2d_graph(dimension, dimension, periodic=True)
    #sets color for all nodes as REST (green)
    for node in g :
        g.nodes[node]['color']=REST
    #nodes with chosen colors
    g.nodes[0, 0]['color']=SHARER
    g.nodes[2, 2]['color']=BORED
    color_map = [ ]
    #append color to a list
    for node in g :
        color_map.append(g.nodes[node]['color'])