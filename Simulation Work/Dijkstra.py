import matplotlib.pyplot as plt
import random
import math
import numpy as np
import heapq

def make_graph():
	# generate the maze graph
	graph = [range(35) for i in range(35)]
	for i in range(35):
		for j in range(35):
			graph[i][j] = {'visited':False, 'distance':np.inf, 'valid':True}
			# ugly shape
			if i in range(6, 13) and j in range(4, 11):
				if j >= 14-i:
					graph[i][j]['valid'] = False
			# center box
			if i in range(14, 18) and j in range(11, 16):
				graph[i][j]['valid'] = False
			# middle left box
			if i in range(9, 13) and j in range(16, 21):
				graph[i][j]['valid'] = False
			# middle right box
			if i in range(18, 25) and j in range(16, 20):
				graph[i][j]['valid'] = False
			# Triangle
			if i in range(20, 29) and j in range(6, 20):
				if(j <= (13*i/8) - 26.5):
					graph[i][j]['valid'] = False
			# Top guy
			if (i in range(12, 29) and j in range(25, 29)) or (i in range(25, 29) and j in range(22, 26)):
				graph[i][j]['valid'] = False
	return graph

def get_invalid_points(graph):
 	x = []
 	y = []

 	for i in range(len(graph)):
 		for j in range(len(graph[0])):
 			if graph[i][j]['valid'] == False:
 				x.append(i)
 				y.append(j)
 	return x, y

def get_shortest_path(path):
	x = []
	y = []
	for i in range(len(path)):
		x.append(path[i][0])
		y.append(path[i][1])
	return x, y

def dijkstra(graph, start, desired):
	x, y = start[0], start[1]
	graph[x][y]['distance'] = 0
	graph[x][y]['visited'] = True
	heap = []

	heapq.heappush(heap, (graph[x][y]['distance'], (x, y)))

	while heap:
		pop = heapq.heappop(heap)
		distance = pop[0]
		curr_x, curr_y = pop[1]

		plt.scatter(curr_x, curr_y, color="green")

		if ((curr_x, curr_y) == desired):
			# Reached the end
			break 

		for i in range(max(curr_x - 1, 0), min(curr_x + 2, 35)):
			for j in range(max(curr_y - 1, 0), min(curr_y + 2, 35)):
				if (graph[i][j]['valid']):
					if i == curr_x or j == curr_y:
						delta = 1
					else:
						delta = math.sqrt(2)
					curr_d = graph[curr_x][curr_y]['distance'] + delta
					if graph[i][j]['distance'] > curr_d:
						graph[i][j]['distance'] = curr_d
						graph[i][j]['parent'] = (curr_x, curr_y)
					
					if (graph[i][j]['visited'] == False):
						graph[i][j]['visited'] = True
						heapq.heappush(heap, (graph[i][j]['distance'], (i , j)))
	v = desired
	parents = [v]

	while v != start:
		v = graph[v[0]][v[1]]['parent']
		parents.append(v)

	return (graph[desired[0]][desired[1]]['distance'], parents)

if __name__ == "__main__":
	graph = make_graph()

	x, y = get_invalid_points(graph)
	plt.ion()
	plt.axis([0, 34, 0, 34])
	plt.scatter(x, y, color="red")

	distance, path = dijkstra(graph, (2, 2), (32, 32))
	print('Distance: %f' %distance)
	print(path[::-1])
	path_x, path_y = get_shortest_path(path)

	plt.plot(path_x, path_y, color='blue')
	plt.grid(True)
	plt.title("Dijkstra's Algorithm")
	plt.xlabel("x")
	plt.ylabel("y")
	plt.show(block=True)
    
