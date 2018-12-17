import subprocess
import numpy as np
import csv
import matplotlib.pyplot as plt

Listplot = np.array([])
benchmark=["fibonacci","matmul","pi","whetstone","memcopy"]
#Create Subprocesses for each config and add output in Log
for x in range(0,5):
	bench = "benchmarks/"+benchmark[x]
	resultarg = "results3/log"+"0"+benchmark[x]+".out"
  	inp = ["./sim-cache","-redir:sim",resultarg, "-cache:dl1","dl1:128:32:4:l", "-cache:il1" ,"dl1","-cache:dl2" ,"dl2:2048:32:4:l" ,bench]
  	subprocess.Popen(inp).communicate()
  	resultarg = "results3/log"+"1"+benchmark[x]+".out"
  	inp = ["./sim-cache","-redir:sim",resultarg, "-cache:dl1","dl1:128:32:4:l", "-cache:il1" ,"dl1" ,"-cache:dl2" "dl2:1536:32:4:l" "-cache:il2" ,"il2:512:32:4:l",  bench]
  	subprocess.Popen(inp).communicate()
  	resultarg = "results3/log"+"2"+benchmark[x]+".out"
  	inp = ["./sim-cache","-redir:sim",resultarg, "-cache:dl1","mycache:384:32:4:l", "-cache:il1" ,"il1:128:32:4:l" ,"-cache:dl2" ,"ul2:2048:32:4:l" ,"-cache:il2" ,"dl2",  bench]
  	subprocess.Popen(inp).communicate()
  	resultarg = "results3/log"+"3"+benchmark[x]+".out"
  	inp = ["./sim-cache","-redir:sim",resultarg, "-cache:dl1","mycache:384:32:4:l", "-cache:il1" ,"il1:128:32:4:l" ,"-cache:dl2" ,"dl2:1536:32:4:l" "-cache:il2" ,"il2:512:32:4:l",  bench]
  	subprocess.Popen(inp).communicate()













# #Extract Missrate from logs and create a list
# X_Axis= np.array([1,2,3,4,5,6,7,8])
# my_xticks = ['1K','2K','4K','8K','16K','32K','64K','128K']
# for x in range(0,5):
# 	bench= benchmark[x]
# 	#print bench
# 	for n in range (0,32):
# 		path = "results/log" +str(n)+bench+".out"
# 		#print path
# 		log =open(path,'r')	
# 		for line in log:
# 			if line.find('mycache.miss_rate') == 0:
# 	#	  		print(float(line.split()[1]))
# 		 		Listplot= np.append(Listplot,float((line.split()[1])))
#     #Plot grapgs for each Benchmark
# 	splitarray=np.array_split(Listplot,4)
# 	plt.plot(X_Axis,splitarray[0])
# 	plt.plot(X_Axis,splitarray[1])
# 	plt.plot(X_Axis,splitarray[2])
# 	plt.plot(X_Axis,splitarray[3])
# 	plt.ylabel('Miss Rate')
# 	plt.xlabel('Size of cache in K')
# 	plt.xticks(X_Axis, my_xticks)
# 	plt.title(bench, fontsize=16)
# 	plt.legend(['8B', '16B', '32B', '64B'], loc='upper right')
# 	plt.show()  
# 	Listplot = np.array([])
# #Create a plot for comparing Benchmarks
# X_Axis=np.array([1,2,3,4,5])
# my_xticks = ['Fibonacci','Matmul','Pi','Whetstone','Memcopy']
# for x in range(0,5):
# 	bench = benchmark[x]
# 	path = "results/log0"+bench+".out"
# 	log =open(path,'r')	
# 	for line in log:
# 		if line.find('mycache.miss_rate') == 0:
# 	#	  		print(float(line.split()[1]))
# 	 		Listplot= np.append(Listplot,float((line.split()[1])))
# plt.bar(X_Axis,Listplot)
# plt.ylabel('Miss Rate')
# plt.xlabel('Benchmarks')
# plt.xticks(X_Axis, my_xticks)
# plt.title("Miss Rate comparision accross Benchmarks(Sets=1K , Block Size = 8B)", fontsize=10)
# plt.show()
