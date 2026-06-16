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
        
        
#function to carry out
def change ( ) :
#empty list to append color into
    colormap = []
    for node in g:
    #Neighbor nodes of a given node so up, down, left and right
        for neighbor in g.neighbors(node):
            if g.nodes[node]['color'] == REST:
                #let a node at rest turn into a sharer with probability 0.001
                g.nodes[node]['color'] = random.choices([SHARER, REST], [0.001, 0.999])[0]
            # If node is sharer with probability 0.01 and if neighbor is rest in
            # else if neighbor is bored change the node into bored
            if g.nodes[node][’color’] == SHARER and random.random() < 0.01:
                if g.nodes[neighbor][’color’]==REST:
                    g.nodes[neighbor][’color’] = SHARER
                elif g.nodes[neighbor][’color’]==BORED:
                    g.nodes[node][’color’]=BORED
            #If nodes is bored with probability 0.01 and if neighbor is rest
            #else nodes stay bored
            if g.nodes[node][’color’] == BORED and random.random() < 0.0005:
                if g.nodes[neighbor][’color’]==REST:
                    g.nodes[node][’color’]=REST
                else:
                    g.nodes[node][’color’]=BORED
        #append node color into the list ”colormap”
        colormap.append(g.nodes[node][’color’])
    return

# list to put counts of states into
count_rest = list(range(0, nu))
count_sharer = list(range(0, nu))
count_bored = list(range(0, nu))

def run_change_times(n):
    for j in range(n):
        #empty list of lists to append values of states into
        count_rest[j] = []
        count_sharer[j] = []
        count_bored[j] = []
        initial_state()
        #append the values into the list of lists ”count_rest[j]” , ”count_sharer[j]” , ”count_bored[j]”
        for i in range (1000):
            change()
            count_rest[j].append(count(g, REST))
            count_bored[j].append(count(g, BORED))
            count_sharer[j].append(count(g, SHARER))
    
run_change_times(nu)
#plot the results
fig, ax = plt.subplots()
step = list(range(0, 1000))
for i in range(nu):
    ax.plot(step, count_rest[i], "#73a832",
            step, count_bored[i], "#3263a8",
            step, count_sharer[i], "#a832a0")

ax.legend(['Resting', 'Bored', 'Sharer'])
ax.set(xlabel='Time SSteps', ylabel='Count of States', title='Spread Of Memes in a 2D Lattice Network')
plt.show()