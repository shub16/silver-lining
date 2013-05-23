import networkx as nx
import matplotlib.pyplot as plt
def rank(g):
	old=dict()
	new=dict()
	for x in g.nodes():
		old[x]=1
		new[x]=0
	n=len(g.nodes())
	i=0
	while(i<100):
		for x in g.nodes():
			new[x]=0
			for y in g.predecessors(x):
				new[x]+=0.85*(old[y]/g.out_degree(y))
			new[x]+=0.15
		old=new
		i+=1
	print "Ranking of the nodes are given below:"
	print(new)
	nx.draw(g)
	plt.show()	
