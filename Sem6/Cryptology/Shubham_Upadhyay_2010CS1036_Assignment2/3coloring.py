import networkx as nx
import random
import matplotlib.pyplot as plt
from time import time
def coloring(G):
	H = nx.Graph()
	edge = G.edges()
	for i in range(len(G.edges())):					# copying the graph G in H to randomly assign 3 coloring 
		H.add_edge(edge[i][0],edge[i][1])
	for a in H.nodes():
		H.node[a]['color'] = 'colorless'
	for a in H.nodes():
		red_tag = 1									# attribute for the availability of the colors
		blue_tag = 1
		green_tag = 1
		nbrs_color = []

		for j in H.neighbors(a):					# checking availability of the colors by seeing the neighbours
			nbrs_color.append(H.node[j]['color'])

		for j in range(len(nbrs_color)):
			if (nbrs_color[j] == 'red'):
				red_tag = 0
			if (nbrs_color[j] == 'blue'):
				blue_tag = 0
			if (nbrs_color[j] == 'green'):
				green_tag = 0

		if (red_tag == 0 and blue_tag == 0 and green_tag == 0):		
			return 0

		if (red_tag == 1 and blue_tag == 1 and green_tag == 1):   # randomly assign the first node a color from {red, blue, green}
			x = random.randrange(3)			
			if (x == 0): 
				H.node[a]['color'] = 'red'
			elif (x == 1): 
				H.node[a]['color'] = 'blue'
			elif (x == 2): 
				H.node[a]['color'] = 'green'

		if (red_tag == 1 and blue_tag == 0 and green_tag == 0):		
			H.node[a]['color'] = 'red'	

		if (red_tag == 0 and blue_tag == 1 and green_tag == 0):		
			H.node[a]['color'] = 'blue'
			
		if (red_tag == 0 and blue_tag == 0 and green_tag == 1):		
			H.node[a]['color'] = 'green'

		if (red_tag == 1 and blue_tag == 0 and green_tag == 1):		
			x = random.randrange(2)
			if (x == 0): 
				H.node[a]['color'] = 'red'
			elif (x == 1): 
				H.node[a]['color'] = 'green'

		if (red_tag == 0 and blue_tag == 1 and green_tag == 1):
			x = random.randrange(2)
			if (x == 0): 
				H.node[a]['color'] = 'blue'
			elif (x == 1): 
				H.node[a]['color'] = 'green'


		if (red_tag == 1 and blue_tag == 1 and green_tag == 0):		
			x = random.randrange(2)
			if (x == 0): 
				H.node[a]['color'] = 'blue'
			elif (x == 1): 
				H.node[a]['color'] = 'red'
	
no_of_nodes=[]
time_taken=[]
for j in range(3,17):
	G = nx.cycle_graph(j)
	n = G.order()
	no_of_nodes.append(j)
	t1 = time()
	for i in range((3**n)-1):
		x = coloring(G)
		if (x != 0 ):
			print "3-Coloring Possible"
			break
	if(x == 0 ):
		print "3-Coloring not Possible"
	t2 = time()
	t = t2-t1
	time_taken.append(t)
plt.plot(no_of_nodes,time_taken)			# plotting a graph of number of nodes vs time taken
plt.xlabel("Number of nodes")
plt.ylabel("Time taken")
plt.show()
