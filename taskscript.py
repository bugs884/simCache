import subprocess
import numpy as np
import csv
import matplotlib.pyplot as plt

Listplot = np.array([])
benchmark=["fibonacci","matmul","pi","whetstone","memcopy"]
#Create Subprocesses for each config and add output in Log
for x in range(0,5):
	for j in range(0,8):
	  for i in range(0,4):
	  	nsets = (2**j)*1024
	  	bsize = (2**(i+3))
	  	argv = "dl1:"+str(nsets)+":"+str(bsize)+":1:l"
	  	#print argv
	  	resultarg = "results/log"+str((j*4)+i)+benchmark[x]+".out"
	  	bench = "benchmarks/"+benchmark[x]
	  	inp = ["./sim-cache", "-redir:sim",resultarg,"-cache:dl1", argv,"-cache:il1", "il1:512:32:1:l", "-cache:dl2" ,"ul2:1024:64:4:l", "-cache:il2","dl2",bench]
	  	#print inp
 	  	subprocess.Popen(inp).communicate()
# #Extract Missrate from logs and create a list
X_Axis= np.array([1,2,3,4])
my_xticks = ['8B', '16B', '32B', '64B']
for x in range(0,5):
	bench= benchmark[x]
	#print bench
	for n in range (0,32):
		path = "results/log" +str(n)+bench+".out"
		#print path
		log =open(path,'r')	
		for line in log:
			if line.find('dl1.miss_rate') == 0:
	#	  		print(float(line.split()[1]))
		 		Listplot= np.append(Listplot,float((line.split()[1])))
    #Plot grapgs for each Benchmark
	splitarray=np.array_split(Listplot,8)
	print splitarray
	plt.plot(X_Axis,splitarray[0])
	plt.plot(X_Axis,splitarray[1])
	plt.plot(X_Axis,splitarray[2])
	plt.plot(X_Axis,splitarray[3])
	plt.plot(X_Axis,splitarray[4])
	plt.plot(X_Axis,splitarray[5])
	plt.plot(X_Axis,splitarray[6])
	plt.plot(X_Axis,splitarray[7])
	plt.ylabel('Miss Rate')
	plt.xlabel('Block size')
	plt.xticks(X_Axis, my_xticks)
	plt.title(bench, fontsize=16)
	plt.legend(['1K','2K','4K','8K','16K','32K','64K','128K'], loc='upper right')
	plt.show()  
	Listplot = np.array([])

#Create a plot for comparing Benchmarks
# def autolabel(rects):
#     """
#     Attach a text label above each bar displaying its height
#     """
#     for rect in rects:
#         height = rect.get_height()
#         #print height
#         ax.text(rect.get_x() + rect.get_width()/2.,1.01*height,'%.4f' % float(height),ha='center', va='bottom',fontsize=10 )

# X_Axis=np.array([1,2,3,4,5])
# my_xticks = ['Fibonacci','Matmul','Pi','Whetstone','Memcopy']
# for x in range(0,5):
# 	bench = benchmark[x]
# 	path = "results/log0"+bench+".out"
# 	log =open(path,'r')	
# 	for line in log:
# 		if line.find('dl1.miss_rate') == 0:
# 	#	  		print(float(line.split()[1]))
# 	 		Listplot= np.append(Listplot,float((line.split()[1])))
# print Listplot
# fig, ax = plt.subplots()
# rect1=ax.bar(X_Axis,Listplot)
# ax.set_ylabel('Miss Rate')
# ax.set_xlabel('Benchmarks')
# ax.set_title("Miss Rate comparision accross Benchmarks(Sets=1K , Block Size = 8B)", fontsize=10)
# ax.set_xticks(X_Axis)
# ax.set_xticklabels(my_xticks)
# autolabel(rect1)
# plt.show()
# # #fig.savefig('Graphs/step1/Across.png')
# # #print Listplot
# # # with open('Step1.csv', 'wb') as myfile:
# # #     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
# # #     wr.writerow(Listplot)
