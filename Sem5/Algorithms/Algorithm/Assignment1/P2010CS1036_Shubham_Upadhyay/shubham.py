import networkx as nx
import random
import copy
import matplotlib.pyplot as plt
def cut(g):
	if((nx.is_connected(g))==False):					# return when the given graph is not connected
		print("Graph is not connected!")
		return 0
	h=nx.MultiGraph()									# made a new multigraph to implement min cut
	h.add_nodes_from(x for x in g.nodes())
	for x in h.nodes():
		h.node[x]['nlist']=[x]							# each node has a attribute, a list containing the nodes that node comprised of 
	h.add_edges_from(g.edges())
	a=h.number_of_nodes()
	while(h.number_of_nodes()>2):
		p=random.choice(g.edges())
		while(g[p[0]][p[1]]['flag']==0):				# picking a random edge from the list of non selected edges
			p=random.choice(g.edges())
		for x in h.nodes():
			for y in h.node[x]['nlist']:
				if(y==p[0]):
					temp=x
				elif(y==p[1]):
					temp1=x
		a=a+1
		g[p[0]][p[1]]['flag']=0
		h.add_node(a,nlist=h.node[temp]['nlist']+h.node[temp1]['nlist'])
		for n,nbrdict in g.adjacency_iter():
			if(n==p[0]):
				dic1=nbrdict							# dic1 contains the information about the first vertex of the random edge selected
			if(n==p[1]):
				dic2=nbrdict							# dic2 contains the information about the second vertex of the random edge selected
		for key,att in dic1.iteritems():
			if(att['flag']==1):
				for b in h.nodes():						# adding edges to the new node which does not make self loops
					if(key in h.node[b]['nlist']):
						if(p[1] not in h.node[b]['nlist']):
							h.add_edge(b,a)
		for key,att in dic2.iteritems():
			if(att['flag']==1):
				for b in h.nodes():
					if(key in h.node[b]['nlist']):
						if(p[0] not in h.node[b]['nlist']):
							h.add_edge(b,a)
		for x in h.node[temp]['nlist']:
			for y in h.node[temp1]['nlist']:
				if((x,y) in g.edges()):
					g[x][y]['flag']=0
		h.remove_nodes_from([temp,temp1])
	edge=[]
	for x in g.edges():
		if g[x[0]][x[1]]['flag']==1:
			edge.append(x)
	return edge
def min_cut(g):
	nx.draw(g)
	plt.show()
	edge=[]
	min_edge=[]
	c=len(g.nodes())
	for x in g.edges():
		g[x[0]][x[1]]['flag']=1
	edge=cut(g)
	if(edge==0):
		return 0
	min_edge=edge
	for i in range(0,c*c-1):							# finding n^2 cut and taking the minimum of them
		for x in g.edges():
			g[x[0]][x[1]]['flag']=1
		edge=cut(g)
		if(len(edge)<len(min_edge)):
			min_edge=[]
			min_edge=edge
	print("Min_Cut=")
	print (min_edge)
	i=copy.deepcopy(g)
	elarge=[(u,v) for (u,v) in g.edges() if (u,v) not in min_edge]
	pos=nx.spring_layout(i)
	i.remove_edges_from(min_edge)
	nx.draw_networkx_nodes(i,pos,nodelist=i.nodes(),node_size=200)
	nx.draw_networkx_edges(i,pos,edgelist=min_edge,edge_color='r',style='dashed',width=6)
	nx.draw_networkx_edges(i,pos,edgelist=elarge,edge_color='b',width=6)
	plt.show()
	nx.draw_networkx_nodes(i,pos,nodelist=i.nodes(),node_size=200)
	nx.draw_networkx_edges(i,pos,edgelist=elarge,edge_color='b',width=6)
	plt.show()
