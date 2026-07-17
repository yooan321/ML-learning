import numpy as np
import networkx as nx
import matplotlib
import json
import random
from networkx.readwrite import json_graph

# function to read a JSON file from the internet
def read_json_file(filename):
    with open(filename) as f:
        js_graph = json.load(f)
    return json_graph.node_link_graph(js_graph)
    
#read the JSON file you need
a=read_json_file('starwars-full-interactions.json')


#open and read the Document file
a=open('mammalia-dolphin-florida-overall.edges')
a=a.read()
#split the str where \n appears into a list
p=a.split('\n')

#empty list to append the Document file to
w= []
##append Document string into a list
for i in range(len(p)):
    w.append((a.split('\n')[i]).split(' '))
    
we=[]
wr=[]
#append columns 1 and 2 of the list into another list
for i in range(len(w)-1):
    we.append(w[i][0])

for i in range(len(w)-1):
    wr.append(w[i][1])
    
    
#combine the two columns  
a = list(zip(we,wr))

#create a graph from the combined list
g=nx.from_edgelist(a)

#create a graph from the JSON file
G2 = nx.Graph(a)

#outputs the average clustering coefficient and the global
nx.average_clustering(g)
nx.transitivity(g)

#draws the network
nx.draw_circular(g,with_labels=True)
plt.show()

#number of edges in the network g
no=g.number_of_edges()

#remove an edge from G with probability p_remove_connection
def remov(G, p_remove_connection):    

    for node in G.nodes():    
        # find the other nodes this one is connected to    
        connected = [to for (fr, to) in G.edges(node)]    
        # and find the remainder of nodes, which are candidates for new edges   
        unconnected = [n for n in G.nodes() if not n in connected]    

        # probabilistically remove a random edge    
        if len(connected): # only try if an edge exists to remove    
            if random.random() < p_remove_connection:    
                remove = random.choice(connected)    
                G.remove_edge(node, remove) 
                connected.remove(remove)    
                unconnected.append(remove)    
    return
    
        
sorted(g.degree, key=lambda x: x[1], reverse=True)

x=[]

#carry the function for deletion of edges while $\alpha$ is less than some value ten times and add the global clustering coefficient to an empty list
for i in range(10):
    #replace g to the start since we remove edges everytime
     g=nx.from_edgelist(aa)
     while True:
        #remove an edge from g with prob 0.5 if the proportion of edges is less than 0.1
         if (no-g.number_of_edges())/no<0.1:
             remov(g,0.5)
         elif (no-g.number_of_edges())/no >=0.1:
            #appends the global clustering coefficient to the empty list x
             x.append(nx.transitivity(g))
             break

#find the average global clustering coefficient
p1=sum(x)/len(x)
#reset the list
x=[]
p2=sum(x)/len(x)

pl=[]
pl.append(p1)
# carry out this up to p9
#
b=np.linspace(0,0.9,10)
#creates the x timesteps
b=['%.1f' % elem for elem in b]
xi = list(range(len(b)))


plt.plot(xi,pl)
plt.xticks(xi,b)
plt.show()


#function that deletes one edge from a graph
def rande(graph, del_orig=True):
     edges = list(graph.edges)
     chosen_edge = random.choice(edges)
     if del_orig:
         # delete chosen edge
         graph.remove_edge(chosen_edge[0], chosen_edge[1])
     return graph




sorted(g.degree, key=lambda x: x[1], reverse=True)


for i in range(10):
     g=nx.Graph(a)
     while True:
         hi=sorted(g.degree, key=lambda x: x[1], reverse=True)
         po=nx.Graph(g.edges(hi[0][0]))
         if (no-g.number_of_edges())/no<0.4:
             rande(po,del_orig=True)
             g.remove_node(hi[0][0])
             g.add_edges_from(po.edges)
         elif (no-g.number_of_edges())/no>=0.4:
             x.append(nx.transitivity(g))
             break
    
#removes a random edge from the node with the highest degree    
for i in range(3):
     g=nx.Graph(a)
     while True:
        #sorts the degrees of the nodes of g from highest to lowest
         hi=sorted(g.degree, key=lambda x: x[1], reverse=True)
         #remove an edge from the node with highest degree until 0.5 proportion of edges have been removed
         if (no-g.number_of_edges())/no<0.5:
             po=list(g.edges(hi[0][0]))
             g.remove_edge(hi[0][0],random.choice(po)[1])
         elif (no-g.number_of_edges())/no>=0.5:
             x.append(nx.transitivity(g))
             break
    
#removes a random edge from a randomly chosen node with weighted nodes    
for i in range(10):
     g=nx.from_edgelist(a)
     while True:
        #sorts the degrees of the nodes of g from highest to lowest
         hi=sorted(g.degree, key=lambda x: x[1], reverse=True)
         #get the degree of the node and weight them so they are chosen with their given weights
         c2=[tple[1] for tple in hi]
         rc=random.choices(hi,weights=c2,k=1)
         po=list(g.edges(rc[0][0]))
         if (no-g.number_of_edges())/no<0.5:
             g.remove_edge(po[0][0],random.choice(po)[1])
         elif (no-g.number_of_edges())/no>=0.5:
             x.append(nx.transitivity(g))
             break
    
    
    
for i in range(room_height*room_width):
     if coun(room,1,room_width,room_height)<100:
         room[np.random.randint(room_height,size=1)[0]][np.random.randint(room_width,size=1)[0]]=1
     elif coun(room,1,room_width,room_height)>=100:
         pass