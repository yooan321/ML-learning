import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
# Idk the name it should have ...
class MyClass(object):
    def init(self, dimension =15, nu=20):
        ”””
        − dimension : dimension of the 2d lattice network .
        − nu : number of times to run the model .
        ”””
        self.dimension = dimension
        self.nu = nu
        self.REST = 'green'
        self.SHARER = 'pink'
        self.BORED = 'blue'
        self.g = None
        self.color_map = []
        #function to count the number of a certain color appearing
        def count(self, network, variable):
            number=0
            for i in range(int(sqrt(len(network)))):
                for j in range(int(sqrt(len(network)))):
                    if network.nodes[i ,j]['color']== variable:
                        number +=1
            return number
        #2d square lattice with periodic boundary conditions
        def initial state(self):
            #global g
            #global color map
            self.g = nx.grid2dgraph(self.dimension, self.dimension, periodic=True)
            #set color for all nodes as REST (green)
            for node in self.g:
                self.g.nodes[node]['color' ]= self .REST
            #nodes with chosen colors
            self.g.nodes[0, 0]['color']= self.SHARER
            self.g.nodes[2, 2]['color']= self.BORED
            #color_map = []
            #append color into a list
            for node in self.g:
                self.color_map.append(self.g.nodes[node]['color'])
        #function to carry out
        def change(self):
            #empty list to append color into
            self.color_map = []
            for node in self.g:
                #Neighbor nodes of a given node so up, down, left and right
                for neighbor in self.g.neighbors(node):
                    if self.g.nodes[node]['color'] == self.REST:
                        #let a node at rest turn into a sharer with probability 0.001
                        self.g.nodes[node]['color']=random.choices([self.SHARER, self.REST], weights=[0.001, 0.999])[0]
                    # If node is sharer with probability 0.01 and if neighbor is
                    # rest changing neighbor into sharer
                    # else if neighbor is self.BORED change the node into self.BORED
                    if self.g.nodes[node]['color'] == self.SHARER and random.random() < 0.01:
                        if self.g.nodes[neighbor]['color'] == self.REST:
                            self.g.nodes[neighbor]['color'] = self.SHARER
                        elif self.g.nodes[node]['color'] == self.BORED and random.random() < 0.01:
                            self.g.nodes[node]['color']= self.BORED
                    # If nodes is bored with probability 0.01 and if neighbor is
                    # rest changing node into rest
                    # else node stays bored
                    if self.g.nodes[node][’color’] == self.BORED and random.random()<0.01:
                        if self.g.nodes[neighbor]['color']==self.REST:
                            self.g.nodes[node]['color']=self.REST
                        else:
                            self.g.nodes[node]['color']=self.BORED
                #append node color into the list "color_map"           
                self.color_map.append(self.g.nodes[node]['color'])
            # ?? 
            return
    def run_change_n_times(self, n):
        #list to put counts of states into
        count_rest =list(range(0,self.nu))
        count_share =list(range(0,self.nu))
        count_bored=list(range(0,self.nu))

        for j in range(n):
            #empty list of lists to append values of states into     
            count_rest[j]=[]
            count_share[j]=[]
            count_bored[j]=[]
            self.initial_state()
            # append the values into the list of lists "count_rest[j]", 
            # "count_share[j]" and "count_bored[j]"
            for i in range(1000):
                self.change()
                count_rest[j].append(self.count(self.g,self.REST))
                count_bored[j].append(self.count(self.g,self.BORED))
                count_share[j].append(self.count(self.g,self.SHARER))

        return count_rest, count_bored, count_share


if __name__ == '__main__':
    
    # with base parameters
    a = MyClass()
    count_rest, count_bored, count_share = a.run_change_n_times(20)
    
    # b = MyClass(dimension=15, nu=30)
    # count_rest, count_bored, count_share = b.run_change_n_times(30)

    #plot the results 
    fig, ax = plt.subplots()
    step = list(range(0,1000))
    for i in range(20):
         ax.plot(step,count_rest[i],"#73a832",
                 step,count_bored[i],"#3263a8",
                 step,count_share[i],"#a832a0")

    ax.legend(['Resting', 'Bored', 'Sharer'])
    ax.set(xlabel='Time Steps',ylabel='Count of States',
           title='Spread Of Memes in a 2d square lattice Network')
    plt.show()