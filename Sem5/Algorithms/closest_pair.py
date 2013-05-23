import time 
from collections import defaultdict
import math
import matplotlib.pyplot as plt
import random
def dist(point0, point1):	# dist function is used to calculate distance between two points
	a=point0[0]-point1[0]
	b=point0[1]-point1[1]
	return math.sqrt(a*a+b*b)

def subsquare(delta,point):	# subsquare function gives the indices for the subsquare containing points
	if point[0]>0:
		x=math.floor(2*point[0]/delta)
	else:
		x=math.ceil(2*point[0]/delta)
	if point[1]>0:
		y=math.floor(2*point[1]/delta)
	else:
		y=math.ceil(2*point[0]/delta)
	return (x,y)
def ClosestPair(point_list):	# finds the closest pair using randomized approach
	extracted_points=[]			# extracted_points contains the points which are already choosen
	x=random.choice(point_list)
	point_list.remove(x)
	extracted_points.append(x)
	y=random.choice(point_list)
	point_list.remove(y)
	extracted_points.append(y)
	delta=dist(x,y)
	d=defaultdict(list)			# defaultdict is dictionary used to map points with the subsquare containing it
	sub_square=subsquare(delta,x)
	d[sub_square].append(x)		
	sub_square=subsquare(delta,y)
	d[sub_square].append(y)
	Closest_pair=(x,y)
	while (len(point_list)>0):
		randomPoint=random.choice(point_list)
		point_list.remove(randomPoint)
		extracted_points.append(randomPoint)
		sub_square=subsquare(delta,randomPoint)
		new_ClosestPair=Closest_pair
		for x in range(-2,3):		# check the 25 closest subsquares 
			for y in range(-2,3):
				temp_square=(sub_square[0]+x,sub_square[1]+y)
				if temp_square in d.keys():
					for i in range(0,len(d[temp_square])):
						new_delta=dist(d[temp_square][i],randomPoint)
						if(new_delta<delta):
							delta=new_delta
							new_ClosestPair=(randomPoint,d[temp_square][i])
		if new_ClosestPair!=Closest_pair:
			new_d=defaultdict(list)
			for i in extracted_points:
				sub_square=subsquare(delta,i)
				new_d[sub_square].append(i)
			d=new_d
			Closest_pair=new_ClosestPair		# new pair of points are closest
		else:
			d[sub_square].append(randomPoint)
	return Closest_pair
list1=[]
for i in range(1,1000):
		rand=(random.random(),random.random())
		list1.append(rand)
print "The Closest pair is : "
print(ClosestPair(list1))
