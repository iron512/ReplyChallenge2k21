#!/usr/bin/python

from sklearn.cluster import KMeans
from pprint import pprint

import sys
import os
import math 
import numpy as np

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

def solutionC(handler):
	output = open("../outputs/" + handler.name.replace("../inputs","")[1] + "_exec.out", "w")
	#Write here the solution
	first = handler.readline().split()

	width = int(first[0])
	height = int(first[1])

	second = handler.readline().split()

	buildCount = int(second[0])
	antCount = int(second[1])
	reward = int(second[2])

	print(buildCount)
	print(antCount)
	print(reward)

	buildings = []
	antennas = []

	for z in range(0,buildCount):
		res = handler.readline().split()
		buildings.append((int(res[0]),int(res[1]),int(res[2]),int(res[3]),z))

	for x in range(0,antCount):
		res = handler.readline().split()
		antennas.append((x,int(res[0]),int(res[1])))

	buildings.sort(key=lambda buildings:buildings[3])
	antennas.sort(key=lambda antennas:antennas[2])

	output.write(str(antCount) + "\n")

	for x in range(0,antCount):
		output.write(str(antennas[x][0]) + " " + str(buildings[x][0]) + " " + str(buildings[x][1]) + "\n")

	output.close()

def solution(handler):
	output = open("../outputs/" + handler.name.replace("../inputs","")[1] + "_exec.out", "w")
	#Write here the solution
	first = handler.readline().split()

	width = int(first[0])
	height = int(first[1])

	second = handler.readline().split()

	buildCount = int(second[0])
	antCount = int(second[1])
	reward = int(second[2])

	print(buildCount)
	print(antCount)

	buildings = []
	antennas = []

	arr = []
	matrix = [ [ 0 for i in range(width) ] for j in range(height) ] 

	for z in range(0,buildCount):
		res = handler.readline().split()
		res = (int(res[0]),int(res[1]),int(res[2]),int(res[3]),z)
		buildings.append(res)
		
		matrix[int(res[1])][int(res[0])] = 1
		arr.append([int(res[1]),int(res[0])])

		#disp = int((np.log2(res[2])))

		#for x in range(-disp,+disp+1):
		#	for y in range(-disp,+disp+1):
		#		if np.abs(x) + np.abs(y) <= disp:
		#			if res[1]+y >= 0 and res[1]+y < height and res[0]+x >= 0 and res[0]+x < width:
		#				matrix[res[1]+y][res[0]+x] = max(int(np.ceil(res[2]/pow(2,(np.abs(x)+np.abs(y))))),matrix[res[1]+y][res[0]+x])


	for x in range(0,antCount):
		res = handler.readline().split()
		antennas.append((x,int(res[0]),int(res[1])))
	#pprint(matrix)

	#arr - kmeans
	print("init kmeans")
	kmeans = KMeans(n_clusters=antCount, random_state=0).fit(arr)
	print("ended kmeans")

	labels = kmeans.labels_
	centroids = [[int(x[0]),int(x[1])] for x in kmeans.cluster_centers_]

	clusters = {}
	for val in range(0, len(labels)):
		if labels[val] not in clusters:
			clusters[labels[val]] = []
		clusters[labels[val]].append(val)

	final = []
	for key in clusters:
		final.append((key,len(clusters[key])))

	final.sort(key=lambda final:final[1], reverse=True)
	antennas.sort(key=lambda antennas:antennas[1])

	#print(centroids)
	#print(clusters)
	#print(final)
	
	output.write(str(antCount) + "\n")

	for val in range(0,len(final)):
		x = centroids[final[val][0]][1]
		y = centroids[final[val][0]][0]

		#print(str(x) + " " + str(y))
		output.write(str(antennas[val][0]) + " " + str(x) + " " + str(y) + "\n")

	output.close()


#--- MAIN ---
inputs = []

print(bcolors.YELLOW + "	PYTHON" + bcolors.RESET)
print()

print("Loading files from inputs directory:\n") 
for row in sorted(os.listdir("../inputs/")):
	row = row.replace("\n","")
	print("	- " + row)
	inputs.append(open("../inputs/"+row,"r"))

print()
#Inputs contains all the input files, lets see on which apply the algorithm
run = []
for decision in sys.argv[1:]:
	run.append(int(decision))

if len(run) != len(inputs):
	print("Wrong argument count")
	sys.exit(1)

for i in range(0,len(inputs)):
	if i == 2 and run[i] == 1:
		print("(1) Running custom on: " + bcolors.YELLOW + inputs[i].name.split("/")[-1] + bcolors.RESET)
		solutionC(inputs[i])
	elif (run[i] == 1):
		print("(1) Running algs on: " + bcolors.GREEN + inputs[i].name.split("/")[-1] + bcolors.RESET)
		solution(inputs[i])
	else:
		print("(0) Not running algs on: " + bcolors.RED + inputs[i].name.split("/")[-1] + bcolors.RESET)

print()
