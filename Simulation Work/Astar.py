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

def heuristic_function(curr, desired):
	d_max = max(abs(curr[0] - desired[0]), abs(curr[1] - desired[1]))
	d_min = min(abs(curr[0] - desired[0]), abs(curr[1] - desired[1]))

	diag_cost = math.sqrt(2)
	side_cost = 1

	return (diag_cost*d_min + side_cost*(d_max - d_min))

def get_shortest_path(path):
	x = []
	y = []
	for i in range(len(path)):
		x.append(path[i][0])
		y.append(path[i][1])
	return x, y

def a_star(graph, start, desired):
	x, y = start[0], start[1]
	graph[x][y]['distance'] = 0
	graph[x][y]['heuristic'] = heuristic_function(start, desired)
	graph[x][y]['f'] = graph[x][y]['heuristic'] + graph[x][y]['distance']
	graph[x][y]['visited'] = True

	finished = []
	started_heap = []

	heapq.heappush(started_heap, (graph[x][y]['f'], (x, y)))

	while started_heap:
		pop = heapq.heappop(started_heap)
		distance = pop[0]
		curr_x, curr_y = pop[1]
		finished.append((curr_x, curr_y))

		plt.scatter(curr_x, curr_y, color="green")

		if ((curr_x, curr_y) == desired):
			# Reached the end
			break
		for i in range(max(curr_x - 1, 0), min(curr_x + 2, 35)):
			for j in range(max(curr_y - 1, 0), min(curr_y + 2, 35)):
				if (graph[i][j]['valid']):
					if (i, j) not in finished:
						if i == curr_x or j == curr_y:
							delta = 1
						else:
							delta = math.sqrt(2)
						curr_d = graph[curr_x][curr_y]['distance'] + delta

						if graph[i][j]['distance'] > curr_d:
							graph[i][j]['distance'] = curr_d
							graph[i][j]['parent'] = (curr_x, curr_y)
						graph[i][j]['heuristic'] = heuristic_function((i, j), desired)
						graph[i][j]['f'] = graph[i][j]['heuristic'] + graph[i][j]['distance']

						if not graph[i][j]['visited']:
							graph[i][j]['visited'] = True
							heapq.heappush(started_heap, (graph[i][j]['f'], (i, j)))
						else:
							for item in started_heap:
								if item[1] == (i, j):
									item[0] == graph[i][j]['f']
							heapq.heapify(started_heap)

	if ((curr_x, curr_y) != desired):
		print("Could not reach desired point")
		return (0, desired)

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

	distance, path = a_star(graph, (2, 2), (32, 32))
	print('Distance: %f' %distance)
	print(path[::-1])

	path_x, path_y = get_shortest_path(path)

	plt.plot(path_x, path_y, color='blue')
	plt.grid(True, which='major', linestyle='-')
	plt.grid(True, which='minor', linestyle='--')
	plt.title("A* Algorithm")
	plt.xlabel("x")
	plt.ylabel("y")
	plt.show(block=True)
    